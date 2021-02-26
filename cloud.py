import requests
import json
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
import PIL

# 微博热搜 API
url = 'https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=pos%3D0_0%26mi_cid%3D100103%26cate%3D10103%26filter_type%3Drealtimehot%26c_type%3D30%26display_time%3D1582539542&luicode=10000011&lfid=231583&sudaref=m.weibo.cn&display=0&retcode=6102'
hotdict = {}

# 请求数据
response = requests.get(url).text
json_data = json.loads(response)['data']['cards'][0]['card_group'][1:]
for item in json_data:
    title = item['desc']
    hot = item['desc_extr']
    hotdict[title] = int(hot)

# 写入文件
with open('./hot.txt', 'w') as f:
    for k, v in hotdict.items():
        f.write(f"{k}: {v}\n")

# 生成词云图片
ccloud = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\simkai.ttf',
                             background_color='white', width=1600, height=800)
ccloud.generate_from_frequencies(frequencies=hotdict)

# 处理图片
plt.figure(dpi=1200)
plt.imshow(ccloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('./hot.png')
