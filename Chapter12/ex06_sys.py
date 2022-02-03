# sys 모듈 --> 시스템 약자
import sys
def main():
    
    print("버전 : ", sys.version)
    print("플랫폼 : ", sys.platform)
    print("바이트 순서 : ", sys.byteorder)
    print("모듈 경로 : ")
    for p in sys.path:
        print(p)
    sys.exit(0)
    print('종료합니다')
main()
    
