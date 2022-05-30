# Write a program to prompt the user for hours and rate per hour using input to compute gross
#  pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly
# rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a
# function called computepay() and use the function to do the computation. The function should
# return a value.
def computepay(h, r):
    if h > 40:
        extra = h - 40
        bonus_rate = r * 1.5
        pay = (40 * r) + (extra * bonus_rate)
        return pay
    return h * r


hrs = input("Enter Hours:")
rates = input("Enter Rate:")
p = computepay(float(hrs), float(rates))
print("Pay", p)
