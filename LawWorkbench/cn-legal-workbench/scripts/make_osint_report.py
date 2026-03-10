#!/usr/bin/env python3
"""Scaffold a public-source investigation report."""

from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATE = """# Web OSINT 与合规监控报告

## 一、检索目标
- 目标主体：{title}
- 检索范围：
- 截止时间：

## 二、来源台账
- 国家企业信用信息公示系统：
- 中国执行信息公开网：
- 中国政府采购网 / 公共资源交易平台：
- 监管及处罚官网：
- 地方政策官网：

## 三、命中事项
- ...

## 四、风险等级与影响
- ...

## 五、需继续官方回钩核验事项
- ...
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an OSINT report scaffold.")
    parser.add_argument("output", help="Target file path.")
    parser.add_argument("--title", default="未命名主体", help="Target subject.")
    parser.add_argument("--force", action="store_true", help="Overwrite if file exists.")
    args = parser.parse_args()

    output_path = Path(args.output)
    if output_path.exists() and not args.force:
        parser.error(f"{output_path} already exists. Use --force to overwrite.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEMPLATE.format(title=args.title.strip() or "未命名主体"), encoding="utf-8")
    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
