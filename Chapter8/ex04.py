file = '20200202-104830.jpg'
print("촬영 날짜 : " + file[4:6] + "월" + file[6:8] + "일")
print("촬영 시간 : " + file[9:11] + "월" + file[11:13] + "일")
print("확장자 : " + file[-3:])

# 날짜 형식의 파일명을 인자로 받고
# 날짜파트를 리턴 해주는 함수 -> 함수명: get_date_str()
# 시간 파트를 리턴해주는 함수 -> 함수명: get_time_str()

def get_date_str(file_name):
    return file_name[:4] + "년" + file_name[4:6] + "월" + file_name[6:8]
def get_time_str(file_name):
    return file_name[9:11] + "시" + file_name[11:13] + "분" + file_name[13:14] + "초"


file1 = "20221012-123960.jpg"
date_str = get_date_str(file1)
time_str = get_time_str(file1)
print("날짜 : "+ date_str)
print("날짜 : "+ time_str)
