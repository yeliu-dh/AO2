import requests
import pandas as pd

import os, sys
import datetime


# def get_file_path(title):
#     loc=
#     year=





def save_img_to_local(url, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    response = requests.get(url)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    return 


import time
import random
import requests

def get_bilibili_title_cover(mid, pages=1):
    videos = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    
    for page in range(1, pages + 1):
        url = "https://api.bilibili.com/x/space/arc/search"
        params = {
            "mid": mid,
            "ps": 30,
            "pn": page,
            "order": "pubdate",
            "jsonp": "jsonp"
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        # ---- 限流处理 ----
        if data.get("code") == -799:
            print("请求过于频繁，正在等待重试...")
            time.sleep(3)  # 关键：休息几秒再试
            response = requests.get(url, headers=headers, params=params)
            data = response.json()

        if data.get("code") != 0:
            print(f"第{page}页请求失败：{data}")
            continue
        
        vlist = data["data"]["list"]["vlist"]
        for v in vlist:
            videos.append({
                "title": v.get("title"),
                "cover": v.get("pic"),
                "bvid": v.get("bvid")
            })

        # ---- 每页休息一下，避免被限流 ----
        time.sleep(random.uniform(0.8, 1.5))

    return videos



# def get_bilibili_title_cover(mid, pages=1):
#     #mid=Member ID

#     videos = []
#     # 设置请求头，伪装成浏览器
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                       "AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/120.0.0.0 Safari/537.36"
#     }
#     for page in range(1, pages + 1):
#         url = "https://api.bilibili.com/x/space/arc/search"
#         params = {
#             "mid": mid,
#             "ps":30,
#             "pn": page,
#             "order": "pubdate",
#             "jsonp": "jsonp"
#         }
#         response = requests.get(url, headers=headers, params=params)
#         if response.status_code != 200:
#             print(f"请求失败，第{page}页，状态码：{response.status_code}")
#             print(response.text)  # 输出错误信息
#             continue
#         data = response.json()
#         print(f"JSON DATA :{data}")
        
#         # parse
#         vlist = data.get("data", {}).get("list", {}).get("vlist", [])
#         for v in vlist:
#             videos.append({
#                 "title": v.get("title"),
#                 "cover": v.get("pic"),
#                 "bvid": v.get("bvid")
#             })

#     return videos

