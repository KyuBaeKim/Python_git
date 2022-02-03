# finally
# 예외 발생 여부와 상관없이 항상 호출
# 작업의 마무리 작업(clean up) 수행
def comm():
    try:
        print("네트워크 접속")
        a = 2/0 # division by zero
        print("네트워크 통신 수행")
    except Exception as e:
        print(e)
        return # finally를 실행한 뒤 return 한다.
    
    finally:
        print("접속 해제")

    # 성공한 경우에만 처리
    print("작업 완료")

    
def main():
    comm()
main()