class Environment:
    PRICE_IDX = 4 # 종가의 위치

    def __init__(self, chart_data = None):
        self.chart_data = chart_data # 주식 종목의 차트 데이터
        self.observation = None # 현재 관측치
        self.idx = -1  # 차트 데이터에서의 현재 위치

    def reset(self): # 리셋 , 학습을 위해
        self.observation = None
        self.idx = -1

    def observe(self): #관측 -> 뒤에 자세히 나옴

        if len(self.chart_data) > self.idx + 1:
            self.idx += 1
            self.observation = self.chart_data.iloc[self.idx]
            return self.observation
        return None
    
    def get_price(self): # 현재 관측에서 종가 얻기
        if self.observation != None:
            return self.observation[self.PRICE_IDX]
        return None

    def set_chart_data(self, chart_data):
        self.chart_data = chart_data


