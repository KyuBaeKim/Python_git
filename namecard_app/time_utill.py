import time
from datetime import datetime

def get_time_filename(ext, seq=1):
   
    now = datetime.now()
    
    file_name = f'{now.year}{now.month:02}{now.day:02}-{now.hour:02}{now.minute:02}{now.second:02}{seq:03}.{ext}'
    return file_name

def get_elapse_time(func): # 함수를 매개변수로 받는다. 
    start = time.time()
    # work1()
    func() # 매개변수로 전달받은 함수르 실행
    end = time.time()

    return(end - start)