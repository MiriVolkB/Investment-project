
base_investment = 7000
increase = 1.02
inflation = 1.02
payments = 12
appreteation = 1.08
lose = 0.999
sum = 0
bulk = 0
growth = 0
YEARS = 20
tax_persent = 0.25


for year in range(1, YEARS + 1):
    if year==1:
            monthly_investment = base_investment
    else:
        monthly_investment = monthly_investment * increase
    growth = monthly_investment * payments

    sum =  ((growth + sum) * appreteation ) * lose

    if year==1:
            total_investment = growth  + bulk * inflation
    else:
       total_investment = (total_investment + growth) * inflation
    gane = sum - total_investment
    tax = tax_persent * gane

    print(f"years total gane: {sum:,.2f} for year: {year}")

print(f"\nTotal after {YEARS} years: {sum:,.2f}")
sum = sum - tax
print(f"Tax after {YEARS} years: {tax:,.2f}")
print(f"Total invested money after {YEARS} years: {total_investment:,.2f}")
print(f"Total ganed money after {YEARS} years: {gane:,.2f}")
print(f"Total after tax after {YEARS} years: {sum:,.2f}\n")



