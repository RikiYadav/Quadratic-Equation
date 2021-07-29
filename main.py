from time import *

wakt = localtime()

day = int(input("Enter the Day : "))
month = int(input("Enter the Month : "))
year = int(input("Enter the Year: "))


def agecalc(day, month, year):
    def ageformula():
        y = abs(wakt.tm_year - year)
        m = abs(wakt.tm_mon - month)
        d = abs(wakt.tm_mday - day)
        td = (y * 365) + (m * 30) + d
        tm = (td * 1440)
        ts = (tm * 60)
        print(
            f'Your age is \n{y} years\n{m} month\n{d} days\nAnd '
            f'you are of\n{td} days\n{tm} minutes\n{ts} seconds ')

    ageformula()


agecalc(day, month, year)
