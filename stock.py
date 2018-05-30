from alphaVantageClient import alphaVantageClient
#from apiCallType import apiCallType
from importantEnums import activityType, apiFunctions

class stockBase():
    def __init__(self, symbol): #default percentRtnDesired to 0 in case we just want to monitor a given stock
        self.x = 1
        self.symbol = symbol
        self.stockShares = [] #List of all share activity on a individual stock
        # super(stockBase, self).__init__()
        self.alphaVantage = alphaVantageClient(symbol)

        self.curPrice = 0; #TMT TODO create container for stock data

        #Don't define function here, define it when the desired API call is made

    def getCurPrice(self, interval):
        #apiCall = apiCallType.TIME_SERIES_INTRADAY(self.symbol, reportIntervals.daily.value, outputSizes.compact.value, dataTypes.json.value)

        #Perform call, save data, then parse
        self.curPrice = self.alphaVantage.request(apiFunctions.TIME_SERIES_INTRADAY.value ,self.symbol, interval)

        return self.curPrice

#These are stocks in which we have a vested interest
class stock(stockBase):
    def __init__(self, percentRtnDesired, purchasePrice, sharesPurchased, *args):
        super(stock, self).__init__(*args) #TODO make this **kwargs?
        self.percentRtnDesired = percentRtnDesired
        self.sharePurchase(purchasePrice, sharesPurchased) #On first init, we bought a new stock, Hooray!
        #alphaVantage = alphaVantageClient(symbol)

    def getSellPriceObjective(self):
        sellPriceObjective, puchasedPrice = 0

        for i in self.stockShares:
            puchasedPrice += i.purchasePrice
            sellPriceObjective = puchasedPrice * (1+self.percentRtnDesired/100)

        return sellPriceObjective

    def changeDesiredPercentRtn(self, newPercentRtnDesired):
        self.percentRtnDesired = newPercentRtnDesired

    def getTotalShares(self):
        totalShares = 0
        for i in self.stockShares:
            if i.activityType == activityType.buy:
                totalShares += i.shareActivity
            else:
                totalShares -= i.shareActivity

        return totalShares

    #Returns all the money put into a stock, not counting sells
    def getTotalInvestment(self):
        totalInvestment = 0
        for i in self.stockShares:
            if i.activityType == activityType.buy:
                totalInvestment += (i.priceActivity * i.shareActivity)

        return totalInvestment

    #The total amount of money you've made from investing, coutning sells and buys
    def getTotalReturn(self):
        totalReturn = 0
        for i in self.stockShares:
            if i.activityType == activityType.buy:
                totalReturn += (i.priceActivity * i.shareActivity)
            else:
                totalReturn -= (i.priceActivity * i.shareActivity)

        #Negative return indicates more money has been put in than gotten out
        return -totalReturn

    def sharePurchase(self, purchasePrice, sharesPurchased):
        self.stockShares.append(shareHistory(purchasePrice, sharesPurchased, activityType.buy))

    def shareSell(self, sellPrice, sharesSold):
        try:
            if self.getTotalShares() < sharesSold:
                raise ValueError("Can't sell more stocks then are in the portfolio")
            else:
                #Make the sell Negative to reflect that it's money gained!
                self.stockShares.append(shareHistory(sellPrice, sharesSold, activityType.sell))
        except ValueError as err:
            print(err.args)

#These are stocks we just watch, or "window shop"
class stockWindowShop(stockBase):
    pass


#Small "private" class to hold purchase/sell price and number of shares bought/sold
#Positive numbers are share buys, negative numbers are share sells
class shareHistory():

    def __init__(self, priceActivity, shareActivity, activityType):
        self.priceActivity = priceActivity
        self.shareActivity = shareActivity
        self.activityType = activityType
