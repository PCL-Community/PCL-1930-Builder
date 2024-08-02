"""
程序启动参数管理。
"""

import argparse

parser = argparse.ArgumentParser(description="1930 文档构建器。")
parser.add_argument(
    "input",
    nargs="?",
    help="输入 Markdown 文件的位置或 URL。默认为 GitHub PCL2-1930 仓库中的 form/README.md 文件。",
    default="https://github.com/PCL-Community/PCL2-1930/blob/form/README.md",
)
parser.add_argument(
    "-o",
    "--output",
    help="输出 Json 文件的位置。默认为 output.json。",
    default="output.json",
)
parser.add_argument("-d", "--debug", help="启用调试模式。", action="store_true")
parser.add_argument(
    "-e", "--encoding", help="输入文件的编码。默认为 UTF-8。", default="utf-8"
)
parser.add_argument(
    "-t",
    "--timeout",
    help="网络请求的超时时间（秒）。默认为 10 秒。",
    type=int,
    default=10,
)
args = parser.parse_args()
