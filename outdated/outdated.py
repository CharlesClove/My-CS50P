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
def my_soulution():

    while(True):
        try:
            date_input = re.split(', | |/',input("Date: ").strip()) #using regex I split both dates that use slash spaces, etc
            #January, 8, 1999 or 1/9/1999 logic for string month, logic for 2 and 3 postition to be a int
            if len(date_input) != 3:
                raise ValueError
            if int(date_input[1]) > 31 or int(date_input[1]) < 0:
                raise ValueError
            if date_input[0].isdigit():
                if int(date_input[0]) > 12 or int(date_input[0]) < 0:
                    raise ValueError
                print(f"{date_input[2]}-{date_input[0].zfill(2)}-{date_input[1].zfill(2)}") #zfill is better than format as it helps assigning it to var
            if date_input[0] in Months:
                word_to_number_month = str(Months.index(date_input[0])+1)
                print(f"{date_input[2]}-{word_to_number_month.zfill(2)}-{date_input[1].zfill(2)}")
            break
        except ValueError:
            continue
        except (EOFError):
            break

def main():
    while(True):
        try:
            x = input("Date: ").strip()
            if not x[0].isdigit():
                m, d, y = x.split(" ")
                if not d.endswith(','):
                    continue
                d = d.replace(',', '')
                d = int(d)
                y = int(y)
                m = m.capitalize()
                if (1 <= d <= 31):
                    print(y, f'{Months.index(m)+1:02}',f'{d:02}', sep="-")
                    break
            else:
                m, d, y = map(int, x.split("/"))
                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(y, f'{m:02}',f'{d:02}', sep="-")
                    break

        except (EOFError):
            break
main()




