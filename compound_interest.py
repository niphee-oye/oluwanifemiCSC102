p= int(input("Enter starting principal please"))
n= int(input("Enter number of compounding periods per year"))
r= float(input("Enter annual rate. e.g 15 for 15%"))
y= int(input("Enter amount of years."))

FV = p * (((1 + ((r/100.0)/n)) ** (n*y)))

print("The final amount after ", y, "years is", FV)