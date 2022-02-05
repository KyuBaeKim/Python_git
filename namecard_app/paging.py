# 페이지네이션 정보를 가지는 클래스 : Paginator
# 데이터: 페이지에 담길 데이터, 페이지 번호, 전체 데이터 건수,....
import math
class Paginator :
    def __init__(self, data, page_num, counter_per_page) -> None:
        self.total_count = len(data)
        self.page = page_num
        self.total_page = math.ceil((self.total_count)/(counter_per_page)) # 나머지가 있는 경우 올림을 해야한다.
        # 1페이지: 0~9
        # 2페이지: 10~19
        self.start = (page_num-1) * counter_per_page
        self.end = self.start + counter_per_page
        self.page = data[self.start:self.end]    
    