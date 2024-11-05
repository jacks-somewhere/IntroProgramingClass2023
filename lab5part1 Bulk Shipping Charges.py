
# Lab 5
# Bulk Shipping Charges

# Program is for finding out how much a customer would be charged for shipping
# a package based on the information that they provide

#Variables
# Shipping Type
NEXT = 'Next Day'
TWO_DAY = '2-Day'
# Weight Based Cost for Next Day Delivery (in pounds)
NEXT_UNDER_5 = 10.50
NEXT_5_TO_20 = 16
NEXT_20_TO_50 = 24
NEXT_OVER_50 = 30.50
# Weight Based Cost for 2-Day Delivery (in pounds)
TWO_UNDER_5 = 6.75
TW0_5_TO_20 = 9.50
TWO_20_TO_50 = 18.50
TWO_OVER_50 = 23
#Per Mile Shipping Fees (cents)
NEXT_MILE = .06
TWO_MILE = .04

# Prompts User to Enter Shipping Information
shipping_type = input('What method of shipping are you using, Next Day or 2-Day? ')
weight = float(input('How much does you package weigh in pounds? '))
miles = int(input('How many miles is it being shipped? '))

# ifs for Next Day shippinge
if shipping_type == NEXT:
    if weight <= 5:
        base_rate = NEXT_UNDER_5
        miles_cost = miles * NEXT_MILE
        total = base_rate + miles_cost
    else:
        if weight > 5 and weight <= 20:
            base_rate = NEXT_5_TO_20
            miles_cost = miles * NEXT_MILE
            total = base_rate + miles_cost
        else:
            if weight > 20 and weight <= 50:
                base_rate = NEXT_20_TO_50
                miles_cost = miles * NEXT_MILE
                total = base_rate + miles_cost
            else:
                if shipping_type == NEXT and weight > 50:
                    base_rate = NEXT_OVER_50
                    miles_cost = miles * NEXT_MILE
                    total = base_rate + miles_cost

# ifs for 2-Day shipping
if shipping_type == TWO_DAY:
    if weight <=5:
        base_rate = TWO_UNDER_5
        miles_cost = miles * TWO_MILE
        total = base_rate + miles_cost
    else:
        if weight > 5 and weight <= 20:
            base_rate = TW0_5_TO_20
            miles_cost = miles * TWO_MILE
            total = base_rate + miles_cost
        else:
            if weight > 20 and weight <= 50:
                base_rate = TWO_20_TO_50
                miles_cost = miles * TWO_MILE
                total = base_rate + miles_cost
            else:
                if weight > 50:
                    base_rate = TWO_OVER_50
                    miles_cost = miles * TWO_MILE
                    total = base_rate + miles_cost

# Final output for for user based on above ifs
print(f'Your package weighing {weight} pounds shipping {shipping_type} will cost:')
print(f'Base rate:  ${base_rate:.2f}')
print(f'Milage:     ${miles_cost:.2f}')
print(f'Total Cost: ${total:.2f}')


