# 旅行地图

绘制精确到地级市的旅行地图

---

### 安装

需要预先安装Matplotlib Basemap Toolkit，请阅读[文档](https://matplotlib.org/basemap/index.html)。

Windows用户可以通过[网站](https://www.lfd.uci.edu/~gohlke/pythonlibs/)下载Python Packages for Windows。

## 使用

### 地图文件

地图文件已经附加在项目内的文件夹中。可以下载最新的地图文件[Shapefile](https://gadm.org/)

地图文件内具体地名可以在`CHN_adm_shp`文件夹下查看`csv`文件。也可以在[网站](https://gadm.org/maps.html)查看

### 用户数据格式

用户输入的数据格式如下表

| 居住地 | 旅行      | 中转       | 出差           |
| ------ | --------- | ---------- | -------------- |
| 武汉市 | Hong Kong | 上海\|上海 | 杭州市         |
|        | 昆明市    | 台北       | 大理白族自治州 |

其中第一行为城市类型，城市类型名称和列数可以自定义。

中国大陆的城市名称应在`mainland_china.csv`文件的`NL_NAME_2`中查询

中国台湾应当在`taiwan_china.csv`文件的`NL_NAME_1`中查询

中国香港和中国澳门分别为`Hong Kong`和`Macao`

数据文件只支持`csv`格式，默认数据文件`sample.csv`。如需自定义需要改`travelled_map.py`文件中相应的路径。

### 运行

直接运行`travelled_map.py`即可得到`pdf`格式的旅行地图

### 许可证

木兰宽松许可证，第2版 （Mulan Permissive Software License，Version 2）

```
Copyright (c) 2019 hktkzyx
travel-map is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
```