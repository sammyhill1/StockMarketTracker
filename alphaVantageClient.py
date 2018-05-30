#Reference https://www.alphavantage.co/documentation/
import json
import time
import logging
import requests

from apiCallTypes import *
from importantEnums import apiFunctions

# alphavantage_api_token = os.environ['alphavantage_api_token']
alphavantage_api_token = ""

#This creates the logfile
#todo: call this in a higher class maybe for global access?

#timestr = time.strftime("%Y_%m_%d-%H%M%S")
#filename = 'log_%s.log'%(timestr)
#logging.basicConfig(filename=filename,level=logging.DEBUG)

class alphaVantageClient():

    #todo fill in
    def __init__(self, symbol = None):
        self.apiKey = alphavantage_api_token
        super(alphaVantageClient, self).__init__()

    #TMT todo make this kwargs
    def request(self, function, symbol, interval):

        # self.function = functions[function]
        # payload = {"url": url, "token": token}
        json_data = None # Initialize Json Data so that it returns a null value if the call is bad
        response = self.createRequest(function, symbol, interval)
        print (response)
        # try:
        #     # print "Requesting response from {0} for Post ID: {1} : {2}".format(self.base_url, post_id, time.asctime( time.localtime(time.time()) ))
        #     print ("Here 1")
        #     #response.raise_for_status() #Eventually include to check for HTML Server Response Errors TMT
        #     # response = requests.get( params=payload)
        #     # response = requests.get(self.createRequest())
        #     response = self.createRequest(function, symbol, interval)
        #
        #     #response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=0MO8EWOIHYCQAHRW', headers=headers)
        #     #response.raise_for_status()
        #     # json_data = response.json()
        #
        # except:
        #     pass
        #     #todo log

        return json_data

    # Formats the url for the api call
    #TODO make a class method?
    def createRequest(self, function, symbol, interval):
        base_url = "https://www.alphavantage.co/query?"
        try:
            if(function < 8):
                print ("%s, %s, %s, %s" % (function, symbol, interval, self.apiKey))
                requestType = StockTimeSeriesData(function, self.apiKey, symbol, interval)

                return '{}function={}&symbol={}&interval={}&apikey={}'.format(base_url, requestType.function, requestType.symbol, requestType.interval, requestType.apiKey)

            #TMT TODO make these other types work
            elif(function < 9):
                requestType = ForeignExchange()
            elif(function < 10):
                requestType = CryptoCurrencies()
            elif(function < 63):
                requestType = TechnicalIndicators()
            else:
                raise ValueError("Function out of range. Must be less than:", apiFunctions.SIZE_OF_ENUM.value)

        except ValueError as err:
            print(err.args)
            return None
