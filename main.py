import re
from package import taxCalculation
#Inputs
#Annuall Income Before Tax in $CAD
annualIncome=50000
#Provinces to be chosen from:
# Alberta
# British Columbia
# Manitoba
# New Brunswick
# Newfoundland and Labrador
# Northwest Territories
# Nova Scotia
# Nunavut
# Ontario
# Prince Edward Island
# Quebec
# Saskatchewan
# Yukon

location="Quebec"
afterTaxIncome=taxCalculation.calculateAfterTaxIncome(annualIncome,location)
#Return after tax income
print(afterTaxIncome)
#return afterTaxIncome
