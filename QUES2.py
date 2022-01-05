#TO CALCULATE TAX
tax_rate=20#percent
standard_deduction=10000
add_deduction=3000
gross_income = input("GROSS INCOME = ")
No_of_dependents=input("NUMBER OF DEPENDENTS = ")
taxable_income = float(gross_income) - standard_deduction - (int(No_of_dependents) * add_deduction)
tax_to_pay=(float(taxable_income)*tax_rate)/100
print(tax_to_pay)
