class Data:
    def __init__(self,month) -> None:
        self.inner_month = month
        
    @property
    def month(self): #getter 함수
        return self.inner_month
    
    @month.setter
    def month(self, month): # setter 함수
        if 1<= month <= 12:
            self.inner_month = month
            
today = Data(8)
today.month = 15

print(today.month)