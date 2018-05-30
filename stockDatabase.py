from stock import stockBase, stock, stockWindowShop
from importantEnums import reportIntervals

class stockDatabase():

    def __init__(self):
        self.stocks = []
        self.stocksHistory = []
        super(stockDatabase, self).__init__()

class stockPortfolio(stockDatabase):

    def newPurchase(self, symbol, purchasePrice, sharesPurchased, percentRtnDesired = None):
        try:
            #Try a new sell, if the symbol is not found, a new stock object must be created and added to our list, but only if a desired % Rtn is defined
            if not any(i.symbol == symbol for i in self.stocks): #Returns true if any stock with that symbol is found
                if percentRtnDesired == None:
                    raise ValueError("Can't add a stock with no percentRtnDesired! You Entered:", percentRtnDesired)

                else:
                    self.stocks.append(stock(percentRtnDesired, purchasePrice, sharesPurchased, symbol))

            #Otherwise add a share to an existing stock
            else:
                symbolIndex = self.getSymbolIndex(symbol)
                self.stocks[symbolIndex].sharePurchase(purchasePrice, sharesPurchased) #Add a new stock purchase
        except ValueError as err:
            print(err.args)

    def newSell(self, symbol, sellPrice, sharesSold):
        try:
            if any(i.symbol == symbol for i in self.stocks):
                symbolIndex = self.getSymbolIndex(symbol)
                self.stocks[symbolIndex].shareSell(sellPrice, sharesSold)

                #If our sell drives our total shares to 0, move that stock to stocksHistory
                if self.stocks[symbolIndex].getTotalShares() == 0:
                    stockRemoved = self.stocks.pop(symbolIndex)
                    self.stocksHistory.append(stockRemoved)
            else:
                raise ValueError("Stock not in portfolio!")
        except ValueError as err:
            print(err.args)

    #TODO fix this class
    def updatePortfolio(self):
        for i in self.stocks:
            i.getCurPrice(reportIntervals.min5.value)
            #Only update stocks whose share count is not 0

    def getSymbolIndex(self, symbol):
        #TODO add try catch for case where getSymbolIndex is not found!
        for i, stock in enumerate(self.stocks):
            if stock.symbol == symbol:
                return i

class stockQuery(stockDatabase):

    def addNewStock(self, symbol):
        if not any(self.stocks.symbol == symbol):
            self.stocks.append(stock(symbol))
