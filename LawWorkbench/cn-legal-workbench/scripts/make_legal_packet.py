#!/usr/bin/env python3
"""Create reusable PRC legal drafting packets."""

from __future__ import annotations

import argparse
from pathlib import Path


PRESETS = {
    "contract-draft": """# 合同起草工作底稿

## 一、项目基本信息
- 项目名称：{title}
- 我方身份：
- 对方身份：
- 交易背景：
- 目标结果：

## 二、条款结构
1. 主体与定义
2. 标的与范围
3. 价款、税费、发票
4. 履行方式与期限
5. 交付与验收
6. 知识产权
7. 保密与数据合规
8. 反商业贿赂
9. 违约责任
10. 解除与终止
11. 争议解决
12. 通知与送达
13. 附件与优先顺序
""",
    "contract-review": """# 合同审核报告

## 一、整体风险评估
- 风险等级：
- 一句话结论：

## 二、必备元素缺失或瑕疵
- ...

## 三、事实描述清晰度
- ...

## 四、权利义务是否对等清晰
- ...

## 五、违约责任设计
- ...

## 六、通知条款合规性
- ...

## 七、其他重大风险点
- ...

## 八、对方可能攻击点及反制建议
- ...
""",
    "contract-modify": """# 合同修改方案

本次采用【简单修改 / 中等修改 / 完全当事人立场修改】策略，理由是：

## 一、核心修改点
- ...

## 二、红黑修订版
[在此粘贴修订文本]

## 三、最终洁净版
[在此粘贴洁净文本]
""",
    "complaint": """# 民事起诉状工作底稿

## 一、当事人信息
- 原告：
- 被告：
- 第三人：

## 二、诉讼请求
1. ...

## 三、事实与理由
- 时间轴：
- 关键违约或侵权行为：
- 证据对应：

## 四、证据目录
- ...
""",
    "defense": """# 民事答辩状工作底稿

## 一、答辩请求
1. ...

## 二、针对原告诉请的逐项答辩
- 诉请一：
- 诉请二：

## 三、事实抗辩
- ...

## 四、法律抗辩
- ...

## 五、证据与附件
- ...
""",
    "agency-plan": """# 代理方案

## 一、案件目标
- ...

## 二、核心争点
- ...

## 三、我方优势
- ...

## 四、对方最强抗辩
- ...

## 五、证据补强计划
- ...

## 六、路径比较
- 调解：
- 和解：
- 仲裁：
- 诉讼：

## 七、胜诉概率、成本与执行评估
- 胜诉概率区间：
- 时间成本：
- 费用成本：
- 执行风险：
""",
    "evidence-catalog": """# 证据目录

| 序号 | 证据名称 | 形成时间 | 证明目的 | 证明对象 | 原件/复印件 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |  |
""",
    "data-asset-opinion": """# 数据资产入表与合规法律工作底稿

## 一、项目概况
- 项目名称：{title}
- 数据类型：
- 业务场景：
- 拟实现目标：

## 二、来源与授权链
- 数据来源：
- 用户授权：
- 第三方协议：
- API/平台限制：

## 三、合规审查
- 个人信息：
- 敏感个人信息：
- 重要数据：
- 脱敏与匿名化：

## 四、入表与交易可行性
- 可控制性：
- 可计量性：
- 合规前置条件：
- 主要阻断风险：
""",
    "diligence-report": """# 尽职调查与 Red Flag 工作底稿

## 一、项目概况
- 项目名称：{title}
- 交易类型：
- 我方角色：

## 二、核查模块
- 股权结构与控制权
- 关联交易
- 重大合同
- 诉讼执行
- 税务与行政处罚
- 数据合规

## 三、Red Flag 清单
- ...

## 四、交易建议
- 可继续推进 / 有条件推进 / 暂缓 / 终止
""",
    "family-wealth-plan": """# 家族财富传承与风险隔离工作底稿

## 一、委托目标
- 项目名称：{title}
- 目标资产：
- 风险担忧：

## 二、风险识别
- 企业债务风险：
- 婚姻变动风险：
- 继承风险：
- 控制权流失风险：

## 三、工具组合
- 家族信托：
- 保险：
- 婚前/婚内安排：
- 遗嘱与继承安排：
- 持股平台与治理安排：

## 四、落地路径
- 立即动作：
- 中期动作：
- 长期维护：
""",
    "word-redline": """# 合同红黑修订与对比说明工作底稿

## 一、版本信息
- 项目名称：{title}
- 原版本号：
- 修订目标：

## 二、红黑修订版
[在此粘贴带【新增】/【删除】标记的文本]

## 三、洁净版
[在此粘贴最终洁净文本]

## 四、合同修改对比说明表
| 条款位置 | 原文要点 | 修改后要点 | 修改类型 | 修改理由 | 风险防控价值 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
""",
    "image-evidence": """# 图像与电子证据识别工作底稿

## 一、证据来源
- 项目名称：{title}
- 图片来源：
- 取证时间：
- 文件数量：

## 二、关键内容提取
- 时间：
- 主体：
- 金额：
- 关键承诺/违约表述：
- 签章信息：

## 三、时间轴与证据目录
- ...

## 四、可疑痕迹清单
- ...
""",
    "quant-analysis": """# Excel 法务量化测算工作底稿

## 一、项目名称
- 项目名称：{title}
- 测算目标：
- 测算期间：

## 二、输入变量
- 本金/基数：
- 利率/LPR：
- 天数/月份：
- 其他参数：

## 三、计算公式
- ...

## 四、测算结果
- ...

## 五、敏感变量与风险提示
- ...
""",
    "pdf-review": """# PDF 卷宗与长文本解析工作底稿

## 一、项目名称
- 项目名称：{title}
- 文档数量：
- 总页数：
- 目标风险点：

## 二、文档导航
- 文档 1：
- 文档 2：

## 三、风险地图
- ...

## 四、重点条款命中
- ...
""",
    "osint-report": """# Web OSINT 与合规监控报告

## 一、检索目标
- 项目名称：{title}
- 目标主体：
- 检索范围：
- 截止时间：

## 二、公开来源台账
- 工商：
- 执行：
- 招投标：
- 行政处罚：
- 政策文件：

## 三、命中事项与风险等级
- ...

## 四、需要进一步核验的事项
- ...
""",
    "cap-table-model": """# 股权稀释测算工作底稿

## 一、项目名称
- 项目名称：{title}
- 融资或增发轮次：

## 二、输入变量
- 股东名单：
- 当前股数：
- 新增股数：

## 三、输出指标
- 投前总股数：
- 投后总股数：
- 稀释比例：
- 控制权变化：
""",
    "cashflow-waterfall": """# Cash Flow Waterfall 工作底稿

## 一、项目名称
- 项目名称：{title}
- 交易类型：
- 可分配现金流：

## 二、顺位规则
- 顺位 1：
- 顺位 2：
- 顺位 3：

## 三、输出指标
- 各顺位实付金额：
- 缺口：
- 剩余现金流：
""",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a PRC legal drafting packet.")
    parser.add_argument("preset", choices=sorted(PRESETS.keys()))
    parser.add_argument("output", help="Target file path.")
    parser.add_argument("--title", default="未命名项目", help="Project title.")
    parser.add_argument("--force", action="store_true", help="Overwrite if file exists.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    output_path = Path(args.output)
    if output_path.exists() and not args.force:
        parser.error(f"{output_path} already exists. Use --force to overwrite.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        PRESETS[args.preset].format(title=args.title.strip() or "未命名项目"),
        encoding="utf-8",
    )
    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
