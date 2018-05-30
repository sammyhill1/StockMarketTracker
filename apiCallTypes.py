import importantEnums

class apiCallTypes():

    #String options for API call to alphaVantage
    #TODO store these in a different way, maybe a dictionary or hash table
    functions = ["TIME_SERIES_INTRADAY",
                 "TIME_SERIES_DAILY",
                 "TIME_SERIES_DAILY_ADJUSTED",
                 "TIME_SERIES_WEEKLY",
                 "TIME_SERIES_WEEKLY_ADJUSTED",
                 "TIME_SERIES_MONTHLY",
                 "TIME_SERIES_MONTHLY_ADJUSTED",
                 "BATCH_STOCK_QUOTES",
                 "CURRENCY_EXCHANGE_RATE",
                 "DIGITAL_CURRENCY_INTRADAY",
                 "SMA",
                 "EMA",
                 "WMA",
                 "DEMA",
                 "TEMA",
                 "TRIMA",
                 "KAMA",
                 "MAMA",
                 "T3",
                 "MACD",
                 "MACDEXT",
                 "STOCH",
                 "STOCHF",
                 "RSI",
                 "STOCHRSI",
                 "WILLR",
                 "ADX",
                 "ADXR",
                 "APO",
                 "PPO",
                 "MOM",
                 "BOP",
                 "CCI",
                 "CMO",
                 "ROC",
                 "ROCR",
                 "AROON",
                 "AROONOSC",
                 "MFI",
                 "TRIX",
                 "ULTOSC",
                 "DX",
                 "MINUS_DI",
                 "PLUS_DI",
                 "MINUS_DM",
                 "PLUS_DM",
                 "BBANDS",
                 "MIDPOINT",
                 "MIDPRICE",
                 "SAR",
                 "TRANGE",
                 "ATR",
                 "NATR",
                 "AD",
                 "ADOSC",
                 "OBV",
                 "HT_TRENDLINE",
                 "HT_SINE",
                 "HT_TRENDMODE",
                 "HT_DCPERIOD",
                 "HT_DCPHASE",
                 "HT_PHASOR",
                 "SECTOR"]
    intervals = ["1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly"]
    seriesTypes = ["close", "open", "high", "low"]
    sizes = ["compact", "full"]
    dataTypes = ["json", "csv"]
    allOptions = ["slowlimit","fastlimit", "slowlimit", "fastlimit", "signalperiod",]

    def __init__(self, function, apiKey):
        self.function = self.functions[function]
        self.apiKey = apiKey

#TODO handle cases where optional arguments are entered
class StockTimeSeriesData(apiCallTypes):
    def __init__(self, function, apiKey, symbol, interval, **kwargs): #TODO Make this *args?
        super().__init__(function, apiKey)
        self.symbol = symbol
        self.interval = self.intervals[interval]

        # try:
        #     if (timePeriod == None) and (seriesType == None):
        #         raise ValueError("Stock Time Series Data must have either timePeriod or seriesType! You Entered timePeriod:", timePeriod, "You Entered seriesType:", seriesType)
        #     else:
        #         self.timePeriod = timePeriod
        #         self.seriesType = seriesType
        #
        # except ValueError as err:
        #     print(err.args)

class ForeignExchange(apiCallTypes):
    def __init__(self, *args):
        super(ForeignExchange, self).__init__(*args) #TODO make this **kwargs?
        pass

class CryptoCurrencies(apiCallTypes):
    def __init__(self, *args):
        super(CryptoCurrencies, self).__init__(*args) #TODO make this **kwargs?
        pass

class TechnicalIndicators(apiCallTypes):
    pass
    # def __init__(self, symbol, interval = None, outputSize = None, datatype, *args):
    #     super(TechnicalIndicators, self).__init__(*args) #TODO make this **kwargs?
    #     self.symbol = symbol
    #     self.interval = interval
    #     self.datatype = datatype
    #     self.outputSize = outputSize
