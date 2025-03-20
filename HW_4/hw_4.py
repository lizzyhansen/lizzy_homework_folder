
# list comp: this line of code reads in my TSLA file and converts each string value to a float 
prices = [round(float(line),2) for line in reversed(open("lizzy_homework_folder/HW_4/TSLA.txt").readlines())]

# print(prices)

# need to find find five day moving average 
#five day average calculation shoul start on day 6 (so that will be index 5 of my prices list)
# so if i'm iterating through my list, I should start the calculations on iteration 5
# need to check that if we already have a stock we aren't buying another 
# need to check that we have a stock before we try to sell

# need to loop through prices list and do... something

i = 0 # indexing value to keep track 
buy = 0
trade_profit = 0 
first_buy = 'True'
total_profit = 0

for price in prices:
    if i >= 5:


        current_price = price #the next price in the list

        average = (prices[i-1] + prices[i-2] + prices[i-3]+ prices[i-4] + prices[i-5])/5 #average price for the 5 previous days
        # print("average:",average)


        if current_price < average * 0.98 and buy == 0:
            buy = current_price
            print("buying at:", price)



           #update first_buy variable if this is the first time you buy
        elif current_price > average * 1.02 and buy !=0:
            #calculate trade profit (how much money did I make)
            print("selling at:", current_price)
            trade_profit += current_price - buy
            print("trade profit:",round( current_price - buy,2))
            buy = 0 

        else:
            pass

    i += 1

# calculte first_buy 

first_buy = prices[6]
print("first_buy",first_buy)
      

# CALCULATE total profit
  
total_profit += float(round(trade_profit, 2))
print("Total_profit", total_profit)

#calculate % return 
final_profit_percentage = ( total_profit / first_buy ) * 100
print("% return", round(final_profit_percentage, 2))





































