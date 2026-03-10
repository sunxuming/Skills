#!/usr/bin/env python3
"""Keyword-screen a contract for essential clause families."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path


KEYWORDS = {
    "主体资格与签约权限": ["当事人", "甲方", "乙方", "签约代表", "授权代表"],
    "定义条款": ["定义", "释义"],
    "标的与范围": ["服务内容", "标的", "合同内容", "合作内容"],
    "价款报酬税费": ["价款", "服务费", "报酬", "税费", "发票"],
    "履行方式与期限": ["履行", "期限", "进度", "交付时间"],
    "验收标准": ["验收", "确认", "测试标准", "验收标准"],
    "知识产权": ["知识产权", "著作权", "成果归属", "许可"],
    "保密与数据合规": ["保密", "个人信息", "数据", "信息安全"],
    "反商业贿赂": ["商业贿赂", "廉洁", "反贿赂", "合规"],
    "违约责任": ["违约", "违约金", "赔偿", "损失"],
    "不可抗力": ["不可抗力", "情势变更"],
    "争议解决": ["争议解决", "仲裁", "管辖", "法院"],
    "通知条款": ["通知", "送达", "电子邮件", "地址"],
    "转让条款": ["转让", "让与", "未经对方同意"],
    "生效终止与优先顺序": ["生效", "终止", "解除", "补充协议", "优先"],
}


def extract_docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        with archive.open("word/document.xml") as handle:
            data = handle.read().decode("utf-8", errors="ignore")
    return re.sub(r"<[^>]+>", " ", data)


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        return extract_docx_text(path)
    return path.read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    parser = argparse.ArgumentParser(description="Screen a contract for missing clause families.")
    parser.add_argument("path", help="Path to .md, .txt, or .docx contract text.")
    args = parser.parse_args()

    path = Path(args.path)
    text = read_text(path)
    missing = []
    covered = []

    for label, words in KEYWORDS.items():
        if any(word in text for word in words):
            covered.append(label)
        else:
            missing.append(label)

    print("Keyword coverage review:")
    print(f"- file: {path}")
    print("- covered:")
    for label in covered:
        print(f"  - {label}")
    print("- missing or not obvious:")
    for label in missing:
        print(f"  - {label}")
    print("- note: keyword coverage is only a screening aid, not a legal conclusion")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
