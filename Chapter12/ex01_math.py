# 표준 모듈
import math
# 모듈을 통해서 직접 사용 할 경우 import
print(math.sqrt(2))

from math import sqrt 
# 모듈을 통해서 함수를 사용 할 경우
print(sqrt(2))

import math as m 
# math를 m으로 사용하겠다.
print(m.sqrt(2))

from math import sqrt as sq
# 긴 함수명을 간단하게 정리하기 위해 별칭을 달아 준다.
print(sq(2))