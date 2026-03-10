# Legal-Tech Routing

## 目标

在 `cn-legal-workbench` 内统一调用现有技能能力，不重复造轮子。

## 继承关系

### Word 深度排版与红黑修订

优先继承：

- [../word-docx-formatting/SKILL.md](../word-docx-formatting/SKILL.md)
- [../word-docx-formatting/references/layout-presets.md](../word-docx-formatting/references/layout-presets.md)

适用：

- 需要最终 `.docx`
- 需要目录、页眉页脚、分节、连续编号
- 需要保留审阅痕迹或 tracked changes 逻辑

继承重点：

- 先分类交付类型
- 先检查样式与文档模型
- 样式优先于直接格式
- 分页符和分节符谨慎使用
- 默认保留批注与 tracked changes
- Windows 下注意 UTF-8 与非 ASCII 文件名的工具链风险

### Excel 与可编辑工作簿

优先继承：

- [../.system/spreadsheets/SKILL.md](../.system/spreadsheets/SKILL.md)

适用：

- 用户要求可编辑 `.xlsx`
- 需要 cap table、waterfall、赔偿测算表、敏感性分析表
- 需要图表或多 sheet 工作簿

### 动态网页抓取与留痕

优先继承：

- [../playwright/SKILL.md](../playwright/SKILL.md)

适用：

- 目标网站需要真实浏览器
- 页面内容是动态加载
- 需要抓取截图、快照、登录后信息、时间留痕

### 桌面截图取证

优先继承：

- [../screenshot/SKILL.md](../screenshot/SKILL.md)

适用：

- 证据只存在于桌面应用窗口
- 需要对聊天窗口、邮箱客户端、内部系统页面做屏幕取证
- 工具级截图能力不可用，需要 OS 级留痕

## 使用原则

- 主入口始终保持 `cn-legal-workbench`
- 只有在需要具体格式、浏览器自动化、可编辑表格时，才调用继承技能的方法
- 只有在证据无法直接导出时，才调用桌面截图取证
- 交付口径仍由 `cn-legal-workbench` 统一控制
