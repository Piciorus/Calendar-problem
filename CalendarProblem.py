from datetime import datetime, timedelta

# This function calculates the available time slots for scheduling a meeting
def getAvailableSlotsFromCalendar(calendar, rangeCalendar, meetingTime):
    """
    :param calendar: list of lists of strings,which represent the calendar with the meetings time
    :param rangeCalendar: list of strings, which represent the start and end time of the calendar(range)
    :param meetingTime: int, which represents the duration of the meeting
    :return: list of lists of strings, which represent the start and end time of the available slots
    """
    startTimeCalendar = datetime.strptime(rangeCalendar[0], '%H:%M')
    endTimeCalendar = datetime.strptime(rangeCalendar[1], '%H:%M')
    availableSlots = []
    # here iterate through the booked time slots in the calendar and checking the time slots between them.
    # If there is a gap that is at least as long as the meeting time,then add it to the available slots
    for i, slot in enumerate(calendar):
        if i == 0:
            if startTimeCalendar < datetime.strptime(slot[0], '%H:%M'):
                freeSlot = [startTimeCalendar.strftime('%H:%M'), slot[0]]
                if (datetime.strptime(freeSlot[1], '%H:%M') - datetime.strptime(freeSlot[0], '%H:%M')) >= timedelta(
                        minutes=meetingTime):
                    availableSlots.append(freeSlot)
        else:
            prevSlot = calendar[i - 1]
            freeSlot = [prevSlot[1], slot[0]]
            if (datetime.strptime(freeSlot[1], '%H:%M') - datetime.strptime(freeSlot[0], '%H:%M')) >= timedelta(
                    minutes=meetingTime):
                availableSlots.append(freeSlot)
        # if there is a gap between the last slot and the end of the calendar range then add it to the available slots
        if i == len(calendar) - 1:
            if endTimeCalendar > datetime.strptime(slot[1], '%H:%M'):
                freeSlot = [slot[1], endTimeCalendar.strftime('%H:%M')]
                if (datetime.strptime(freeSlot[1], '%H:%M') - datetime.strptime(freeSlot[0], '%H:%M')) >= timedelta(
                        minutes=meetingTime):
                    availableSlots.append(freeSlot)
    return availableSlots

# This function calculates the available time slots in the calendar where meetings
# could potentially be scheduled, given a specified meeting duration.
def getMeetingSlots(calendar1, calendar1Range, calendar2, calendar2Range, meetingTime):
    """
    :param calendar1:  list of lists of strings,which represent the calendar with the meetings time from the person1
    :param calendar1Range: list of strings, which represent the start and end time of the calendar(range) from the person1
    :param calendar2: list of lists of strings,which represent the calendar with the meetings time from the person2
    :param calendar2Range: list of strings, which represent the start and end time of the calendar(range) from the person2
    :param meetingTime: int, which represents the duration of the meeting
    :return: list of lists of strings, which represent the start and end time of the available slots
    """
    availableSlots1 = getAvailableSlotsFromCalendar(calendar1, calendar1Range, meetingTime)
    availableSlots2 = getAvailableSlotsFromCalendar(calendar2, calendar2Range, meetingTime)
    meetingSlots = []
    # here iterate through the available slots of each calendar,and checking if there is any overlap between them.
    # If there is and the overlap is at least as long as the meeting time,then add it to the meeting slots
    for slot1 in availableSlots1:
        for slot2 in availableSlots2:
            startTime = max(datetime.strptime(slot1[0], '%H:%M'), datetime.strptime(slot2[0], '%H:%M'))
            endTime = min(datetime.strptime(slot1[1], '%H:%M'), datetime.strptime(slot2[1], '%H:%M'))
            if (endTime - startTime) >= timedelta(minutes=meetingTime):
                meetingSlots.append([startTime.strftime('%H:%M'), endTime.strftime('%H:%M')])
    return meetingSlots


calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00'], ['19:00', '20:00']]
calendar1Range = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
calendar2Range = ['10:00', '18:30']
meetingTime = 30

meetingSlots = getMeetingSlots(calendar1, calendar1Range, calendar2, calendar2Range, meetingTime)
print(meetingSlots)

# datetime.strptime: It's a method that creates a datetime object from a string representing a date and time, using a specified format.
# For example, datetime.strptime('9:00', '%H:%M') will create a datetime object with hour = 9 and minute = 0.

# timedelta: It's a class that represents a duration, or the difference between two dates or times. It's used for performing arithmetic with dates and times.
# For example, timedelta(minutes=30) creates a duration of 30 minutes.

# startTimeCalendar.strftime('%H:%M'): It's a method that creates a string representation of a datetime object, using a specified format.
# For example, startTimeCalendar.strftime('%H:%M') will create a string in the format of "hour:minute" (e.g. "09:00").
