import stock

class stockPortfolio(stock):

    def __init__(self):
        self.stocks = []
        super(stockPortfolio, self).__init__()

    def addStock(self, stock):
        self.stocks.append(stock)

    def updatePortfolio(self):
