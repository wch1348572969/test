# 训练场项目约定

## 项目是什么

这是一个用于学习 DSH 的小型库存管理库。它只有一个模块 `src/inventory.py` 和一组 `unittest` 测试。

## 命令

- 运行全部测试：`python -m unittest discover -s tests -v`
- 运行单个测试：`python -m unittest tests.test_inventory.InventoryTests.test_restock_rejects_non_positive -v`
- 查看改动：`git diff`
- 查看状态：`git status --short`

## 代码约定

- 使用 Python 3.10+ 类型标注。
- 公共函数和类使用中文 docstring；内部注释可以用中文。
- 不引入第三方依赖。
- 不改变已有公开 API 的名称和参数顺序，除非任务明确要求。
- 修改前先读相关文件；不要凭文件名猜内容。
- 修 bug 先复现，再改；改完必须跑测试。

## 范围

- 允许修改：`src/`、`tests/`、`docs/`、`README.md`、`CHANGELOG.md`。
- 不要修改：`data/orders.csv`，除非任务明确要求。
- 不要删除现有测试；可以新增测试。

## 完成标准

每次任务结束前输出：

1. 修改了哪些文件；
2. 运行了什么命令；
3. 退出码；
4. 测试结果；
5. 还剩什么风险或未完成项。
