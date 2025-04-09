
# list comp: this line of code reads in my 10 files and converts each string value to a float 
AAPL_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/AAPL.txt").readlines())]
ADBE_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/ADBE.txt").readlines())]
AMZN_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/AMZN.txt").readlines())]
F_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/F.txt").readlines())]
GOOG_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/GOOG.txt").readlines())]
JPM_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/JPM.txt").readlines())]
MCD_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/MCD.txt").readlines())]
MSFT_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/MSFT.txt").readlines())]
NKE_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/NKE.txt").readlines())]
TSLA_prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_5/TSLA.txt").readlines())]


import json 

# define function meanReversionStrategy
def meanReversionStrategy(prices, name): 
    print(name, "Mean Reversion Strategy Output:")
    i                   = 0 # indexing value to keep track 
    buy                 = 0
    trade_profit        = 0 
    first_buy           = 0
    total_profit        = 0

    for price in prices:
        if i >= 5:
            current_price = price #the next price in the list

            average = (prices[i-1] + prices[i-2] + prices[i-3]+ prices[i-4] + prices[i-5])/5 #average price for the 5 previous days
            # print("average:", average)


            if current_price < average * 0.98 and buy == 0:
                buy = current_price
                print("Buying at:", price)
                if first_buy == 0: 
                    first_buy = current_price
                    print('first_buy at:', first_buy)

            #update first_buy variable if this is the first time you buy
            elif current_price > average * 1.02 and buy !=0:
                #calculate trade profit (how much money did I make)
                print("selling at:", current_price)
                total_profit += current_price - buy
                print("trade profit:", current_price - buy)
                buy = 0 
            

            else:
                pass

        i += 1

    #outputs percent return
    percent_return = total_profit/first_buy
    print("percent_return:",round(percent_return, 2), "%")

    #ouputs first buy
    print("first_buy:",round(first_buy,2))

    #output total profit 
    print("total_profit:", round(total_profit,2))
    #return total profit and percent return
    return total_profit, percent_return


    # CALCULATE total profit
    
    total_profit += float(round(trade_profit, 2))
    print("Total_profit", total_profit)

    #calculate % return 
    final_profit_percentage = ( total_profit / first_buy ) * 100
    print("% return", round(final_profit_percentage, 2))



# define function simpleMovingAverageStrategy
def simpleMovingAverageStrategy(prices, name):
    print(name, "simple moving avg strategy:")


# simple moving average trading strategy logic

    i = 0 # indexing value to keep track 
    buy              = 0
    trade_profit     = 0 
    first_buy        = 0
    total_profit     = 0

    for price in prices:
        if i >= 5:


            current_price = price #the next price in the list

            average = (prices[i-1] + prices[i-2] + prices[i-3]+ prices[i-4] + prices[i-5])/5 #average price for the 5 previous days
          

            if current_price > average and buy == 0:
                buy = current_price
                if first_buy == 0: 
                    first_buy = current_price
                    print("first buy at:", first_buy)
                print("selling at:", price)


            #update first_buy variable if this is the first time you buy
            elif current_price < average and buy != 0:
                #calculate trade profit (how much money did I make)
                print("buying at:", current_price)
                total_profit += current_price - buy
                print("trade profit:",round( current_price - buy,2))
                buy = 0 

            else:
                pass

        i += 1
 
    #outputs percent return
    percent_return = total_profit/first_buy
    print("percent_return:",round(percent_return, 2), "%")

    #ouputs first buy
    print("first_buy:",round(first_buy,2))

    #output total profit 
    print("total_profit:", round(total_profit,2))
    #return total profit and percent return
    return total_profit, percent_return

#create results dictionary
results = {}


def saveresults(results):
    json.dump(results, open("/home/ubuntu/lizzy_homework_folder/HW_5/results.json", "w"), indent=4)


# read in 10 files 
tickers = ['AAPL', 'ADBE', 'AMZN', 'F', 'GOOG', 'JPM','MCD','MSFT','NKE', 'TSLA']


# isolate the list of prices from the file 
for ticker in tickers:
    prices = [float(line) for line in reversed(open("/home/ubuntu/lizzy_homework_folder/HW_5/" + ticker + ".txt").readlines())]

    # run mean reversion and simple moving average 
    MR_profit, MR_returns = meanReversionStrategy(prices, ticker)
    SMA_profit, SMA_returns = simpleMovingAverageStrategy(prices, ticker)
    
    # get the profit and return % from the functions and save them to a dictionary 
    results[ticker +"_prices"] = prices
    results[ticker+"_MR_profit"] = MR_profit
    results[ticker + "_MR_returns"] =MR_returns

    results[ticker+"_SMA_profit"] = SMA_profit
    results[ticker + "_SMA_returns"] =SMA_returns


# saveResults(results) # do this last and outside of for loop - save the results dictionary to a file called results.json
saveresults(results)
print("results saved to results.json")

