###Problem 1###
#coupon payment
#c = 1000 * .09
#time in years
#t = 14
# current price
#p = 850.46
#face value
#par = 1000

#yield to maturity
#ytm = (c + ((par - p) / t)) / ((par + p) / 2)

###Problem 2###
#time in years
#t = 6
#current price
#p = 970
#yield to maturity
#ytm = .099
#face value
#par = 1000

#coupon rate
#c = (ytm * ((par + p) / 2)) - ((par - p) / t)

###Problem 3###
#time in year
#t = (19-2) * 2
#face value
#par = 1000
#current price
#p = 1020
#coupon rate
#c = (1000 * .094) / 2

#yield to maturity
#ytm = (c + ((par - p) / t)) / ((par + p) / 2)

###Problem 4###
#real rate
#real = .055
#inflation rate
#inflation = .02

#treasury bill rate
#t_bill = ((1 + real) * (1 + inflation)) - 1

###Problem 5###
#total rate
#total = .095
#inflation rate
#inflation = .05

#real rate of return
#rrr = ((1 + total) / (1 + inflation)) - 1

###Problem 6###
###Part a###
#time in years
#t = 7 * 2
#coupon rate
#c_j = (1000 * .05) / 2
#yield to maturity
#ytm = .07 / 2
#face value
#par = 1000

#current price
#p_j = c_j * ((1 - (1 + ytm) ** -t) / ytm) + (par / (1 + ytm) ** t)

#interest rate rises by 2%
#ytm_ja = .09 / 2
#new price
#p_ja = c_j * ((1 - (1 + ytm_ja) ** -t) / ytm_ja) + (par / (1 + ytm_ja) ** t)

#percent price change of bond j
#percent_change_ja = (p_ja - p_j) / p_j

###Part b###
#coupon rate
#c_k = (1000 * .11) / 2
#yield to maturity
#ytm_k = .11 / 2
#interest rate rises by 2%
#ytm_kb = .13 / 2

#price
#p_k = c_j * ((1 - (1 + ytm_k) ** -t) / ytm_k) + (par / (1 + ytm_k) ** t)

#new price
#p_kb = c_j * ((1 - (1 + ytm_kb) ** -t) / ytm_kb) + (par / (1 + ytm_kb) ** t)

#percent price change of bond k
#percent_change_kb = (p_kb - p_k) / p_k
###Part c###
#interest rate drops by 2%
#ytm_jc = .05 / 2

#new price
#p_jc = c_j * ((1 - (1 + ytm_jc) ** -t) / ytm_jc) + (par / (1 + ytm_jc) ** t)
#percent price change of bond j
#percent_change_jc = (p_jc - p_j) / p_j
###Part d###
#interest rate drops by 2%
#ytm_kd = .09 / 2

#new price
#p_kd = c_j * ((1 - (1 + ytm_kd) ** -t) / ytm_kd) + (par / (1 + ytm_kd) ** t)
#percent price change of bond k
#percent_change_kd = (p_kd - p_k) / p_k

###Problem 7###
#price
#p = 1013.04
#time
#t = 11 * 2
#face value
#par = 1000
#coupon rate
#i = .104

#coupon price
#c = i * par / 2

#yield to maturity
#ytm = (c + ((par - p) / t)) / ((par + p) / 2)

###Problem 8###
#clean price
#clean_price = 1180
#accrued_interest
#accrued_interest = ((1000*.076) / 2) * (4/6)
#invoice price
#dirty_price = accrued_interest + clean_price

###Problem 9###
#cash flow
#cf = 5 * 52
#interest rate
#r = .114
#growth rate
#g = .036
#time
#t = 32
#present value
#pv = cf / (r - g) * (1 - ((1+g) / (1+r))**t)

###Problem 1###
#growth rate
#g = .06
#dividend
#d = 1.32
#return
#r =.1
#dividend in 10 years
#d10 = d*(1+g)**10
#current price
#p = d / (r - g)
#price in 10 years
#p10 = d10 / (r - g)

###Problem 2###
#dividend
#d = 4.55
#growth rate
#g = .03
#stock price
#p = 40
#return
#r = (d * (1+g) / p) + g

###Problem 3###
#dividend
#d = 4.90
#growth rate
#g = .043
#return
#r = .079
#stock price
#p = (d * (1 + g)) / (r - g)

###Problem 4###
#stock price
#p = 90
#return
#r = .1
#dividend next year
#d1 = p * r
#current dividend
#d0 = d1 / (1 + r)

###Problem 5###
#dividend
#d = 25
#time in years
#t = 7
#return
#r = .1
#current price
#p = d * (1 - (1+r) ** -t) / r

###Problem 6###
#dividend
#d = 1.40
#growth
#g = .06
#time in years
#t = 1
#return red inc.
#r1 = .089
#return yellow corp.
#r2 = .119
#return blue
#r3 = .153
###Part a###
#stock price for red inc.
#p1 = (d * (1 + g)) / (r1 - g)
###Part b###
#stock price for yellow corp.
#p2 = (d * (1 + g)) / (r2 - g)
###Part c###
#stock price for blue
#p3 = (d * (1 + g)) / (r3 - g)

###Problem 7###
#dividend
#d = 11
#return
#r = .12
#growth
#g = .04
#time in years
#t = 15
#current price
#p = (d / (r - g)) / ((1 + r)**t)

###Problem 8###
#dividend
#d1 = 13
#d2 = 11
#d3 = 9
#d4 = 5
#growth
#g = .08
#return
#r = .17

#current price
#p = (d1/(1+r)) + (d2/(1+r)**2) + (d3/(1+r)**3) + (d4/(1+r)**4) + ((d4 * (1+g))/(r-g)) * (1 / (1+r)**4)

###Problem 9###
#dividend
d = 1.60
#growth rate
g = .18
#fall rate
f = .04
#required return
r = .07
#time in years
t = 3

#current price
p1 = (d * ((1 + g) ** t) * (1 + f)) / (r - f)
p0 = ((d * (1 + g)) / (1 + r)) + ((d * (1 + g)**2) / (1 + r)**2) + ((d * (1 + g)**3) / (1 + r)**3) + p1 / ((1+r)**t) + p1 / ((1+r)**t)

