---
name: release-check
description: 发布前检查版本号、测试、变更日志和未提交改动
whenToUse: 当用户要求发布、打包、版本检查或生成 release note 时
---

# Release check

按顺序执行，不要跳过：

1. 读取 `pyproject.toml`、`package.json` 或 `README.md`，确认当前版本号；如果找不到，明确说“未找到版本号”。
2. 运行 `python -m unittest discover -s tests -v`，记录退出码和失败数。
3. 运行 `git status --short`，列出未提交改动；如果当前目录不是 git 仓库，说明原因。
4. 检查 `CHANGELOG.md` 是否存在，是否有当前版本的条目。
5. 输出一张检查表：

   | 检查项 | 结果 | 证据 |
   |---|---|---|
   | 版本号 | ... | ... |
   | 测试 | ... | ... |
   | 未提交改动 | ... | ... |
   | CHANGELOG | ... | ... |

6. 只报告，不要自动打 tag、不要 commit、不要 push、不要发布。

如果任何一项失败，明确列出阻塞项和建议的下一步。
