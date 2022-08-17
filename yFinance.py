import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# def getInput():
# ticker = input("Enter ticker name ").upper()
# startDate = input("Enter a start date in format of 'YYYY-MM-DD' ")
# endDate = input("Enter a start date in format of 'YYYY-MM-DD' ")
    # return ticker, startDate, endDate

class FinanceInstrument():
    def __init__(self, ticker, startDate, endDate):
        self.ticker = ticker
        self.startDate = startDate
        self.endDate = endDate
        self.getData()
        self.LogReturn()
        self.plot()
        self.price_plot()
        self.return_plot()
        self.meanReturn()
        self.stdReturn()
        self.annualizedPref()

    def __repr__(self):
        return "FinanceInstrument(ticker={}, startDate={}, endDate={})".format(self.ticker, self.startDate, self.endDate)
        
        
    def getData(self):
        raw = yf.download(self.ticker, self.startDate, self.endDate)
        raw.rename(columns = {"Close":"price"}, inplace = True)
        self.data = raw
        print(self.data)

    def LogReturn(self):
        # print(self.data)
        price = self.data["price"]
        print(price)
        self.data["LogReturn"] = np.log(price/price.shift(1))
        print(self.data)

    def plot(self):
        # self.data.LogReturn.plot()
        # plt.show()
        # self.data.LogReturn.hist(bins=100)
        # plt.show()
        pass
    
    def meanReturn(self, freq = None):
        '''Mean Return'''
        if freq is None:
           return self.data.LogReturn.mean()
        else:
            resampledPrice = self.data.price.resample(freq).last()
            resampledReturn = np.log(resampledPrice/resampledPrice.shift(1))
            print("Mean Return : ", resampledReturn.mean())
            return resampledReturn.mean()

    def stdReturn(self, freq = None):
        '''Standard Diviation'''

        if freq is None:
            return self.data.LogReturn.std()
        else:
            resampledPrice = self.data.price.resample(freq).last()
            resampledReturn = np.log(resampledPrice/resampledPrice.shift(1))
            print("Standard Deviation : ", resampledReturn.std())
            return resampledReturn.std()
    
    def annualizedPref(self):
        '''Annualized Performance'''
        meanReturn = round(self.data.LogReturn.mean()*252,3)
        risk = round(self.data.LogReturn.std()* np.sqrt(252)*3)
        print("Return {} | Risk {}".format(meanReturn, risk))

    def price_plot(self):
        self.data.price.plot(figsize = (12, 8))
        plt.title("Return {}".format(self.ticker), fontsize = 15)
        plt.show()

    def return_plot(self, kind = "hist"):
        if kind == "ts":
            self.data.price.plot(figsize = (12, 8))
            plt.title("Return {}".format(self.ticker), fontsize = 15)
            plt.show()
        elif kind == "hist":
            self.data.price.hist(figsize = (12,8), bins = int(np.sqrt(len(self.data))))
            plt.title ("Frequency of Return {}".format(self.ticker), fontsize=15)
            plt.show()


stock = FinanceInstrument("AAPL","2000-01-01","2022-01-01")
stock.meanReturn("m")
stock.stdReturn("m")
# stock.annualizedPref()
# getInput()ticker, startDate, endDate


