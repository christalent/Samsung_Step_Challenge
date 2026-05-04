from datetime import date
import calendar
import math

current_steps =  13313
monthly_steps = 200000
infinity = math.inf

star_array = [20000, 60000, 90000, 120000, 160000]

def main():
	today      = date.today()
	this_day   = today.day
	this_month = today.month
	this_year  = today.year
	days_in_current_month = calendar.monthrange(this_year, this_month)[1]
	days_left = days_in_current_month - this_day
	
	steps_per_day = monthly_steps / days_in_current_month
	steps_remaining = monthly_steps - current_steps
		
	print("Day\tTotal\tRemain\tStar")
	print("------\t------\t------\t----")
	
	current_star = star_array.pop(0)
	
	for day in range(1, days_in_current_month + 1):
		if day == this_day:
			highlight = '*'
		else:
			highlight = ''
		
		if (current_star > int(steps_per_day * day)):
			print("{}{}\t{}\t{}".format(day, highlight, int(steps_per_day * day), monthly_steps - int(steps_per_day * day)))
		else:
			print("{}{}\t{}\t{}\t{}".format(day, highlight, int(steps_per_day * day), monthly_steps - int(steps_per_day * day), current_star))
			if star_array:
				current_star = star_array.pop(0)
			else:
				current_star = infinity

	print("------\t------\t---------")
	print("{}\tdays left after today".format(days_left))
	if (steps_remaining > 0):
		print("{}\tsteps remaining".format(steps_remaining))
	if (days_left > 0):
		print()
		print("{}\taverage daily steps needed as of today ".format(int(steps_remaining / (days_left + 1))))
		print("{}\taverage daily steps needed after today ".format(int(steps_remaining / days_left)))
		
	
if __name__ == "__main__":
	main()
