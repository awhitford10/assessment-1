
def optimal_change(cost,payment):
    bill_amount =[100.0,50.0,20.0,10.0,5.0,1.0,0.25,0.10,0.05,0.01] #hold values all in float
    bills = ['$100 bill','$50 bill','$20 bill','$10 bill','$5 bill','$1 bill','quarter','dime','nickle','penny'] #names if singlular
    bills_plural = ['$100 bills','$50 bills','$20 bills','$10 bills','$5 bills','$1 bills','quarters','dimes','nickles','pennies']#plural name
    bill_count = [0,0,0,0,0,0,0,0,0,0]          #holder for number of bills in change
    output = [f"The optimal change for an item that costs ${cost} with an amount paid of ${payment} is "] #beggining statement of output
    
    if not((type(cost)==float or type(cost)==int) and (type(payment)==float or type(payment)==int)):
        return ('Invalid inputs: inputs must be numeric.')  #catch any input that is not int or float
    elif payment < cost:    #catch cost higher than payment
        return(f'The payment was not enough. The amount still owed is ${round(cost-payment,2)}.')
    elif payment == cost:   #cath exact change
        return('You payed the perfect amount. No changed will be dispensed. You make my job easy. I love you!')
    else:       #only other input both numeric where payment > cost
        change = payment - cost     #how much left for change
        for x in range(0,10):       #count through lists (bill_amount,bills,bills_plural) all same length
            while round(change - bill_amount[x],2) >= 0.00: #continues with highest bill untill bill is more than whats left
                bill_count[x] += 1
                change -= bill_amount[x]
            if bill_count[x] == 1:          #append singular case to output
                output.append(f'{bill_count[x]} {bills[x]}, ')
            elif bill_count[x] > 1:         #append plural case to output
                output.append(f'{bill_count[x]} {bills_plural[x]}, ')
    if len(output) > 2:
        output[-1] = 'and '+ output[-1] #if more than single denomination give, input 'and'

    return "".join(output).rstrip(', ')+'.' #join output, remove trailing comma and space, insert ending period


