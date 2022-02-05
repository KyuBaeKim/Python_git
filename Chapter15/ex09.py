class Date:
    def __init__(self, month) -> None:
        self.__month = month  
        
    def getmonth(self):
        return self.__month
    
    def setmonth(self, month):
        if 1<= month <= 12:
            self.__month = month
    
    month = property(getmonth, setmonth)

today = Date(8)
today.month = 15

print(today.month)
# print(today.__month)
# __.month 는 프라이빗 멤버 변수이다. (외부에서 바로 접근이 불가하다.)