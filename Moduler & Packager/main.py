from utils import datetime_tools, math_tools, random_tools, uuid_tools, file_tools

def datetime_menu():
    while True:
        print("\n--- DATE & TIME MENU ---")
        print("1. Current Date & Time")
        print("2. Custom Format")
        print("3. Difference Between Dates")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back")
        ch=int(input("Enter choice: "))
        if ch==1:
            print(datetime_tools.current_datetime())
            print("="*25)
        elif ch==2:
            print(datetime_tools.formatted_datetime())
            print("="*25)
        elif ch==3:
            d1=input("Enter first date (DD-MM-YYYY): ")
            d2=input("Enter second date (DD-MM-YYYY): ")
            print("Difference:",datetime_tools.date_difference(d1, d2),"days")
            print("="*25)
        elif ch==4:
            print("Elapsed Time:", datetime_tools.stopwatch(), "seconds")
            print("="*25)
        elif ch==5:
            seconds=int(input("Enter seconds: "))
            datetime_tools.countdown(seconds)
            print("="*25)
        elif ch==6:
            break
        else:
            print("Invalid choice")

def math_menu():
    while True:
        print("\n--- MATH MENU ---")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric shapes")
        print("5. Back")
        ch=int(input("Enter choice: "))
        if ch==1:
            n = int(input("Enter number: "))
            print("Factorial:",math_tools.factorial(n))
            print("="*25)
        elif ch==2:
            p=float(input("Principal: "))
            r=float(input("Rate (%): "))
            t=float(input("Time (years): "))
            print("Amount:",math_tools.compound_interest(p,r,t))
            print("="*25)
        elif ch==3:
            angle=float(input("Enter angle (in radians): "))
            result=math_tools.trigonometry(angle)
            print(result)
            print("="*25)
        elif ch==4:
            print("\n1. Circle\n2. Rectangle")
            opt=int(input("Choose: "))
            if opt==1:
                r=float(input("Radius: "))
                print("Area of circle: ", math_tools.area_circle(r))
            elif opt==2:
                l=float(input("Length: "))
                b=float(input("Breadth: "))
                print("Area of rectangle: ", math_tools.area_rectangle(l, b))
            print("="*25)
        elif ch==5:
            break
        else:
            print("Invalid choice")
        
def random_menu():
    while True:
        print("\n--- RANDOM MENU ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Password")
        print("4. Generate OTP")
        print("5. Random Sampling from Dataset")
        print("6. Game (Dice)")
        print("7. Back")
        ch=int(input("Enter choice:"))
        if ch==1:
            print("Random Number: ",random_tools.random_number())
            print("="*25)
        elif ch==2:
            print("Random List: ",random_tools.random_list())
            print("="*25)
        elif ch==3:
            print("Password: ",random_tools.generate_password())
            print("="*25)
        elif ch==4:
            print("OTP: ",random_tools.generate_otp())
            print("="*25)
        elif ch==5:
            data=input("Enter Data: ")
            print("Sample: ",random_tools.random_sample(data))
            print("="*25)
        elif ch==6:
            print("Dice Number: ",random_tools.dice_game())
            print("="*25)
        elif ch==7:
            break
        else:
            print("Invalid choice")

def file_menu():
    while True:
        print("\n--- FILE MENU ---")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")
        ch=int(input("Enter choice: "))
        if ch==1:
            filename=input("Enter file name: ")
            print(file_tools.create_file(filename))
        elif ch==2:
            filename=input("Enter file name: ")
            data=input("Enter data: ")
            print(file_tools.write_file(filename, data))
        elif ch==3:
            filename=input("Enter file name: ")
            print("Content:", file_tools.read_file(filename))
        elif ch==4:
            filename=input("Enter file name: ")
            data=input("Enter data: ")
            print(file_tools.append_file(filename, data))
        elif ch==5:
            break
        else:
            print("Invalid choice")

def main():
    while True:
        print("\n===== MULTI-UTILITY TOOLKIT =====")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice=int(input("Enter your choice: "))

        if choice==1:
            datetime_menu()
        elif choice==2:
            math_menu()
        elif choice==3:
            random_menu()
        elif choice==4:
            print("\n--- GENERATE UNIQUE IDENTIFIERS ---")
            print("Generated UUID:",uuid_tools.generate_uuid())
            print("="*25)
        elif choice==5:
            file_menu()
        elif choice==6:
            mod = input("Enter module name: ")
            try:
                print(dir(eval(mod)))
            except:
                print("Invalid module")
            print("="*25)
        elif choice==7:
            print("-"*25+"\n"+"Thank you for using Multi-Utility Toolkit"+"\n"+"-"*25)
            break
        else:
            print("Invalid option chosen. Please choose again.")

if __name__ == "__main__":
    main()