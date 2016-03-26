# calculate and impose discount on shipping item

while True:
    items = int(input('Enter number of items:'))

    if items <= 0:
        print('Invalid number of Items')
    else:
        cost_per_item = float(input('Enter shipping cost per item: $'))

        total_shipping_cost = items * cost_per_item

        if total_shipping_cost > 100:
            #calculate 10% discount
            discount_amount = total_shipping_cost * (10/100)
            total_shipping_cost = (total_shipping_cost - discount_amount)

            print('10% discount shipping cost is: $', total_shipping_cost, sep='')

        else:
            print('Total shipping cost is: $', total_shipping_cost, sep='')








