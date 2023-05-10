# -*- coding: utf-8 -*-
"""
Created on 2023/5/9  15:46

@author: v_wweijin
"""

import requests

url = 'http://localhost:5000/api/qrcodescan'
file_list = [
    ('image', ('qrcode_zhuanlan.zhihu.com.png', open(r'C:\Users\v_wweijin\Desktop\qrcode_zhuanlan.zhihu.com.png', 'rb'))),
    ('image', ('qrcode_www.jianshu.com.png', open(r'C:\Users\v_wweijin\Desktop\qrcode_www.jianshu.com.png', 'rb'))),
    ('image', ('testqrcode.png', open(r'C:\Users\v_wweijin\Desktop\testqrcode.png', 'rb'))),
]

req = requests.post(url, files=file_list, verify=False)
req.encoding = req.apparent_encoding
rst = req.text
print(rst)
