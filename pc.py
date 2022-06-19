import os
import random

import requests
import re

my_file = 'D:\Desktop\img'
if os.path.exists(my_file):
    print("文件夹已存在")
else:
    os.mkdir(my_file)
    print("文件夹不存在，创建文件夹")

data = {'test': 'data'}
headers = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           # "Accept-Language":"en-US,en;q=0.5",
           # "Accept-Encoding": "gzip, deflate",
           # "Connection":"keep-alive",
           "Content-Type": "application/x-www-form-urlencoded",
           }

while True:
    print("搜索中...")
    while True:
        page = random.randint(1, 73)
        print(page)
        url1 = 'https://www.818w.cc/c49p' + str(page) + '.aspx'
        print(url1)
        res1 = requests.get(url1)
        res1.encoding = 'utf-8'
        url1_list = re.findall(r'<a href="(.*?)" target', res1.text)
        print(url1_list)
        li = []
        for i in url1_list[14:]:
            if url1_list[0] == i:
                continue
            else:
                url2 = 'https://www.818w.cc/' + i
                print(url2)
                if url2 in li:
                    continue
                else:
                    li.append(url2)
                    res2 = requests.get(url2)
                    res2.encoding = 'utf-8'
                    a = url2[:-5]
                    # print(a)
                    end_urls = re.findall(r"p[1-9].aspx", res2.text)
                    for count in end_urls:
                        end_url = a + count
                        res3 = requests.get(end_url)
                        res3.encoding = 'utf-8'
                        img_target = re.findall(r'<img src="(.*?)" alt="" vs', res3.text)
                        # print(img_target)
                        for j in img_target:
                            d = my_file + '\\'
                            img_url = 'https://www.818w.cc/' + j
                            response = requests.get(img_url, headers=headers, params=data).content
                            path = d + j[15:-10]
                            if os.path.exists(path):
                                print("文件已存在")
                                continue
                            # print(path)
                            elif len(path) >= 26:
                                with open(path, "wb") as fp:
                                    fp.write(response)
                                    print("下载成功")
