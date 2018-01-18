functions = ['TIME_SERIES_INTRADAY',
             'TIME_SERIES_DAILY',
             'TIME_SERIES_DAILY_ADJUSTED',
             'TIME_SERIES_WEEKLY',
             'TIME_SERIES_WEEKLY_ADJUSTED',
             'TIME_SERIES_MONTHLY',
             'TIME_SERIES_MONTHLY_ADJUSTED',
             'BATCH_STOCK_QUOTES',
             'CURRENCY_EXCHANGE_RATE',
             'DIGITAL_CURRENCY_INTRADAY',
             'SMA',
             'EMA',
             'WMA',
             'DEMA',
             'TEMA',
             'TRIMA',
             'KAMA',
             'MAMA',
             'T3',
             'MACD',
             'MACDEXT',
             'STOCH',
             'STOCHF',
             'RSI',
             'STOCHRSI',
             'WILLR',
             'ADX',
             'ADXR',
             'APO',
             'PPO',
             'MOM',
             'BOP',
             'CCI',
             'CMO',
             'ROC',
             'ROCR',
             'AROON',
             'AROONOSC',
             'MFI',
             'TRIX',
             'ULTOSC',
             'DX',
             'MINUS_DI',
             'PLUS_DI',
             'MINUS_DM',
             'PLUS_DM',
             'BBANDS',
             'MIDPOINT',
             'MIDPRICE',
             'SAR',
             'TRANGE',
             'ATR',
             'NATR',
             'AD',
             'ADOSC',
             'OBV',
             'HT_TRENDLINE',
             'HT_SINE',
             'HT_TRENDMODE',
             'HT_DCPERIOD',
             'HT_DCPHASE',
             'HT_PHASOR',
             'SECTOR']

             #todo made "driver" where each class is each possible API call type. For posterity only
             class functions(Enum):
                              TIME_SERIES_INTRADAY         = 0
                              TIME_SERIES_DAILY            = 1
                              TIME_SERIES_DAILY_ADJUSTED   = 2
                              TIME_SERIES_WEEKLY           = 3
                              TIME_SERIES_WEEKLY_ADJUSTED  = 4
                              TIME_SERIES_MONTHLY          = 5
                              TIME_SERIES_MONTHLY_ADJUSTED = 6
                              BATCH_STOCK_QUOTES           = 7
                              CURRENCY_EXCHANGE_RATE       = 8
                              DIGITAL_CURRENCY_INTRADAY    = 9
                              SMA      = 10
                              EMA      = 11
                              WMA      = 12
                              DEMA     = 13
                              TEMA     = 14
                              TRIMA    = 15
                              KAMA     = 16
                              MAMA     = 17
                              T3       = 18
                              MACD     = 19
                              MACDEXT  = 20
                              STOCH    = 21
                              STOCHF   = 22
                              RSI      = 23
                              STOCHRSI = 24
                              WILLR    = 25
                              ADX      = 26
                              ADXR     = 27
                              APO      = 28
                              PPO      = 29
                              MOM      = 30
                              BOP      = 31
                              CCI      = 32
                              CMO      = 33
                              ROC      = 34
                              ROCR     = 35
                              AROON    = 36
                              AROONOSC = 37
                              MFI      = 38
                              TRIX     = 39
                              ULTOSC   = 40
                              DX       = 41
                              MINUS_DI = 42
                              PLUS_DI  = 43
                              MINUS_DM = 44
                              PLUS_DM  = 45
                              BBANDS   = 46
                              MIDPOINT = 47
                              MIDPRICE = 48
                              SAR      = 49
                              TRANGE   = 50
                              ATR      = 51
                              NATR     = 52
                              AD       = 53
                              ADOSC    = 54
                              OBV      = 55
                              HT_TRENDLINE = 56
                              HT_SINE      = 57
                              HT_TRENDMODE = 58
                              HT_DCPERIOD  = 59
                              HT_DCPHASE   = 60
                              HT_PHASOR    = 61
                              SECTOR       = 62)
