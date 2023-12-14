
vac_site = input("Vaccination site? ")

# Create tuples to store the values of the type, qty and cost of vaccination
vaccine_type = []
vaccine_qty = []
vaccine_cost = []

cost = 0

# ask for input until the user gives an empty value
while True:

    vac_type = input("Vaccine type? ")
    if vac_type == '':
        break

    qty = int(input("Number of vaccines requested? "))
    fee = float(input("Shipping fee per 100 doses? "))

    # Make sure the shipping fee is charged for a batch of 100
    if qty % 100 == 0:
        cost = (qty / 100) * fee
    else:
        vac_number = (int(qty / 100) + 1) * 100
        cost = (vac_number / 100) * fee

    # add values to respective tuples
    vaccine_type.append(vac_type)
    vaccine_qty.append(qty)
    vaccine_cost.append(cost)

# Ask for cash paid
cash_paid = float(input("Cash paid? "))

total = float(sum(vaccine_cost))
cost_without_vat = total * (5 / 6)
the_vat = cost_without_vat * (20 / 100)

# Calculate change
change = cash_paid - total

# format the numerical values to always print two digits after the decimal
the_vat = format(the_vat, '.2f')
total = format(total, '.2f')
cash_paid = format(cash_paid, '.2f')
change = format(change, '.2f')



# Print Heading
print('VACCINES2U'.ljust(19), 'SHIPPING ORDER'.rjust(20))
print('VAT GB123456789'.ljust(19), vac_site.upper().rjust(20))

print()

# Print item heading
print('Vaccine'.ljust(25) + 'Qty.'.center(5) + 'Cost'.rjust(10))

# Print vaccination types and their respective quantity and cost
for i in range(len(vaccine_type)):
    the_type = vaccine_type[i].upper()
    the_qty = str(int(vaccine_qty[i]))
    the_cost = format(vaccine_cost[i], '.2f')
    print(the_type.ljust(25) + the_qty.center(5) + the_cost.rjust(10))

print()

# Print total, vat and change
print('TOTAL'.ljust(30) + total.rjust(10))
print('VAT INCLUDED IN TOTAL'.ljust(30) + the_vat.rjust(10))
print('CASH PAID'.ljust(30) + cash_paid.rjust(10))
print('CHANGE'.ljust(30) + change.rjust(10))

