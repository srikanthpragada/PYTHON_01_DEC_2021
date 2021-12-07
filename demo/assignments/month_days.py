# Display no. of days in the given month
month = int(input("Enter month :"))
if month == 2:
    # take year and check whether it is leapyear
    year = int(input("Enter year :"))
    if year % 4 == 0:
        print(29)
    else:
        print(28)
elif month in [4, 6, 9, 11]:  # month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(31)
