import pandas as pd
luv = pd.read_excel("/Users/medhaniesolomon/OneDrive - The University of Texas at Dallas/Financial_Report.xlsx", sheet_name=2, header=1)
#replace all NA values with a 0
luv.fillna(0)
#remove the fiscal year columns of 2018 and 2019
luv=luv.drop(columns = ["Dec. 31, 2019", "Dec. 31, 2018"])
#remove all values with 0
luv=luv.drop([0,2,12,23,24,26,27,29,30], axis=0)
Revenue = luv.iloc[0,1]
Operating_Profit = luv.iloc[9,1]
Net_Profit = luv.iloc[17,1]
#income before tax
EBIT = luv.iloc[15,1]
#depreciation and amortization
DA = luv.iloc[6,1]
Interest_Expense = luv.iloc[10,1]
Tax_Provision = luv.iloc[16,1]
Gross_Profit = -2787.00
Gross_Profit_Ratio = Gross_Profit / Revenue
gpr = round(Gross_Profit_Ratio*100, 2)
print("The Gross Profit Ratio is " + str(gpr) + "%")
Operating_Profit_Ratio = Operating_Profit / Revenue
opr = round(Operating_Profit_Ratio*100, 2)
print("The Operating Profit Ratio is " + str(opr) + "%")
Net_Profit_Ratio = Net_Profit / Revenue
npr = round(Net_Profit_Ratio*100, 2)
print("The Net Profit Ratio is " + str(npr) + "%")
Tax_Ratio = Tax_Provision / EBIT
tr = round(Tax_Ratio*100, 2)
print("The Tax Ratio is " + str(tr) + "%")
Interest_Coverage_Ratio = (EBIT + DA)  / Interest_Expense
icr = round(Interest_Coverage_Ratio, 2)
print("The Interest Coverage Ratio is " + str(icr) +"%")