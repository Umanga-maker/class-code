var = '0'
while var.isnumeric() == True:
    var = input("Enter a number: ")
    if var == "10":
        break
    elif var.isnumeric() == True:
        print ("Your input", var)
        

print ("End of while loop")
