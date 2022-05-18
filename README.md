# 旅行地图

这是一个精确到城市旅行地图生成器。
本项目是基于开源项目 [pyechart](https://github.com/pyecharts/pyecharts)，
生成的中国地图符合法律规范。

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/hktkzyx/travel-map/Build%20and%20Test%20Python%20Package)](https://github.com/hktkzyx/travel-map/actions/workflows/build_and_test.yml)
[![Codecov](https://img.shields.io/codecov/c/github/hktkzyx/travel-map)](https://app.codecov.io/gh/hktkzyx/travel-map)
[![PyPI](https://img.shields.io/pypi/v/travel-map)](https://pypi.org/project/travel-map/)
[![PyPI - License](https://img.shields.io/pypi/l/travel-map)](https://github.com/hktkzyx/travel-map/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/travel-map)](https://img.shields.io/pypi/pyversions/travel-map)
[![GitHub last commit](https://img.shields.io/github/last-commit/hktkzyx/travel-map)](https://github.com/hktkzyx/travel-map/commits/main)

## 安装

```bash
pip install travel-map
```

## 使用

用户需要将旅行信息输入到一个 CSV 文件里，例如

```csv travelled_cities.csv
城市,组
北京,旅行
上海,旅行
武汉,居住
香港,中转
```

文件中城市的名称可以查阅[文件](https://github.com/pyecharts/pyecharts/blob/d1b2ecd223b6c6d429e698ec690e15bf8c40ae09/pyecharts/datasets/map_filename.json)。

然后运行命令

```bash
travel-map --title "我的旅行地图" --output travel_map.html travelled_cities.csv
```

即可生成标题为`我的旅行地图`的精确到城市的旅行地图如下

![demo](./demo/demo.png)

## 如何贡献

十分欢迎 Fork 本项目！
欢迎修复 bug 或开发新功能。
开发时请遵循以下步骤:

1. 使用 [poetry](https://python-poetry.org/) 作为依赖管理

    克隆项目后，在项目文件夹运行

    ```bash
    poetry install
    ```

2. 使用 [pre-commit](https://pre-commit.com/) 并遵守 [Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) 规范

    安装 pre-commit 并运行

    ```bash
    pre-commit install -t pre-commit -t commit-msg
    ```

    建议使用 [commitizen](https://github.com/commitizen-tools/commitizen) 提交您的 commits。

3. 遵循 [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) 分支管理策略

    安装 [git-flow](https://github.com/petervanderdoes/gitflow-avh) 管理您的分支并运行

    ```bash
    git config gitflow.branch.master main
    git config gitflow.prefix.versiontag v
    git flow init -d
    ```

4. PR 代码到 develop 分支

## 许可证

木兰宽松许可证，第2版 （Mulan Permissive Software License，Version 2）

Copyright (c) 2019 Brooks YUAN

travel-map is licensed under Mulan PSL v2.

You can use this software according to the terms and conditions of the Mulan PSL v2.

You may obtain a copy of Mulan PSL v2 at: <http://license.coscl.org.cn/MulanPSL2>

THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.

See the Mulan PSL v2 for more details.
