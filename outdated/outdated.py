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

            if int(date_input[0]) > 12 or int(date_input[0]) < 0:
                raise ValueError

            if int(date_input[1]) > 31 or int(date_input[1]) < 0:
                raise ValueError

            if date_input[0] in Months:
                word_to_number_month = str(Months.index(date_input[0])+1)
                print(f"{date_input[2]}-{word_to_number_month.zfill(2)}-{date_input[1].zfill(2)}")

            print(f"{date_input[2]}-{date_input[0].zfill(2)}-{date_input[1].zfill(2)}") #zfill is better than format as it helps assigning it to var
            break
        except ValueError:
            continue
        except (EOFError):
            break



main()
