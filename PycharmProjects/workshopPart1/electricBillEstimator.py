print('Electricity bill estimator')

cent_per_kWh = float(input('Enter cents per kWh: '))
daily_use_kWh = float(input('Enter daily use in kWh: '))
no_of_bill_days = float(input('Enter number of billing days: '))

bill = cent_per_kWh * daily_use_kWh * no_of_bill_days

print('Estimated bill: $',bill/100)
