from alphaVantageClient import alphaVantageClient
from apiCallType import apiCallType

class stock:

    def __init__(self, symbol, puchasedPrice, percentRtnDesired ):
        self.symbol = symbol
        self.curPrice = curPrice
        self.purchasePrice = purchasePrice
        self.percentRtnDesired = percentRtnDesired #Enter as percentage

        alphaVantage = alphaVantageClient(symbol)

    def __sellPriceObjective(self):
        sellPriceObjective = puchasedPrice * (1+percentRtnDesired/100)
        return sellPriceObjective

    def getCurPrice(self):
        self.curPrice = alphaVantage.request(self.symbol, )
