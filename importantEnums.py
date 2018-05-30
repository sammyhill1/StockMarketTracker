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
    TIME_SERIES_DAILY_ADJUSTED = 2
    TIME_SERIES_WEEKLY = 3
    TIME_SERIES_WEEKLY_ADJUSTED = 4
    TIME_SERIES_MONTHLY = 5
    TIME_SERIES_MONTHLY_ADJUSTED = 6
    BATCH_STOCK_QUOTES = 7
    CURRENCY_EXCHANGE_RATE = 8
    DIGITAL_CURRENCY_INTRADAY = 9
    SMA = 10
    EMA = 11
    WMA = 12
    DEMA = 13
    TEMA = 14
    TRIMA = 15
    KAMA = 16
    MAMA = 17
    T3 = 18
    MACD = 19
    MACDEXT = 20
    STOCH = 21
    STOCHF = 22
    RSI = 23
    STOCHRSI = 24
    WILLR = 25
    ADX = 26
    ADXR = 27
    APO = 28
    PPO = 29
    MOM = 30
    BOP = 31
    CCI = 32
    CMO = 33
    ROC = 34
    ROCR = 35
    AROON = 36
    AROONOSC = 37
    MFI = 38
    TRIX = 39
    ULTOSC = 40
    DX = 41
    MINUS_DI = 42
    PLUS_DI = 43
    MINUS_DM = 44
    PLUS_DM = 45
    BBANDS = 46
    MIDPOINT = 47
    MIDPRICE = 48
    SAR = 49
    TRANGE = 50
    ATR = 51
    NATR = 52
    AD = 53
    ADOSC = 54
    OBV = 55
    HT_TRENDLINE = 56
    HT_SINE = 57
    HT_TRENDMODE = 58
    HT_DCPERIOD = 59
    HT_DCPHASE = 60
    HT_PHASOR = 61
    SECTOR = 62
    SIZE_OF_ENUM = 63

@unique
class allOptions(Enum):
    slowlimit = 0
    fastlimit = 1
    slowperiod = 3
    fastperiod = 4
    signalperiod = 5
    slowmattype = 6
