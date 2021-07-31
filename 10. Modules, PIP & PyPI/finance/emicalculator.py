from interest import simple_interest

def calculate_emi(Principal,Rate,No_of_Payments):
    years=No_of_Payments/12
    interest=simple_interest(Principal, years, Rate)
    totalAmount=Principal+interest
    return totalAmount/No_of_Payments

def calculate_downpayment(TotalValue,No_of_Payments,Rate,desired_payment):
    years=No_of_Payments/12
    totalinterest=simple_interest(TotalValue, years, Rate)
    LoanValue=calculate_emi(TotalValue, Rate, No_of_Payments) * No_of_Payments
    totalpayments=desired_payment*No_of_Payments
    return LoanValue-totalpayments

