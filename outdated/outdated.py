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
def my_soulution(): # i made solution that accepts more formats, however course demanded that (example: October/9/1999) is wrong

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
            x = input("Date: ").strip() #strip input off spaces
            if not x[0].isdigit(): #if first character is not a number
                m, d, y = x.split(" ") #split into 3 variables based on space
                if not d.endswith(','): #if d variable does not end with ',' reprompt
                    continue
                d = d.replace(',', '') #replace the ','
                d = int(d) # turn days and years into ints from strings
                y = int(y)
                m = m.capitalize() # capitalize to make sure it finds index of list
                if (1 <= d <= 31): # if days are in correct limits of a month, print year, index of month in list and day with a separator
                    print(y, f'{Months.index(m)+1:02}',f'{d:02}', sep="-")
                    break
            else:
                m, d, y = map(int, x.split("/")) #split based on '/' and map variables as ints in one go
                if 1 <= m <= 12 and 1 <= d <= 31: #if norms are correct continue
                    print(y, f'{m:02}',f'{d:02}', sep="-") #print date in requested format
                    break
        except ValueError:
            continue
        except (EOFError):
            break
main()




