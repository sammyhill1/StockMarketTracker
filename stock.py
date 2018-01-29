from alphaVantageClient import alphaVantageClient
from apiCallType import apiCallType
#todo import importantEnums?

class stock():

    def __init__(self, symbol, percentRtnDesired ):
        self.stockShares = [] #List of all purchases of an individual stock
        self.symbol = symbol
        self.percentRtnDesired = percentRtnDesired #Enter as percentage

        alphaVantage = alphaVantageClient(symbol)

    def __sellPriceObjective(self):
        sellPriceObjective = puchasedPrice * (1+self.percentRtnDesired/100)
        return sellPriceObjective

    def getCurPrice(self):
        apiCall = apiCallType.TIME_SERIES_INTRADAY(self.symbol, reportIntervals.daily.value, outputSizes.compact.value, dataTypes.json.value)

        #don't want to do this. Perform call, save data in parse, then just pull the values I want
        self.curPrice = alphaVantage.request(self.symbol, )

    def appendSharePurchase(self):
        self.stockShares.append(__sharePurchase())

#Small "private" class to hold all the purchses of a given stock
class __sharePurchase:

    def __init__(self, purchasePrice, sharesPurchased):
        self.purchasePrice = purchasePrice
        self.sharesPurchased = sharesPurchased
