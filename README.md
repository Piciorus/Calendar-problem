# Calendar-problem
This repository contains a Python script that can be used to find available meeting slots between two people based on their calendars.The script finds the available time slots in each person's calendar and checks for overlaps to find meeting slots that are at least as long as the specified meeting time. The output is a list of lists of strings representing the start and end time of the available meeting slots.

Restrictions:
- each calendar will have limits, min and max range (ex: one maybe from 8:00 until 20:00,
maybe one starting from 10:00 until 18:00)
- the range of all available (free) time they can meet will have to fit into the meeting
required time (a variable input set to minutes)
- you must find all free time between the 2 calendars that is bigger or equal to the given
meeting minutes time
