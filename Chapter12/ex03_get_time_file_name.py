# 다음 함수를 정의하세요.
# 함수명 : capure()
# 리턴값: 20220110-130103.jpg
from time_utill import get_time_filename
import time
def capture(seq = 1):
    file_name = get_time_filename('jpg', seq)
    # 카메라 촬영
    # 촬영한 이미지를 지정한 파일명으로 저장
    
    return file_name

def main():
    for s in range(5):
        file_name = capture(s+1)
        print(file_name)
        # sleep 실행멈춤 기능
        time.sleep(0.2)
main()