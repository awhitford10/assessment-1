
def optimal_change(cost,payment):
    bill_amount =[100.0,50.0,20.0,10.0,5.0,1.0,0.25,0.10,0.05,0.01]
    bills = ['$100 bill','$50 bill','$20 bill','$10 bill','$5 bill','$1 bill','quarter','dime','nickle','penny']
    bills_plural = ['$100 bills','$50 bills','$20 bills','$10 bills','$5 bills','$1 bills','quarters','dimes','nickles','pennies']
    bill_count = [0,0,0,0,0,0,0,0,0,0]
    output = [f"The optimal change for an item that costs ${cost} with an amount paid of ${payment} is "]
    
    if not((type(cost)==float or type(cost)==int) and (type(payment)==float or type(payment)==int)):
        return ('Invalid inputs: inputs must be numeric.')
    elif payment < cost:
        return(f'The payment was not enough. The amount still owed is ${cost-payment}')
    elif payment == cost:
        return('You payed the perfect amount. No changed will be dispensed. You make my job easy. I love you!')
    else:
        change = payment - cost
        for x in range(0,10):
            while round(change - bill_amount[x],2) >= 0.00:
                bill_count[x] += 1
                change -= bill_amount[x]
            if bill_count[x] == 1:
                output.append(f'{bill_count[x]} {bills[x]}, ')
            elif bill_count[x] > 1:
                output.append(f'{bill_count[x]} {bills_plural[x]}, ')
    if len(output) > 2:
        output[-1] = 'and '+ output[-1]

    return "".join(output).rstrip(', ')+'.'


