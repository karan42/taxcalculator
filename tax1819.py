def individual(income, age):
    if income < 2.5*10**5:
        return 0
    elif income < 5*10**5:
        if age < 60:
            tax = (income - 2.5*10**5) * 0.05
        elif 60 > age < 80:
            tax = (income - 3*10**5) * 0.05
    elif income < 10**6:
        if age < 80:
            tax = 12500 + (income - 5*10**5) * 0.2
        else:
            tax = (income - 5*10**5) * 0.2
    else:
        tax = 112500 + (income - 10**6) * 0.3
    cess = tax * 0.04
    if 50*10**6 < income < 10**7:
        surcharge = (tax + cess) * 0.1
    elif income > 10**7:
        surcharge = (tax + cess) * 0.15
    else:
        surcharge = 0
    totaltax = tax + cess + surcharge
    return totaltax
