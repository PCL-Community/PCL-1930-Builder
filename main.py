"""
1930 文档构建器。
"""

import json
from modules.markdown_lib import Markdown
from modules.args import args
from modules.base import log, read


log(f"开始构建文档：源 {args.input}")
if args.ssl_no_revoke:
    log("警告：您禁用了 SSL 证书验证，这可能导致安全问题。")
content = read(args.input)
result = Markdown(content).to_json()

with open(args.output, "w", encoding="utf-8") as f:
    log("正在写入文件")
    f.write(json.dumps(result, ensure_ascii=False, indent=4))
