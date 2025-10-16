HouroftheDay = int(input("Enter the Hour of the Day(0-23): "))

if 5 <= HouroftheDay < 12:
    print("Good Morning!")
elif 12 <= HouroftheDay < 17:
    print("Good Afternoon!")
elif 17 <= HouroftheDay < 20:
    print("Good Evening!")
elif (20 <= HouroftheDay <= 23) or (0 <= HouroftheDay < 5):
    print("Good Night!")
else:
    print("Invalid hour. Please enter a number between 0 and 23.")
