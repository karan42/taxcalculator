def individual(income, age=0):
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
    if 50*10**6 < income < 10**7:
        surcharge = tax * 0.1
    elif income > 10**7:
        surcharge = tax * 0.15
    else:
        surcharge = 0
    cess = (tax + surcharge) * 0.04
    totaltax = tax + cess + surcharge
    return totaltax


def corporate(income, turnover=0):
    if turnover < 250*10**7:
        tax = income * 0.25
    else:
        tax = income * 0.29
    if 10**7 < income < 10**8:
        surcharge = tax * 0.07
    elif income > 10**8:
        surcharge = tax * 0.12
    else:
        surcharge = 0
    cess = (tax + surcharge) * 0.04
    totaltax = tax + surcharge + cess
    return totaltax


def foreignco(income):
    tax = income * 0.4
    if 10**7 < income > 10**8:
        surcharge = tax * 0.02
    elif income > 10**8:
        surcharge = tax * 0.05
    else:
        surcharge = 0
    cess = (tax + surcharge) * 0.04
    totaltax = tax + surcharge + cess
    return totaltax
