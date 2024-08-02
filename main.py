"""
1930 文档构建器。
"""

import json
from pathlib import Path
from modules.markdown import Markdown
from modules.args import args
from modules.base import log, debug, read

log(f"开始构建文档：源 {args.input}")
content = read(args.input)
result = Markdown(content).to_json()

with open(args.output, "w", encoding="utf-8") as f:
    log("正在写入文件")
    f.write(json.dumps(result, ensure_ascii=False, indent=4))
