# DSH 训练场

这是一个用于练习 DeepSeek Harness 的小型 Python 项目。它故意包含一个可复现的失败测试，方便你练习“只读分析 → 修复 → 验证 → 审查”的完整流程。

## 环境要求

- Python 3.10+
- 不需要安装第三方依赖
- 可选：git（用于练习查看 diff 和恢复文件）

## 快速开始

```powershell
cd 训练场
python -m unittest discover -s tests -v
```

你应该会看到一个失败：`test_restock_rejects_non_positive`。

## 目录

```text
训练场/
├── AGENTS.md                 # 项目约定（DSH 会读取）
├── README.md                 # 本文件
├── data/
│   └── orders.csv            # 只读示例数据（练习中不要修改）
├── docs/
│   ├── 需求.md               # “库存预警报告”的需求与边界
│   └── 欢迎.md               # 含一个错别字，用于 L0 练习
├── src/
│   └── inventory.py          # 库存领域模型（含一个 bug）
├── tests/
│   └── test_inventory.py     # 单元测试
└── .agents/
    └── skills/
        └── release-check/
            └── SKILL.md      # 一个可调用的 Skill 示例
```

## 约定

- 先跑测试，再改代码。
- 只改 `src/`、`tests/`、`docs/`、`README.md`、`CHANGELOG.md`。
- 不要修改 `data/orders.csv`。
- 不引入第三方依赖。
- 改完必须让测试全绿。
