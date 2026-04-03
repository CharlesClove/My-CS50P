import re
Months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    while(True):
        try:
            d_i = input("Date: ).strip()
            
            break
        except ValueError:
            continue
        except (EOFError):
            break
main()
