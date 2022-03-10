###Problem 1###
#last average price
#avg_price1 = 27958 
#first average price
#avg_price2 = 21308 
#number of years between first and last values
#n = 6 

#calculate the compound annual growth rate
#cagr = ((avg_price1 / avg_price2)**(1/n))-1
#change value to percentage then round to 2 decimal places
#percentage_increase = round((cagr * 100), 2)
#print("The average price increased annually by " + str(percentage_increase) + "%")

###Problem 2###
#from numpy import log as ln
#interest rate
#r = 0.05
#future_value = 180000
#present_value = 35000

#number of years
#t = ln((future_value / present_value) / ln(1 + r))
#year = round(t, 2)
#print("It will take about " + str(year) + " years to have enough money to buy the car.")

###Problem 3###
#years
#t = 17
#interest rate
#r = 0.095
#future_value = 650000000

#present_value = (future_value / ((1 + (r/1))**(t)))

#pv = round(present_value, 2)
#print("The present value of this liability is " + str(pv))

###Problem 4###
#interest rate
#r = 0.08
#future_value = 4500000
#years
#t = 73
#present_value = (future_value / ((1 + r)**(t)))
#pv = round(present_value, 2)
#print("Present value = " + str(pv))

###Problem 5###
#interest rate
#r = 0.07
#present_value = 55
#years
#t = 87

#future_value = (present_value * ((1 + r)**(t)))
#fv = round(future_value)
#print("The coins will be worth around $" + str(fv) + " in 2034")

###Problem 6###
###Part a###

#prize money
#prize1 = 120
#prize2 = 1179000
#number of years between first and last prize
#years
#t = 112
#calculate the compound annual growth rate
#cagr = ((prize2 / prize1)**(1/t)) - 1
#percent_value = round((cagr*100), 2)
#print("The prize money increased by " + str(percent_value) + "% per year")

###Part b###
#interest rate
#r = cagr
#years
#t = 33
#present_value = 1179000
#future_value = (present_value * ((1 + r)**(t)))
#fv = round(future_value)
#print("By 2040, the winner's prize money would be about $" + str(fv))

###Problem 7###
#future_value = 10305500
#present_value = 12385500
#years
#t = 4

#interest rate
#r = ((future_value / present_value)**(1/t)) - 1

#annual_rate = round((r *100), 2)
#print("The annual rate of return is " + str(annual_rate) + "%")

###Problem 8###
###Part a###
#interest rate
#r = .1
#years
#t = 35
#present_value = 2000
#future_value = (present_value * ((1 + r)**(t)))
#fv = round(future_value, 2)
#print("My account will be worth $" + str(fv))
###Part b###
#new t after waiting 7 years to contribute
#new_t = 28
#new_future_value = (present_value * ((1 + r)**(new_t)))
#new_fv = round(new_future_value, 2)
#print("My account, after waiting 7 years before contributing, will be worth $" + str(new_fv))

###Problem 9###
#interest rate
#r = 0.05
#years
#t = 8
#present_value = 29000
#future_value = (present_value * ((1 + r)**(t)))
#fv = round(future_value, 2)
#print("I will have $" + str(fv))

###Problem 10###
#from numpy import log as ln
#interest rate
#r = 0.12
#present_value = 8000
#future_value = 95000
#years
#t = ln(future_value/present_value) / ln(1+r)
#new_t = round(t, 2)
#print("I will wait " + str(new_t) +" years from now")