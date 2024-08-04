"""
Markdown 文件。
"""

import functools
import re
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

import markdown
import requests
from urllib3.exceptions import InsecureRequestWarning

from modules.base import debug
from modules.ref_parser import RefParser

CATEGORY = {
    "Minecraft": "Minecraft 常见问题",
    "PCL": "启动器常见问题",
    "Hard": "难检反馈",
    "Footnote": "脚注",
}


class MdLine:
    """
    Markdown 行。
    """

    def __init__(self, line: str):
        self.line = line

    def split(self) -> tuple[str, Optional[str], Optional[str]]:
        """
        将表格的行拆分为三个部分。
        """
        result = self.line.strip().strip("|").split("|")
        if len(result) > 3:
            raise ValueError(f"表格行格式错误：{self.line}")
        result = [i.strip() for i in result]
        return (
            result[0],
            result[1] if len(result) > 1 else None,
            result[2] if len(result) > 2 else None,
        )

    def category(self) -> Optional[str]:
        """
        如果匹配到 `BUILD_FLAG:BEGIN`，该行属于哪一段的开始。
        """
        for category in CATEGORY:
            if category in self.line:
                return category
        return None

    def is_content_start(self):
        """
        是否是表格内容的开始。
        """
        lst = self.split()
        return all(len(i.replace("-", "").replace(" ", "")) == 0 for i in lst if i)


class Markdown:
    """
    Markdown 文件。
    """

    content: str
    """文件内容。"""
    category: Optional[str] = None
    """
    当前加载到了哪个分类？
    
    遇到 `BUILD_FLAG:BEGIN` 时赋 str；遇到 `BUILD_FLAG:END` 时赋 None。
    """
    table_started: bool = False
    """表格是否已经开始了（而非仍然正在加载表头）？遇到 `BUILD_FLAG:END` 时赋 False。"""

    def __init__(self, content: str):
        self.content = content

    def __iter__(self):
        """
        迭代。只返回表格正文中的行。

        别骂了。没写过 Parser。确实很屎山。
        """
        for line in self.content.splitlines():
            l = MdLine(line)
            if "BUILD_FLAG:BEGIN" in line:
                self.category = l.category()
                debug(f"开始加载分类：{self.category}")
                continue
            if "BUILD_FLAG:END" in line:
                debug(f"该分类结束：{self.category}")
                self.category = None
                self.table_started = False
                continue
            if not self.category:
                debug(f"跳过的 Markdown 行：{line}")
                continue
            match self.category:
                case "Footnote":
                    debug(f"Markdown 脚注：{line}")
                case _:
                    result = list(l.split())
                    if not self.table_started and l.is_content_start():
                        self.table_started = True
                        debug("Markdown 表正文开始")
                        continue
                    result[0] = (
                        markdown.Markdown(output_format="html")
                        .convert(result[0])
                        .replace("<p>", "")
                        .replace("</p>", "")
                        if result[0]
                        else None
                    )
                    result[1] = (
                        markdown.Markdown(output_format="html")
                        .convert(result[1])
                        .replace("<p>", "")
                        .replace("</p>", "")
                        if result[1]
                        else None
                    )
                    if self.table_started:
                        yield result

    def to_json(self):
        """
        转为 Json 文件。
        """
        table = {}
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        executor = ThreadPoolExecutor(max_workers=15)
        for line in self:
            debug(f"加载的 Markdown 表格行：{line}")
            if not line:
                continue
            if len(line) == 0 or all(not i for i in line):
                continue
            if self.category not in table or table[self.category] is None:
                table[self.category] = []
            executor.submit(
                table[self.category].append,
                {
                    "catg": self.category,
                    "title": re.sub(r"<.*?>", "", line[0]),  # 去除格式
                    "q": line[0],
                    "a": line[1] if len(line) > 1 else "",
                    "ref": RefParser(
                        line[2] if len(line) > 2 and line[2] else ""
                    ).parse(),
                },
            )
        executor.shutdown(wait=True)
        return table
