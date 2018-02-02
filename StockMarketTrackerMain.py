from stockDatabase import stockPortfolio, stockQuery

def main():

    #while True:
    #These are our objects for our portfolio and our queries
    sp = stockPortfolio()
    sq  = stockQuery()

    sp.newStockPurchase("MSFT", 0.1, 78, 3)
    sp.newStockPurchase("TGI", 0.9, 24, 33)
    print (sp.stocks[0].symbol)
    print (sp.stocks[0].stockShares[0].purchasePrice)
    print (sp.stocks[0].percentRtnDesired)
    print (sp.stocks[1].symbol)
    print (sp.stocks[1].stockShares[0].purchasePrice)

    sp.newStockPurchase("MSFT", 0.4, 24, 2)
        #Run the program!
        #Let's get some user input too! Probably in a different thread

if __name__ == '__main__':

    main()
