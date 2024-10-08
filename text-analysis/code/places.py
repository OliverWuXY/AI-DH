import pandas as pd
import folium
'''
历史地名处理
'''
places_df = pd.read_csv('../data/历史地名-fromCBDB.csv')
print(places_df.columns)
# print(places_df.head())
# print(places_df['belongs1_Name'])
print(set(places_df['belongs4_Name']))
song_df = places_df[places_df['belongs4_Name'] =='宋朝']
print(song_df['c_name_chn'])

import folium
import pandas as pd


song_df =  song_df.dropna(subset=['x_coord','y_coord'])

# belongs4_Name 为宋代的数据
data = pd.DataFrame({
    'city': song_df['c_name_chn'],
    'lon': song_df['x_coord'],
    'lat': song_df['y_coord'],
    'firstyear': song_df['c_firstyear'],
    'lastyear': song_df['c_lastyear'],
})

print(data)
# 创建一个地图对象
m = folium.Map(location=[30.4194,115.7749], zoom_start=5)

# 添加标记和弹出信息
for i, row in data.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=f"{row['city']}: {row['firstyear']}-{row['lastyear']}年 "
    ).add_to(m)

# 保存地图到HTML文件
m.save('map_song.html')

