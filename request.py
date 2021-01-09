# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:41:41 2021

@author: madhv
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())