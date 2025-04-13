year, month, day = map(int, input().split())
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_of_month[1] = 29
total_days = sum(days_of_month[:month - 1]) + day
print(total_days)