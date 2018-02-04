#from alphaVantageClient import alphaVantageClient
#from apiCallType import apiCallType
from importantEnums import activityType

class stock():

    def __init__(self, symbol, stockIndex, percentRtnDesired = None, purchasePrice = None, sharesPurchased = None): #default percentRtnDesired to 0 in case we just want to monitor a given stock
        self.symbol = symbol
        self.stockShares = [] #List of all share activity on a individual stock
        self.percentRtnDesired = percentRtnDesired #Enter as percentage, can be None
        self.stockIndex = stockIndex

        if (sharesPurchased and purchasePrice) != None:
            self.sharePurchase(purchasePrice, sharesPurchased)

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
            totalShares += i.shareActivity

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
            totalReturn += (i.priceActivity * i.shareActivity)

        #Negative return indicates more money has been put in than gotten out
        return -totalReturn

    def getCurPrice(self):
        pass
        #apiCall = apiCallType.TIME_SERIES_INTRADAY(self.symbol, reportIntervals.daily.value, outputSizes.compact.value, dataTypes.json.value)

        #don't want to do this. Perform call, save data in parse, then just pull the values I want
        #self.curPrice = alphaVantage.request(self.symbol, )

    def sharePurchase(self, purchasePrice, sharesPurchased):
        self.stockShares.append(shareHistory(purchasePrice, sharesPurchased, activityType.buy))

    def shareSell(self, sellPrice, sharesSold):
        try:
            if self.getTotalShares() < sharesSold:
                raise ValueError("Can't sell more stocks then are in the portfolio")
            else:
                #Make the sell Negative to reflect that it's money gained!
                self.stockShares.append(shareHistory(-sellPrice, sharesSold, activityType.sell))
        except ValueError as err:
            print(err.args)



#Small "private" class to hold purchase/sell price and number of shares bought/sold
#Positive numbers are share buys, negative numbers are share sells
class shareHistory():

    def __init__(self, priceActivity, shareActivity, activityType):
        self.priceActivity = priceActivity
        self.shareActivity = shareActivity
        self.activityType = activityType
