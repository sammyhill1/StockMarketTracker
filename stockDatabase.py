from stock import stock

class stockDatabase():

    def __init__(self):
        self.stocks = []
        super(stockDatabase, self).__init__()

class stockPortfolio(stockDatabase):

    #def addNewStock(self, symbol, percentRtnDsired, purchasePrice, sharesPurchased):
    #    if symbol not in stocks
    #        self.stocks.append(stock(symbol, percentRtnDsired, purchasePrice, sharesPurchased))

    def newStockPurchase(self, symbol, percentRtnDesired, purchasePrice, sharesPurchased):
        if not any(i.symbol == symbol for i in self.stocks): #Returns true if any stock with that symbol is found
            self.stocks.append(stock(symbol, percentRtnDesired, purchasePrice, sharesPurchased))
        else:
            #TODO make more efficient find which stock we're looking for, search by symbol, retun index
            test = self.__getSymbolIndex(i for i in self.stocks if i.symbol == symbol)
            print(test.symbol)
            error

    def stockShareSell(self, symbol, sellPrice, sharesSold):
        #TODO
        pass

    def updatePortfolio(self):
        for i in self.stocks:
            self.stocks.getCurPrice()

    def __getSymbolIndex(self, default=None):
        for i in self.stocks:
            return i
        return default

class stockQuery(stockDatabase):

    def addNewStock(self, symbol):
        if not any(self.stocks.symbol == symbol):
            self.stocks.append(stock(symbol))
