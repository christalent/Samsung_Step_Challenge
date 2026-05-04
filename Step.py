from datetime import date
import calendar
import math

current_steps =  15717

monthly_steps = 200000
infinity = math.inf 

date_star_array = [ [4,20000], [7,35000], [13,70000], [18,100000], [25,150000] ]

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
	
	current_star_date, current_star_steps =  date_star_array.pop(0)
		
	for day in range(1, days_in_current_month + 1):
		if day == this_day:
			highlight = '*'
		else:
			highlight = ''
			
		if day == current_star_date:
			highlight = highlight + '!'
		
		if day == current_star_date:
			print("{}{}\t{}\t{}\t{}".format(day, highlight, int(steps_per_day * day), monthly_steps - int(steps_per_day * day), current_star_steps))
			if date_star_array:
				current_star_date, current_star_steps =  date_star_array.pop(0)
			else:
				current_star_steps = infinity
				current_star_date = infinity

		else:
			if (current_star_steps > int(steps_per_day * day) or (current_star_date > day)):
				print("{}{}\t{}\t{}".format(day, highlight, int(steps_per_day * day), monthly_steps - int(steps_per_day * day)))
					
			else:
				print("{}{}\t{}\t{}\t{}".format(day, highlight, int(steps_per_day * day), monthly_steps - int(steps_per_day * day), current_star_steps))
				if date_star_array:
					current_star_date, current_star_steps =  date_star_array.pop(0)
				else:
					current_star_steps = infinity
					current_star_date = infinity

		
	
	print("------\t------\t---------")
	print("{}\tdays left after today".format(days_left))
	print("{}\tsteps taken".format(current_steps))
	if (steps_remaining > 0):
		print("{}\tsteps remaining".format(steps_remaining))
	if (days_left > 0):
		print("")
		print("{}\taverage daily steps needed as of today ".format(int(steps_remaining / (days_left + 1))))
		print("{}\taverage daily steps needed after today ".format(int(steps_remaining / days_left)))
		
	
if __name__ == "__main__":
	main()
