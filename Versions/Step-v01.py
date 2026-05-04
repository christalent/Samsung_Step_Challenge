from datetime import date
import calendar

current_steps =  36143
monthly_steps = 200000

def main():
	today      = date.today()
	this_day   = today.day
	this_month = today.month
	this_year  = today.year
	days_in_current_month = calendar.monthrange(this_year, this_month)[1]
	days_left = days_in_current_month - this_day
	
	steps_per_day = monthly_steps / days_in_current_month
	steps_remaining = monthly_steps - current_steps
		
	print("Day\tTotal\tRemaining")
	print("------\t------\t---------")
	for day in range(1, days_in_current_month + 1):
		if day == this_day:
			highlight = '*'
		else:
			highlight = ''
		
		print("{}{}\t{}\t{}".format(day, highlight, int(steps_per_day * day), monthly_steps - int(steps_per_day * day)))

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
