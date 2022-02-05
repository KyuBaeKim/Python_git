class Seq:
    def __init__(self, data) -> None:
        self.data = data
        self.index = -2
        
    def __iter__(self):
        self.index = -2
        return self
        
    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            raise StopIteration
        
        return self.data[self.index:self.index+2]

        
def main():
    solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
    
    for k in solarterm:
        print(k, end = ',')
    print()
    print('------------------------')
    
    for k in solarterm :
        print(k, end=',')
    print()
    print('------------------------')

main()