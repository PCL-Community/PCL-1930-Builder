"""
基础函数。
"""

import requests
from urllib3.exceptions import InsecureRequestWarning

from modules.args import args


def log(content: object, hint: str = "INFO"):
    """输出日志。"""
    print(f"[{hint}] {content}")


def debug(content: object):
    """输出调试日志。"""
    if args.debug:
        print(f"[DEBUG] {content}")


def read(path: str):
    """读取本地或网络文件。"""
    if path.startswith("http://") or path.startswith("https://"):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        return requests.get(
            path, timeout=args.timeout, verify=not args.ssl_no_revoke
        ).text
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
