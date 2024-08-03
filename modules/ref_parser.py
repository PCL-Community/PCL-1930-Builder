"""
解析引用。

~~感觉这将会是一个非常屎山的代码~~
"""

from dataclasses import dataclass
from enum import Enum
import markdown
import requests

from modules.args import args
from modules.base import debug


def link2html(link: str) -> str:
    """
    将 Markdown 链接转换为 HTML 链接。
    """
    return f'<a href="{link[link.index("(")+1:link.index(")")]}">{link[link.index("[")+1:link.index("]")]}</a>'


class TYPE(Enum):
    """
    引用类型。
    """

    ISSUE = 0
    PR = 1
    DISCUSSION = 2
    LINK = 3


@dataclass
class Ref:
    """
    一个引用。
    """

    ref_type: TYPE
    """引用类型。"""
    num: str
    """引用编号。"""

    def __init__(self, ref_type: TYPE, num: str) -> None:
        self.ref_type = ref_type
        self.num = num


class RefParser:
    """
    解析引用。
    """

    text: str
    """源文本。"""

    def __init__(self, text: str) -> None:
        self.text = text
        self.parse()

    def iter_ref(self):
        """
        一个生成器，找出所有可用的引用。
        """
        well = False
        num: str = ""
        square = False
        link: str = ""
        for b in self.text:
            if well:  # 正在寻找 issue / pr / discussion 编号
                if b.isdigit():
                    num += b
                    continue
                # 一个编号寻找完成，判断类型
                resp = requests.get(
                    f"https://github.com/Hex-Dragon/PCL2/issues/{num}",
                    timeout=10,  # 傻逼 GitHub 请求 pr 的时候会先 302 到 issue 再到 discussion
                    verify=not args.ssl_no_revoke,
                )
                if resp.is_redirect:
                    if "pull" in (h := resp.headers["Location"]):
                        yield Ref(TYPE.PR, f"#{num}")
                    elif "discussions" in h:
                        yield Ref(TYPE.DISCUSSION, f"#{num}")
                else:
                    yield Ref(TYPE.ISSUE, f"#{num}")
                num = ""
                well = False
                continue
            if square:  # 找到第一个圆括号结束
                link += b
                if b != ")":
                    continue
                yield Ref(TYPE.LINK, link2html(link))
                square = False
                link = ""
                continue
            if b == "#" and not square:
                well = True
            elif b == "[":
                square = True
                link += b

    issue: list[str] = []
    pull: list[str] = []
    disc: list[str] = []
    link: list[str] = []

    def parse(self):
        """
        进行解析。
        """
        result = {
            "issue": [],
            "disc": [],
            "pull": [],
            "link": [],
        }
        for ref in self.iter_ref():
            debug(f"{ref.ref_type.name}   {ref.num}")
            match ref.ref_type:
                case TYPE.ISSUE:
                    result["issue"].append(ref.num)
                case TYPE.PR:
                    result["pull"].append(ref.num)
                case TYPE.DISCUSSION:
                    result["disc"].append(ref.num)
                case TYPE.LINK:
                    result["link"].append(ref.num)
        return result
