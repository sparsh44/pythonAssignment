#  conditions for leap year
#   leap year if perfectly divisible by 400
# not leap year if perfectly divisible by 100
# leap if ND by 100 and 400 but divisible by 4

day=int(input("DAY: "))
month=int(input("MONTH: "))
year=int(input("YEAR: "))

if year%400==0:
    a=1
    #leap year

elif year%4==0 and year%100!=0 :
    a=1
    #leap year

else :
    a=2
    #not leap year
if day<=31 and month<=12:
    # 31 days months are 1 3 5 7 8 10 12
    if  month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day==31:
            day=1
            if month==12:
                month=1
                year=year+1
            else:
                month=month +1
        else:
            day=day+1
    # if leap year
    elif a==1:
        if month==2 and day==28:
            day=29
        elif month==2 and day==29 :
            day=1
            month=3
        else:
            if day==30:
                day=1
                month=month +1
            else:
                day=day+1
    #if not leap year
    elif a==2:
        if month==2 and day==28 :
            day=1
            month=3
        else:
            if day==30:
                day=1
                month=month +1
            else:
                day=day+1


    if month==4 or month==6 or month==11 or month==9:
        if day==31 or day==32:
            print("This day is not valid")
        else:
            print("Next Date is:",  day,"/",month,"/",year)

    elif a==2 and month ==2 and day>=29:
        print("This day is not valid")     
    else:
        print("Next Date is:",  day,"/",month,"/",year)

else:
    print("This is not a valid date")
