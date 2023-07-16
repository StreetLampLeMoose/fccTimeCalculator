def add_time(start, duration , day = 0):
    new_time = ""
    minuteList = minutes(start, duration)
    hourDaysList = hourDaysCalc(start,duration)
    if day != 0 : 
        weekDay = dayOfWeek(start, duration, day)
        if hourDaysList[1] == 0 :
            new_time = str(hourDaysList[0]) + ":" + str(minuteList[0]) + " " + str(hourDaysList[2]) + ", " + weekDay
        elif hourDaysList[1] == 1 :
            new_time = str(hourDaysList[0]) + ":" + str(minuteList[0]) + " " + str(hourDaysList[2]) + ", " + weekDay + " (next day)"
        elif hourDaysList[1] > 1: 
            new_time = str(hourDaysList[0]) + ":" + str(minuteList[0]) + " " + str(hourDaysList[2]) + ", " + weekDay + " (" + str(hourDaysList[1]) + " days later)"
        return new_time
    if hourDaysList[1] == 0:     
         new_time = str(hourDaysList[0]) + ":" + str(minuteList[0]) + " " + str(hourDaysList[2])
    elif hourDaysList[1] == 1:
        new_time = str(hourDaysList[0]) + ":" + str(minuteList[0]) + " " + str(hourDaysList[2]) +  " (next day)"
    elif hourDaysList[1] > 1 : 
        new_time = str(hourDaysList[0]) + ":" + str(minuteList[0]) + " " + str(hourDaysList[2]) + " (" + str(hourDaysList[1]) + " days later"

    return new_time

def dataCleaner (start, duration) :
     
     startSplit = start.split(":")
     startHour = startSplit[0]
     startSplit = startSplit[1].split(" ")
     startMinutes = startSplit[0]
     startHalf = startSplit[1]
     if startHalf == "PM" : 
         startHour = int(startHour) + 12
     durationSplit = duration.split(":")
     durationHour = durationSplit[0]
     durationMinutes = durationSplit[1]
     cleanedData = list((startMinutes, startHour, startHalf, durationMinutes,durationHour))
     return cleanedData

def minutes (start, duration) : 
    minuteHourList = []
    hourNumber = 0
    cleanedData = dataCleaner(start, duration)
    startMinutes = int(cleanedData[0])
    durationMinutes = int(cleanedData[3])
    minuteNumber = startMinutes + durationMinutes 

    if minuteNumber > 60 : 
        minuteNumber = minuteNumber - 60
        hourNumber = 1

    if minuteNumber < 10 :
        minuteNumber = "0" + str(minuteNumber)
    minuteHourList.append(minuteNumber)
    minuteHourList.append(hourNumber)
    return minuteHourList

def hourDaysCalc(start, duration) :
    cleanedData = dataCleaner(start,duration)
    extraHour = minutes(start,duration)
    hourTotal = int(cleanedData[1]) + int(cleanedData[4]) + extraHour[1]
    amPm = cleanedData[2]
    if hourTotal >= 12 and hourTotal < 24: 
        if hourTotal == 12: 
            amPm = "PM"
            hour =hourTotal
            daysPassed = 0
        else :
            hour = hourTotal - 12
            amPm = "PM"
            daysPassed = 0
    elif hourTotal >= 24 : 
        hour = hourTotal % 24
        amPm = "AM"
        daysPassed = (hourTotal - hour) / 24
        if hour > 12 : 
            hour = hour-12
            amPm = "PM"
    else : 
        hour = hourTotal
        amPm = "AM"
        daysPassed = 0
    if hour == 0: 
        hour = 12
    hourDays = list((hour, int(daysPassed) , amPm))                         
    return hourDays



def daysLater (start, duration) : 
    #todo
    return

def dayOfWeek (start, duration , day) :
    day = day.lower()
    daysOfWeek = ["monday" , "tuesday" , "wednesday" , "thursday" , "friday" , "saturday","sunday"]
    daysOfWeekFormatted = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday","Sunday"]
    dayIndex = daysOfWeek.index(day)
    hourDays = hourDaysCalc(start,duration)
    dayIndex = dayIndex + hourDays[1]
    if dayIndex > 7 : 
        dayIndex = dayIndex % 7
        day = daysOfWeekFormatted[int(dayIndex)]
    else : 
        day = daysOfWeekFormatted[int(dayIndex)]
    return day

