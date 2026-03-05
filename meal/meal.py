def main():
    time = input("What time is it? ")
    prased_time = convert(time)
    #print(prased_time)
    if prased_time >= 7 and prased_time <=8:
        print("breakfast time")
    elif prased_time >= 12 and prased_time <=13:
        print("lunch time")
    elif prased_time >= 18 and prased_time <=19:
        print("dinner time")
    

def convert(time):
    hours, minutes = time.split(":")
    return float(int(hours)+(int(minutes)/60))

if __name__ == "__main__":
    main()
