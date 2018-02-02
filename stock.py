#from alphaVantageClient import alphaVantageClient
#from apiCallType import apiCallType
#TODO import importantEnums?

class stock():

    def __init__(self, symbol, percentRtnDesired = None, purchasePrice = None, sharesPurchased = None): #default percentRtnDesired to 0 in case we just want to monitor a given stock
        self.symbol = symbol
        self.stockShares = [] #List of all purchases of an individual stock
        self.percentRtnDesired = percentRtnDesired #Enter as percentage, can be None

        if (sharesPurchased and purchasePrice) != None:
            self.addSharePurchase(purchasePrice, sharesPurchased)

        #alphaVantage = alphaVantageClient(symbol)

    def getSellPriceObjective(self):
        sellPriceObjective, puchasedPrice = 0

        for i in self.stockShares:
            puchasedPrice += i.purchasePrice
            sellPriceObjective = puchasedPrice * (1+self.percentRtnDesired/100)

        return sellPriceObjective

    def changeDesiredPercentRtn(self, newPercentRtnDesired):
        self.percentRtnDesired = newPercentRtnDesired

    def totalShares(self):
        totalShares = 0
        for i in self.stockShares:
            totalShares += i.sharesPurchased

        return totalShares

    def totalInvestment(self):
        totalInvestment = 0
        for i in self.stockShares:
            totalInvestment += (i.purchasePrice * i.sharesPurchased)

        return totalInvestment

    def getCurPrice(self):
        pass
        #apiCall = apiCallType.TIME_SERIES_INTRADAY(self.symbol, reportIntervals.daily.value, outputSizes.compact.value, dataTypes.json.value)

        #don't want to do this. Perform call, save data in parse, then just pull the values I want
        #self.curPrice = alphaVantage.request(self.symbol, )

    def addSharePurchase(self, purchasePrice, sharesPurchased):
        self.stockShares.append(sharePurchase(purchasePrice, sharesPurchased))

    def removeSharePurchase(self):
        #TODO remove this purchase from the list
        pass

#Small "private" class to hold purchase price and number of shares of a stock buy
class sharePurchase():

    def __init__(self, purchasePrice, sharesPurchased):
        self.purchasePrice = purchasePrice
        self.sharesPurchased = sharesPurchased
