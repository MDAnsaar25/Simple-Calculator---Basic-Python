#simple calculator
print("Welcome to the Simple Calculator")
number1 = int(input("Enter your First number: "))
number2 = int(input("Enter your Second number: "))
result = 0
print("Choose your choices here: Add, Sub, Mul, Div")
operation=input("Enter your Choice:  ")
if(operation == "Add"):
  result = number1+number2
  print("The addition of the number given is", result)
elif(operation == "Sub"):
  result = number1-number2
  print("The subraction of the number given is", result)
elif(operation == "Mul"):
  result = number1*number2
  print("The multiplication of the number given is", result)
elif(operation=="Div"):
  result= number1/number2
  print("The division of the number given is", result)
else:
  print("Enter the correct operation to perform the Arithmetic Calculation")

  