from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.rcParams.update({'figure.autolayout': True})
from matplotlib.patches import Polygon
from matplotlib.patches import Patch
from matplotlib.collections import PatchCollection
import pandas as pd

# 读取用户数据
initial_data = pd.read_csv('sample.csv')
initial_data = initial_data.values

fig, ax = plt.subplots()
#创建图形对象
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
m.readshapefile('gadm36_CHN_shp/gadm36_CHN_1', 'provinces', drawbounds=True, linewidth=0.25)
m.readshapefile('gadm36_CHN_shp/gadm36_CHN_2', 'cities', drawbounds=True, linewidth=0.1)
m.readshapefile('gadm36_TWN_shp/gadm36_TWN_0', 'taiwan', drawbounds=True, linewidth=0.5)
m.readshapefile('gadm36_TWN_shp/gadm36_TWN_1', 'taiwancity', drawbounds=True, linewidth=0.1)
m.readshapefile('gadm36_HKG_shp/gadm36_HKG_0', 'hk', drawbounds=True, linewidth=0.5)
m.readshapefile('gadm36_MAC_shp/gadm36_MAC_0', 'macao', drawbounds=True, linewidth=0.5)
#选取城市
patches_1, patches_2, patches_3, patches_4 = [], [], [], []
for info, shape in zip(m.cities_info, m.cities):
    if info['NAME_2'] in initial_data[:, 0]:
        patches_1.append(Polygon(shape, True))
    elif info['NAME_2'] in initial_data[:, 1]:
        patches_2.append(Polygon(shape, True))
    elif info['NAME_2'] in initial_data[:, 2]:
        patches_3.append(Polygon(shape, True))
    elif info['NAME_2'] in initial_data[:, 3]:
        patches_4.append(Polygon(shape, True))
#绘制城市
ax.add_collection(PatchCollection(patches_1, facecolors='C0'))
ax.add_collection(PatchCollection(patches_2, facecolors='C1'))
ax.add_collection(PatchCollection(patches_3, facecolors='C2'))
ax.add_collection(PatchCollection(patches_4, facecolors='C3'))
#绘制图例
cities1 = Patch(color='C0', label='Resident Cities')
cities2 = Patch(color='C1', label='Working')
cities3 = Patch(color='C2', label='Travelled Cities')
cities4 = Patch(color='C3', label='Visited Cities')
ax.legend(handles=[cities1, cities2, cities3, cities4], loc='lower left')
ax.set_title('Travelled Map')
fig.savefig('Travelled Map.pdf')
plt.show()
