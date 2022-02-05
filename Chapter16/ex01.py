# 모듈의 정의 (util.py)
# 모듈로 사용 되지 않았으면 : main
# 모듈로 사용 되면 : util
# import는 한번만 된다.

# __name__ : 모듈명을 저장하고 있는 변수
# 실행의 주체가 되었을때 __main__ --> main은 하나다.

import util

print("linch = ", util.INCH)
print("~10 = ",util.calcsum(10))



print('ex01.py', __name__)