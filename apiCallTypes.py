import importantEnums 

class apiCallType:

    #String options for API call to alphaVantage
    intervals = ["1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly"]
    sizes = ["compact", "full"]
    outputTypes = ["json", "csv"]

    #todo fill in
    def __init__(self):
        pass

    class TIME_SERIES_INTRADAY(self, symbol, interval, outputSize, dataType):
        self.function = "TIME_SERIES_INTRADAY"
        self.symbol = symbol
        self.interval = interval #bound intervals by up to 60 mins
        self.outputSize = outputSize
        self.dataType = dataType

    class TIME_SERIES_DAILY(self, symbol, interval, outputSize, dataType):
        self.function = "TIME_SERIES_DAILY"
        self.symbol = symbol
        self.interval = interval #bound intervals by up to 60 mins
        self.outputSize = outputSize
        self.dataType = dataType

    class SMA(self, symbol, interval, time_period, series_type):
        self.function = "SMA"
        self.symbol = symbol
        self.interval = interval
        self.outputSize = outputSize
        self.dataType = dataType

    class EMA(self, symbol, interval, time_period, series_type):
        self.function = "EMA"
        self.symbol = symbol
        self.interval = interval
        self.outputSize = outputSize
        self.dataType = dataType
