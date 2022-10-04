time = input("시간 입력")
time = time.split(" ")
min = int(time[1])
hour = int(time[0])

if(min - 45 < 0) :
    if(hour == 0) :
        hour = 23
    else :
        hour = hour - 1
    min = (min + 15)
else :
    min = min - 45

print(hour , min)

