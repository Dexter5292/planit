from datetime import date
import math

def weekdays(date1, date2):
	date1 = date1.split("-")
	date2 = date2.split("-")

	delta = date(int(date2[0]), int(date2[1]), int(date2[2])) - date(int(date1[0]), int(date1[1]), int(date1[2]))
	weekd = math.ceil(delta.days * (5/7))
	return weekd