from alphaVantageClient import alphaVantageClient
from apiCallType import apiCallType
#todo import importantEnums?

class stock():

    def __init__(self, symbol, percentRtnDesired ):
        self.stockShares = [] #List of all purchases of an individual stock
        self.symbol = symbol
        self.percentRtnDesired = percentRtnDesired #Enter as percentage

        alphaVantage = alphaVantageClient(symbol)

    def sellPriceObjective(self):
        sellPriceObjective, puchasedPrice = 0

        for i in self.stockShares:
            puchasedPrice += i.purchasePrice
        sellPriceObjective = puchasedPrice * (1+self.percentRtnDesired/100)

        return sellPriceObjective

    def getCurPrice(self):
        apiCall = apiCallType.TIME_SERIES_INTRADAY(self.symbol, reportIntervals.daily.value, outputSizes.compact.value, dataTypes.json.value)

        #don't want to do this. Perform call, save data in parse, then just pull the values I want
        self.curPrice = alphaVantage.request(self.symbol, )

    def appendSharePurchase(self, purchasePrice, sharesPurchased):
        self.stockShares.append(__sharePurchase(purchasePrice, sharesPurchased))

    def totalShares(self):
        totalShares = 0
        for i in self.stockShares:
            totalShares += i.sharesPurchased

        return totalShares

#Small "private" class to hold purchase price and number of shares of a stock buy
class __sharePurchase:

    def __init__(self, purchasePrice, sharesPurchased):
        self.purchasePrice = purchasePrice
        self.sharesPurchased = sharesPurchased
