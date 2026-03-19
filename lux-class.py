%load_ext line_profiler

%lprun -f check_driving_license check_driving_license()

age = int(input("Enter your age: "))

if age >= 22:
    print("You are eligible to apply for a driving license.")
elif age >= 35:
    print("You are eligible to apply for a driving license and you can also apply for a commercial driving license.")
else:
    print("You are not eligible to apply for a driving license yet. Please wait until you are 22 years old.")