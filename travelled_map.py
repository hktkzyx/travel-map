from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn')
mpl.rcParams['figure.autolayout'] = True
mpl.rcParams['font.family'] = 'SimHei'
from matplotlib.patches import Polygon
from matplotlib.patches import Patch
from matplotlib.collections import PatchCollection
import pandas as pd

# 读取用户数据
initial_data = pd.read_csv('my_data.csv')
columns = initial_data.columns

fig, ax = plt.subplots()
# 创建图形对象
m = Basemap(
    llcrnrlon=77,
    llcrnrlat=14,
    urcrnrlon=140,
    urcrnrlat=51,
    projection='lcc',
    lat_1=33,
    lat_2=45,
    lon_0=100
)
# 读取shapefile
m.readshapefile('gadm36_CHN_shp/gadm36_CHN_0', 'china', drawbounds=True, linewidth=0.5)
m.readshapefile('gadm36_CHN_shp/gadm36_CHN_1', 'provinces', drawbounds=True, linewidth=0.5)
m.readshapefile('gadm36_CHN_shp/gadm36_CHN_2', 'cities', drawbounds=True, linewidth=0.1)
m.readshapefile('gadm36_TWN_shp/gadm36_TWN_0', 'taiwan', drawbounds=True, linewidth=0.5)
m.readshapefile('gadm36_TWN_shp/gadm36_TWN_1', 'taiwancity', drawbounds=True, linewidth=0.1)
m.readshapefile('gadm36_HKG_shp/gadm36_HKG_0', 'hk', drawbounds=True, linewidth=0.5)
m.readshapefile('gadm36_MAC_shp/gadm36_MAC_0', 'macao', drawbounds=True, linewidth=0.5)
# 选取城市
patches = {}
for col in columns:
    patches[col] = []
for info, shape in zip(m.cities_info, m.cities):
    city_name = info['NL_NAME_2']
    for col in columns:
        if city_name in initial_data[col].values:
            patches[col].append(Polygon(shape, True))
for info, shape in zip(m.taiwancity_info, m.taiwancity):
    city_name = info['NL_NAME_1']
    for col in columns:
        if city_name in initial_data[col].values:
            patches[col].append(Polygon(shape, True))
for info, shape in zip(m.hk_info, m.hk):
    city_name = info['NAME_0']
    for col in columns:
        if city_name in initial_data[col].values:
            patches[col].append(Polygon(shape, True))
for info, shape in zip(m.macao_info, m.macao):
    city_name = info['NAME_0']
    for col in columns:
        if city_name in initial_data[col].values:
            patches[col].append(Polygon(shape, True))
# 绘制城市
i = 0
for col in columns:
    ax.add_collection(PatchCollection(patches[col], facecolors='C' + str(i)))
    i += 1
# 绘制图例
types = []
i = 0
for col in columns:
    types.append(Patch(color='C' + str(i), label=col))
    i += 1
ax.legend(handles=types, loc='lower left')
ax.set_title(u'旅行地图')
fig.savefig('Travelled Map.pdf')
plt.show()
