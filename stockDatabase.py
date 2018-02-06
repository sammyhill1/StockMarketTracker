from stock import stockBase, stock, stockWindowShop

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
                    stockIndex = len(self.stocks) #List is 0 indexed, so len is where we should put it (where we want it +1)
                    self.stocks.append(stock(percentRtnDesired, purchasePrice, sharesPurchased, symbol, stockIndex))

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

                # if self.stocks[symbolIndex].getTotalShares() == 0:
                #     self.stocksHistory.append(stock(symbol, self.stockIndex, None))
            else:
                raise ValueError("Stock not in portfolio!")
        except ValueError as err:
            print(err.args)

    #TODO fix this class
    def updatePortfolio(self):
        for i in self.stocks:
            self.stocks.getCurPrice()
            #Only update stocks whose share count is not 0

    def getSymbolIndex(self, symbol):
        curStock = [i for i in self.stocks if i.symbol == symbol] #Find list with symbol...TODO make this not return an entire list
        return curStock[0].stockIndex

class stockQuery(stockDatabase):

    def addNewStock(self, symbol):
        if not any(self.stocks.symbol == symbol):
            self.stocks.append(stock(symbol))
