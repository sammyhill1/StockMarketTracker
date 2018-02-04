from stock import stock

class stockDatabase():

    def __init__(self):
        self.stocks = []
        self.stockIndex = 0 #Encode this into the stock list so that it is self aware of it's position. TODO make this better
        super(stockDatabase, self).__init__()

class stockPortfolio(stockDatabase):

    def newPurchase(self, symbol, purchasePrice, sharesPurchased, percentRtnDesired = None):
        try:
            #Try a new sell, if the symbol is not found, a new stock object must be created and added to our list, but only if a desired % Rtn is defined
            if not any(i.symbol == symbol for i in self.stocks): #Returns true if any stock with that symbol is found
                if percentRtnDesired == None:
                    raise ValueError("Can't add a stock with no percentRtnDesired! You Entered:", percentRtnDesired)

                else:
                    self.stocks.append(stock(symbol, self.stockIndex, percentRtnDesired, purchasePrice, sharesPurchased))
                    self.stockIndex += 1 #Keep track of the number of total stocks purchased

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
            else:
                raise ValueError("Stock not in portfolio!")
        except ValueError as err:
            print(err.args)

    #TODO fix this class
    def updatePortfolio(self):
        for i in self.stocks:
            self.stocks.getCurPrice()

    def getSymbolIndex(self, symbol):
        curStock = [i for i in self.stocks if i.symbol == symbol] #Find list with symbol...TODO make this not return an entire list
        return curStock[0].stockIndex

class stockQuery(stockDatabase):

    def addNewStock(self, symbol):
        if not any(self.stocks.symbol == symbol):
            self.stocks.append(stock(symbol))
