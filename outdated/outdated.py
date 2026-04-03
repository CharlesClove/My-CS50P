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
            date_input = re.split(', | |/',input("Date: ")) #using regex I split both dates that use slash spaces, etc
            #January, 8, 1999 or 1/9/1999
            if len(date_input) != 3:
                print("wrong format")
                raise ValueError
            if 

        except ValueError:
            continue
        except (EOFError):
            break

main()
