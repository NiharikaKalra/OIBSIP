while True: 
    try:
        # Taking height and weight from user
        H = float(input("Enter your height in m:"))
        W = float(input("Enter your weight in kg:"))
        
        #Input validation : Input reject and give error message when user give negative values
        if H <= 0 or W <= 0:
            print("Fill heigth and weight is always greater than zero")
            print("oops! their is an error\n Try again")
            
            # restart the loop and ask for input 
            continue 
        else:
            # calculating the height and weight of user
            BMI = round(W / (H * H), 2)
            print(f'Body Mass Index is : {BMI}')
            
            # accoring to user input describing which category user height and weight belong to .
            if BMI < 18.5:
                print("underweight")
            elif BMI < 24.9:
                print("normal weight")
            elif BMI < 29:
                print("overweight")
            else:
                print("obses")
            # exit if program run succesfully!
            break 

    except ValueError:
        # Input validation : Give error message if user gives input data in alphabet(non - numeric value).
        print("Fill height and weight always in numbers not in alphabet")
        print("oops!there is an error\n Try again")
        
        