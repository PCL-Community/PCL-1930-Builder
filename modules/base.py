"""
基础函数。
"""

import requests
from modules.args import args


def log(content: object):
    """输出日志。"""
    print(f"[INFO] {content}")


def debug(content: object):
    """输出调试日志。"""
    if args.debug:
        print(f"[DEBUG] {content}")


def read(path: str):
    """读取本地或网络文件。"""
    if path.startswith("http://") or path.startswith("https://"):
        return requests.get(
            path, timeout=args.timeout, verify=not args.ssl_no_revoke
        ).text
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
