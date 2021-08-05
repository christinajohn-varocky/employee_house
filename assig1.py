# salary=80000
# total_cost=500000
# portion_saved=.15

annual_salary=int(input('Enter your annual salary:'))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=int(input("Enter the cost of your dream home:"))


def time_for_downpayment(annual_salary,portion_saved,total_cost):
    current_saving=0
    r=.04
    month=0
    portion_down_payment = total_cost*.25
    while current_saving <= portion_down_payment:
        portion=(annual_salary/12)*portion_saved
        current_saving+=(current_saving*.04/12)+portion
        month+=1
    return month
    
print("no of months :",time_for_downpayment(annual_salary,portion_saved,total_cost))