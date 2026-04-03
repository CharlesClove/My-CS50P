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
            #January, 8, 1999 or 1/9/1999 logic for string month, logic for 2 and 3 postition to be a int
            if len(date_input) != 3:
                raise ValueError

            if date_input[0] in Months:
                word_to_number_month = Months.index(date_input[0])
        except ValueError:
            continue
        except (EOFError):
            break

    print(f"{date_input[2]}-{date_input[0]:02d}-{date_input[1]:02d}")

main()
