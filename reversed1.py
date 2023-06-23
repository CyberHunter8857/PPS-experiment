def Reverse_Integer(Number):
    Reverse = 0
    while Number > 0:
        Reminder = Number % 10
        Reverse = (Reverse * 10) + Reminder
        Number = Number // 10
    return Reverse

Number = int(input("Enter any number: "))
reversed_number = Reverse_Integer(Number)
print("Reversed Number:", reversed_number)
