import random
import datetime
birthday=[]
i=0
while (i<50):
    year = random.randint(1993,2025)
    if year%4==0 and year%100!=0 or year%400==0:
        leap=1
    else:
        leap=0
    month= random.randint(1,12)
    if(month==2 and leap==1):
        day= random.randint(1,29)
    elif (month==2 and leap==0):
        day = random.randint(1,28)
    elif month==7 and month==8:
        day = random.randint(1,31)
    elif (month%2!=0 and month<7):
        day= random.randint(1,31)
    elif (month%2!=0 and month>7 and month<12):
        day= random.randint(1,31)
    else:
        day= random.randint(1,30)
    dd = datetime.date(year,month,day)
    day_of_year  = dd.timetuple().tm_yday
    i=i+1
    birthday.append(day_of_year)
birthday.sort()
i=0
while(i<50):
    print(birthday[i])
    i+=1
for i in birthday:
    if birthday.count(i)>1:
        print(f" The repeated birthdays are {i}")



# # Alternate version

# import random
# import datetime

# birthday = []
# dates = []  # store full dates for later duplicate check

# i = 0
# while i < 50:
#     year = random.randint(1993, 2025)

#     # Check leap year
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         leap = 1
#     else:
#         leap = 0

#     month = random.randint(1, 12)

#     # Determine day correctly
#     if month == 2 and leap == 1:
#         day = random.randint(1, 29)
#     elif month == 2 and leap == 0:
#         day = random.randint(1, 28)
#     elif month == 7 or month == 8:  # fixed condition
#         day = random.randint(1, 31)
#     elif month % 2 != 0 and month < 7:
#         day = random.randint(1, 31)
#     elif month % 2 != 0 and month > 7 and month < 12:
#         day = random.randint(1, 31)
#     else:
#         day = random.randint(1, 30)

#     # Create date and compute day of year
#     dd = datetime.date(year, month, day)
#     day_of_year = dd.timetuple().tm_yday

#     birthday.append(day_of_year)
#     dates.append(dd)

#     i += 1

# # Sort and display day_of_year
# birthday.sort()
# for d in birthday:
#     print(d)

# # ✅ Detect duplicates correctly (without repeating output)
# print("\nRepeated day_of_year values:")
# seen = set()
# duplicates = set()
# for d in birthday:
#     if d in seen:
#         duplicates.add(d)
#     else:
#         seen.add(d)
# print(duplicates if duplicates else "None")

# # ✅ Detect repeated full dates
# print("\nRepeated full dates:")
# seen_dates = set()
# duplicates_dates = set()
# for d in dates:
#     if d in seen_dates:
#         duplicates_dates.add(d)
#     else:
#         seen_dates.add(d)
# print(duplicates_dates if duplicates_dates else "None")





        

