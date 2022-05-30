# Write a program to prompt the user for hours and rate per hour using
# input to compute gross pay. Pay the hourly rate for the hours up to 40 and
# 1.5 times the hourly rate for all hours worked above 40 hours.

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h > 40:
    extra = h - 40
    bonus_rate = r * 1.5
    pay =  (40 * r) + (extra * bonus_rate)
    print(pay)
