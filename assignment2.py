###Problem 1###
#present value
#PVA = 31000
#interest rate
#r=.0625
#time in years
#t=14

#annual cash flow
#C = (PVA * r) / (1 - (1 / (1 + r)**t))

###Problem 2###

###Problem 3###
#triple money in 72 months
#present value
#PV = 1000
#time in years
#t = 6
#future value
#FV = 3000

#annual rate of return
#r = (((FV/PV)**(1/t)) - 1) * 100

#quarteryly rate of return
#quarter_r = r / 4

###Problem 4###
#initial payment
#C = 540000
#time in years
#t=16
#growth rate
#g=0.05
#discount rate
#r = 0.1

#PV = ((C / (r - g)) * (1 - (((1 + r) / (1 + g))**t)))

#from numpy import log as ln
###Problem 5###
#monthly payments
#P = 380
#future value
#FV = 25694
#interest rate
#r = 0.08

#number of payments
#t = ln(1 + (FV / P) * (r / 12)) / ln(1 + (r / 12))

###Problem 6###
# #monthly payments
#monthly = 800

#APR
#a = 0.076

#time in months
#t = 360

#principal
#p = 230000

#present value annual
#PVA = monthly * ((1 - (1 / (1+(a / 12)) ** t)) / (a / 12))

#remaining principal due
#x = p - PVA

#balloon_payment = x * ((1 + (a / 12)) ** t)

###Problem 7###
#import numpy  as np
###Part a###
#monthly payment
#PMT = 17000
#time in months
#t = 360
#present value
#PV = 2800000 * (.8)
#interest rate
#r= ((PMT / PV) - 1) * (math.exp((1/(t+1))))

#ad = np.mirr(pv=PV, nper = t, pmt = PMT)
#print(ad)

###Problem 8###
#monthly payments
#PMT = 1700
#interest rate for first 6 years
#r= .13
#time in months
#t=72
#interest rate for the next 10 years
#i=.1
#time in months
#tt=120
#present value for first 6 years
#PV1 = PMT * (1 - (1 / (1+(r/12))**t))/(r/12)
#present value for remaining 10 years
#PV2 = PMT * (1 - (1 / (1+(i/12))**tt))/(i/12)
#present value of cash flow today
#P = PV2 / ((1 + (r/12))**t)
#present value
#PV = P + PV1

###Problem 9###
#present value
#PV = 43000
#time in months
#t = 60
#interest rate
#r = .0825
#monthly payment
#PMT = (PV / (1+r/12)) / ((1 - (1 / (1+(r/12))**t))/(r/12))

###Problem 10###
#future value of loan repayment amount
#FV = 5000 * (1.1)
#present value of amount received
#PV = 5000 * (1 - .03)
#interest rate you will pay
#r = (FV / PV) - 1

import pandas as pd

luv=pd.read_excel("/Users/medhaniesolomon/OneDrive - The University of Texas at Dallas/Financial_Report.xlsx", sheet_name=2, header=1, na_filter=False)
#print(luv.head())

#gross profit from 2018-2020
gross_profit_20 = -7596
gross_profit_19 = 10389
gross_profit_18 = 10051

#revenue from 2018-2020
revenue_20 = luv.iloc[1,1]
revenue_19 = luv.iloc[1,2]
revenue_18 = luv.iloc[1,3]

#operating profit from 2018-2020
operating_profit_20 = luv.iloc[11,1]
operating_profit_19 = luv.iloc[11,2]
operating_profit_18 = luv.iloc[11,3]

#net profit from 2018-2020
net_profit_20 = luv.iloc[20,1]
net_profit_19 = luv.iloc[20,2]
net_profit_18 = luv.iloc[20,3]

#earnings before income tax from 2018-2020
EBIT_20 = luv.iloc[18,1]
EBIT_19 = luv.iloc[18,2]
EBIT_18 = luv.iloc[18,3]

#depreciation and amortization from 2018-2020
DA_20 = luv.iloc[8,1]
DA_19 = luv.iloc[8,2]
DA_18 = luv.iloc[8,3]

#interest expense from 2018-2020
interest_expense_20 = luv.iloc[13,1]
interest_expense_19 = luv.iloc[13,2]
interest_expense_18 = luv.iloc[13,3]

#tax provision from 2018-2020
tax_provision_20 = luv.iloc[19,1]
tax_provision_19 = luv.iloc[19,2]
tax_provision_18 = luv.iloc[19,3]

#gross profit ratio from 2018-2020
gross_profit_ratio_20 = gross_profit_20 / revenue_20
gross_profit_ratio_19 = gross_profit_19 / revenue_19
gross_profit_ratio_18 = gross_profit_18 / revenue_18

#operating profit ratio from 2018-2020
operating_profit_ratio_20 = operating_profit_20 / revenue_20
operating_profit_ratio_19 = operating_profit_19 / revenue_19
operating_profit_ratio_18 = operating_profit_18 / revenue_18

#net profit ratio from 2018-2020
net_profit_ratio_20 = net_profit_20 / revenue_20
net_profit_ratio_19 = net_profit_19 / revenue_19
net_profit_ratio_18 = net_profit_18 / revenue_18

#tax ratio from 2018-2020
tax_ratio_20 = tax_provision_20 / EBIT_20
tax_ratio_19 = tax_provision_19 / EBIT_19
tax_ratio_18 = tax_provision_18 / EBIT_18

#interest coverage ratio from 2018-2020
interest_coverage_ratio_20 = (EBIT_20 / DA_20) / interest_expense_20
interest_coverage_ratio_19 = (EBIT_19 / DA_19) / interest_expense_19
interest_coverage_ratio_18 = (EBIT_18 / DA_18) / interest_expense_18

#percent change in gross profit from 2018 to 2020
percent_change_gross_profit_ratio = ((gross_profit_ratio_20 - gross_profit_ratio_18) / gross_profit_ratio_18) * 100

#percent change in operating proft from 2018 to 2020
percent_change_operating_profit_ratio = ((operating_profit_ratio_20 - operating_profit_ratio_18) / operating_profit_ratio_18) * 100

#percent change in net profit from 2018 to 2020
percent_change_net_profit_ratio = ((net_profit_ratio_20 - net_profit_ratio_18) / net_profit_ratio_18) * 100

#percent change in tax ratio from 2018 to 2020
percent_change_tax_ratio = ((tax_ratio_20 - tax_ratio_18) / tax_ratio_18) * 100

#percent change in interest coverage ratio from 2018 to 2020
percent_change_interest_coverage_ratio = ((interest_coverage_ratio_20 - interest_coverage_ratio_18) / interest_coverage_ratio_18) * 100

#monthly payment
monthly = 1200
#present value
pv = 61000
#perpetuity yield
#r = monthly / pv
#effective annual rate
#ear = ((1 +(r / 12)) ** 12) - 1



###problem 7
#present value
pv = 2800000 * (.8)
#monthly payments
month = 17000
#time in months
t=12*30

r = (1 - ((1+r)**t)) / (pv/month)

ear = ((1+r)**12) - 1