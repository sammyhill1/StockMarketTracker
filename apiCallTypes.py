from enum import Enum

class apiCallType:

    class intervals(Enum):
        min1    = 0
        min5    = 1
        min15   = 2
        min30   = 3
        min60   = 4
        daily   = 5
        weekly  = 6
        monthly = 7

    intervals = ["1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly"]

    def __init__(self):
        pass

    def TIME_SERIES_INTRADAY(self, symbol, interval, outputSize, dataType):
        self.function = "TIME_SERIES_INTRADAY"
        self.symbol = symbol
        self.interval = interval #bound intervals by up to 60 mins
        self.outputSize = outputSize
        self.dataType = dataType

    def TIME_SERIES_DAILY(self, symbol, interval, outputSize, dataType):
        self.function = "TIME_SERIES_DAILY"
        self.symbol = symbol
        self.interval = interval #bound intervals by up to 60 mins
        self.outputSize = outputSize
        self.dataType = dataType

    def SMA(self, symbol, interval, time_period, series_type):
        self.function = "SMA"
        self.symbol = symbol
        self.interval = interval
        self.outputSize = outputSize
        self.dataType = dataType

    def EMA(self, symbol, interval, time_period, series_type):
        self.function = "EMA"
        self.symbol = symbol
        self.interval = interval
        self.outputSize = outputSize
        self.dataType = dataType
