# dic update
def main():
    dic = {
        'boy':'소년', 
        'school':'학교',
        'book':'책'
        }
    dic2 = {
        'student':'학생', 
        'teach':'선생님',
        'book':'서적'
        }
    
    dic.update(dic2)
    print(dic)
main()