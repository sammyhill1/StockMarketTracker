from enum import Enum, unique

@unique
class reportIntervals(Enum):
    min1    = 0
    min5    = 1
    min15   = 2
    min30   = 3
    min60   = 4
    daily   = 5
    weekly  = 6
    monthly = 7

@unique
class seriesTypes(Enum):
    close = 0
    open = 1
    high = 2
    low = 3

@unique
class outputSizes(Enum):
    compact = 0
    full    = 1

@unique
class dataTypes(Enum):
    json = 0
    csv  = 1

@unique
class activityType(Enum):
    buy = 0
    sell = 1
    watch = 2

@unique
class apiFunctions(Enum):
    TIME_SERIES_INTRADAY = 0
    TIME_SERIES_DAILY = 1
    TIME_SERIES_DAILY_ADJUSTED = 3
    TIME_SERIES_WEEKLY = 4
    TIME_SERIES_WEEKLY_ADJUSTED = 5
    TIME_SERIES_MONTHLY = 6
    TIME_SERIES_MONTHLY_ADJUSTED = 7
    BATCH_STOCK_QUOTES = 8
    CURRENCY_EXCHANGE_RATE = 9
    DIGITAL_CURRENCY_INTRADAY = 10
    SMA = 11
    EMA = 12
    WMA = 13
    DEMA = 14
    TEMA = 15
    TRIMA = 16
    KAMA = 17
    MAMA = 18
    T3 = 19
    MACD = 20
    MACDEXT = 21
    STOCH = 22
    STOCHF = 23
    RSI = 24
    STOCHRSI = 25
    WILLR = 26
    ADX = 27
    ADXR = 28
    APO = 29
    PPO = 30
    MOM = 31
    BOP = 32
    CCI = 33
    CMO = 34
    ROC = 35
    ROCR = 36
    AROON = 37
    AROONOSC = 38
    MFI = 39
    TRIX = 40
    ULTOSC = 41
    DX = 42
    MINUS_DI = 43
    PLUS_DI = 44
    MINUS_DM = 45
    PLUS_DM = 46
    BBANDS = 47
    MIDPOINT = 48
    MIDPRICE = 49
    SAR = 50
    TRANGE = 51
    ATR = 52
    NATR = 53
    AD = 54
    ADOSC = 55
    OBV = 56
    HT_TRENDLINE = 57
    HT_SINE = 58
    HT_TRENDMODE = 59
    HT_DCPERIOD = 60
    HT_DCPHASE = 61
    HT_PHASOR = 62
    SECTOR = 63

@unique
class allOptions(Enum):
    slowlimit = 0
    fastlimit = 1
    slowperiod = 3
    fastperiod = 4
    signalperiod = 5
    slowmattype = 6
