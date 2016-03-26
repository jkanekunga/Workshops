print('Electricity bill estimator 2.0')

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_condition = int(input('Please choose your tariff. Enter 1 for Tariff 11 or 2 for tariff 31:'))

if 1 > tariff_condition or tariff_condition > 2:
        print('Wrong number!')
else:
        daily_use_kWh = float(input('Enter daily use in kWh: '))
        no_of_bill_days = float(input('Enter number of billing days: '))

        if tariff_condition == 1:
            cent_per_kWh = TARIFF_11
        elif tariff_condition == 2:
            cent_per_kWh = TARIFF_31

        bill = cent_per_kWh * daily_use_kWh * no_of_bill_days
        print('Estimated bill: $',bill)




