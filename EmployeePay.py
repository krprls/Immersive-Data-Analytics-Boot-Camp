#Programme for employee pay

# function to caliculate the pay rate

def emplpay(payRate, hoursWorked):
    if hoursWorked > 40:
        pay40 = payRate * 40
        extraPay = (1.5 * payRate) * (hoursWorked - 40)
        totalpay = pay40 + extraPay
    else:
        totalPay = payRate * hoursWorked
        
    return totalPay

#program for excute 

name = input("please enter your name: ")
print(name)

ID = input("Please enter your ID: ")
print(ID)

hoursWorked = input("hoursWorked: ")
print(hoursWorked)

payRate = input("payRate: ")
print(payRate)

totalpay = emplpay(float(payRate), int(hoursWorked))

print('your name: ' + name + 'ID#' + ID + 'pay' + str(totalpay))







