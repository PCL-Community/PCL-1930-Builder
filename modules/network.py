"""
网络请求。
"""

import requests
from retry import retry

from modules.args import args


@retry(tries=3, delay=5)
def get(url: str, timeout: int):
    """
    执行 GET 请求。至多进行 3 次尝试。
    """
    return requests.get(
        url, timeout=timeout, verify=not args.ssl_no_revoke, allow_redirects=False
    )
