def profit(cost,sp):
    profit=sp-cost
    return profit


def inc_profit(cost):
    profit=cost*5/100
    sp=cost+profit
    return sp


cost_price=int(input('enter the cost of product: '))
selling_price=int(input('enter the selling price of product: '))
Profit=profit(cost_price,selling_price)
Selling_Price=inc_profit(cost_price)
print('profit from this sell: ',Profit)
print('selling price of this product if profit is 5% is: ',Selling_Price)


