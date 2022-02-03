# pickle -> 파이썬 내에 사용가능 (binary로 표현되기 때문이다.)
# json -> 다른언어 호환 가능 (text로 포현되기 때문이다.)

import pickle
import json

def save(file_name, data):
    try:
        with open(file_name, "wb") as file:
            pickle.dump(data, file)
    except Exception as e:
        print(e)
  
def save_json(file_name, data):
    try:
        with open(file_name, "wt") as file:
            json.dump(data, file)
    except Exception as e:
        print(e)

def load(file_name):
    try:
        with open(file_name,'rb') as file :
            data = pickle.load(file)
            return data
    except Exception as e :
        print(e)

def load_json(file_name):
    try:
        with open(file_name,'rt') as file :
            data = json.load(file)
            return data
    except Exception as e :
        print(e)