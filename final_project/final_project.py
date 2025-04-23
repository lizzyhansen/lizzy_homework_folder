import requests 
import json 

def simplemovingavg(prices, ticker):
    print(ticker, "simple moving avg strategy:")

    # simple moving average trading strategy logic

    i = 0 # indexing value to keep track 
    buy              = 0
    trade_profit     = 0 
    first_buy        = 0
    total_profit     = 0
    signal           = ""

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

    # give the signal to buy/sell 
    if len(prices) >= 6: 
        last_price = prices[-1]
        avg = sum(prices[-6:-1])/5
        if last_price > avg:
            signal = "SELL"
            print("you should SELL this stock today")
        elif last_price < avg:
            signal = "BUY"
            print("you should BUY this stock today")


    return total_profit, percent_return, signal 
    
def meanreversionstrat(price, ticker):
    print(ticker, "Mean Reversion Strategy Output:")
    i                   = 0 # indexing value to keep track 
    buy                 = 0
    trade_profit        = 0 
    first_buy           = 0
    total_profit        = 0
    signal              = ""

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


    if len(prices) >= 6: 
        last_price = prices[-1]
        avg = sum(prices[-6:-1])/5
        upper = avg * 1.02
        lower = avg * 0.98
        if last_price > upper:
            signal = "SELL"
            print("you should SELL this stock today")
        elif last_price < lower: 
            signal = "BUY"
            print("you should BUY this stock today")


    return total_profit, percent_return, signal 

def Bollinger_Band(prices, ticker):
    print(ticker, "Bollinger Band Strategy:")
    i                   = 0 # indexing value to keep track 
    buy                 = 0
    trade_profit        = 0 
    first_buy           = 0
    total_profit        = 0
    signal              = ""

    for price in prices:
        if i >= 5:
            current_price = price #the next price in the list

            average = (prices[i-1] + prices[i-2] + prices[i-3]+ prices[i-4] + prices[i-5])/5 #average price for the 5 previous days
            # print("average:", average)

            upper_threshold = average * 1.05 #5% above
            lower_threshold = average * 0.95 #5% below 


            if current_price > upper_threshold:
                if buy  == 0:
                    buy = current_price
                    if first_buy == 0:
                        first_buy = current_price
                    print("Buying at:", price)
                    print('first_buy at:', first_buy)

            #update first_buy variable if this is the first time you buy
            elif current_price > average * 1.02 and buy !=0:
                #calculate trade profit (how much money did I make)
                print("selling at:", current_price)
                trade_profit = current_price - buy
                total_profit += trade_profit
                print("trade profit:", current_price - buy)
                buy = 0
        
            else:
                pass

        i += 1
    if first_buy > 0:
        percent_return = total_profit/first_buy
    else: 
        percent_return = 0 

    #outputs percent return
    percent_return = total_profit/first_buy
    print("percent_return:",round(percent_return, 2), "%")

    #ouputs first buy
    print("first_buy:",round(first_buy,2))

    #output total profit 
    print("total_profit:", round(total_profit,2))

    # signal on last day whether to buy/sell
    if len(prices) >= 6: 
        last_price = prices[-1]
        avg = sum(prices[-6:-1])/5
        upper = avg * 1.05
        lower = avg * 0.95
        if last_price > upper:
            signal = "BUY"
            print("you should BUY this stock today")
        elif last_price < lower: 
            signal = "SELL"
            print("you should SELL this stock today")


    #return total profit and percent return
    return total_profit, percent_return, signal

def saveresults(results):
    json.dump(results, open("/home/ubuntu/final_project/results.json", "w"), indent=4)

def initialDataPull(tickers):
    for ticker in tickers:
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

    # making the api call for our stock
        request = requests.get(url)
        request_dictionary = json.loads(request.text)

        # keys
        key_0 = "Time Series (Daily)"
        # key_1 = "2025-04-08"
        key_2 = "4. close"

        lines = []

        for date in request_dictionary[key_0].keys():
            lines.append(date + "," + request_dictionary[key_0][date][key_2] + "\n")

        lines = lines[::-1]

        with open("/home/ubuntu/lizzy_homework_folder/final_project/data/"+ticker+".csv", "w") as file:
            file.writelines(lines)

def appendData(tickers):
    for ticker in tickers: 
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

        # making the api call for our stock
        request = requests.get(url)
        request_dictionary = json.loads(request.text)

        # keys
        key_0 = "Time Series (Daily)"
        #key_1 = "2025-04-08"
        key_2 = "4. close"

        # open pre-existing files 
        with open("/home/ubuntu/lizzy_homework_folder/final_project/data/"+ticker+ ".csv", "r") as file:
            csv_lines = file.readlines()

        # getting the most recent date from our csv file
        latest_date = csv_lines[-1].split(",")[0]

        new_lines = []

        for date in request_dictionary[key_0].keys():
            if date == latest_date:
                break 
            else:
                new_lines.append(date + "," + request_dictionary[key_0][date][key_2] + "\n")

        new_lines = new_lines[::-1]


            #add new data 
        with open("/home/ubuntu/lizzy_homework_folder/final_project/data/"+ticker+".csv", "a") as file:
            file.writelines(new_lines)
    

    # track the last date added to our file 
    # check the last date in the file 
    pass

#initializing variables we'll need all through the code
results = {}
most_profit   = 0 
best_strat    = ""
best_ticker   = ""

tickers = ['AAPL', 'ADBE', 'AMZN', 'F', 'GOOG', 'JPM','MCD','MSFT','NKE', 'TSLA']
# initialDataPull(tickers) #once all data is in, comment this line out.


for ticker in tickers:
    prices = [float(line.split(",")[1]) for line in reversed(open("/home/ubuntu/lizzy_homework_folder/final_project/data/" + ticker + ".csv").readlines())]

# call functions 
    MR_profit, MR_returns, MR_signal = meanreversionstrat(prices, ticker)
    SMA_profit, SMA_returns, SMA_signal = simplemovingavg(prices, ticker)
    BB_profit, BB_returns, BB_signal = Bollinger_Band(prices, ticker)
    
    # get the profit and return % from the functions and save them to a dictionary 
    results[ticker +"_prices"] = prices
    results[ticker+"_MR_profit"] = round (MR_profit, 2)
    results[ticker + "_MR_returns"] = round(MR_returns,2)
    results[ticker + "_MR_signal"] = MR_signal 

    results[ticker+"_SMA_profit"] = round(SMA_profit, 2)
    results[ticker + "_SMA_returns"] = round(SMA_returns, 2)
    results[ticker + "_SMA_signal"] = BB_signal 

    if MR_profit > most_profit: 
        most_profit = MR_profit 
        best_strat = "Mean Reversion"
        best_ticker = ticker
    elif SMA_profit > most_profit: 
        most_profit = SMA_profit 
        best_strat = "Simple Moving Average"
        best_ticker = ticker 
    elif BB_profit > most_profit:
        most_profit = BB_profit 
        best_strat = "Bollinger Band Strategy"
        best_ticker = ticker


    results["best_ticker"] = best_ticker 
    results["best_strategy"] = best_strat
    results["best_profit"] = round(most_profit,2)

print("The best ticker was:", best_ticker)
print("The best strategy was:", best_strat)
print("The highest profit was:", str(round(most_profit)))

appendData(tickers)

#save the results to the json file 
saveresults(results)
print("Results saved to results.json")