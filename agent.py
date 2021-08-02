import numpy as np
import utils

class Agent:
    # 에이전트 상태가 구성하는 값 개수
    STATE_DIM = 2 # 주식 보유 비율, 포트폴리오 가치 비율

    # 매매 수수료 및 세금
    TRADING_CHARGE = 0.00015 # 거래 수수료
    TRADING_TAX = 0.0025 # 거래세

    # 행동
    ACTION_BUY = 0
    ACTION_SELL = 1
    ACTION_HOLD = 2
    # 인공 신경망에서 확률을 구할 행동들
    ACTIONS = [ACTION_BUY, ACTION_SELL]
    NUM_ACTIONS = len(ACTIONS) # 인공 신경망에서 고려할 출력값의 개수

    def __init__(self, environment, min_trading_unit = 1, max_trading_unit = 2, delayed_reward_threshold = .05):
        # Environment
        # 현재 주식 가격을 가져오기 위해 환경 참조
        self.environment = environment

        # 최소 매매 단위, 최대 매매 단위, 지연보상 임계치
        self.min_trading_unit = min_trading_unit
        self.max_trading_unit = max_trading_unit
        # 지연 보상 임계치
        self.delayed_reward_threshold = delayed_reward_threshold

        # Agent 클래스의 속성
        self.initial_balance = 0 # 초기 자본금
        self.balance =0 # 현재 현금 잔고
        self.num_stocks = 0 # 보유 주식수
        # PV = balance + num_stocks * {현재 주식 가격}
        self.portfolio_value = 0
        self.base_portfolio_value = 0 # 직전 학습 시점의 PV
        self.num_buy  = 0 # 매수 횟수
        self.num_sell = 0 # 매도 횟수
        self.num_hold = 0 # 홀드 횟수
        self.immediate_reward = 0 # 즉시 보상
        self.profitloss = 0 # 현재 손익
        self.base_profitloss = 0 # 직전 지연 보상 이후 손익
        self.exploration_base = 0 # 탐험 행동 결정 기준

        # Agent 클래스의 상태
        self.ratio_hold = 0 # 주식 보유 비율
        self.ratio_portfolio_value = 0 # 포트폴리오 가치 비율
        