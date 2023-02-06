print((lambda time: "At School"if time[0]*60+time[1]>=450 and time[0]*60+time[1]<1020 else "Off School")([int(i) for i in input().split()]))
