# QUEUE(큐) : FIFO (먼저 들어간것이 먼저 나온다.)
# EX) BUFFER : 처리속도가 다른 모듈간에 정보를 전달할때 충격을 완화시켜준다.
# BUFFER에 데이터를 저장하는 과정을 버퍼링이라 한다.
 
# STACT(큐) : LIFO (마지막에 들어간것이 먼저 나온다.)

# QUEUE 
# FIRST IN : list.append() LAST OUT : list.pop(0)

# STACK
# FIRST IN : list.append() LAST OUT : list.pop()

def main() :
    score = [88, 95, 70, 100, 99]
    score.append(50)

    print('큐', score)
    print('큐', score.pop(0))
    print('큐', score)
    print()

    score = [88, 95, 70, 100, 99] 
    score.append(50)

    print('스택', score)
    print('스택', score.pop())
    print('스택', score)
    print()
main()
