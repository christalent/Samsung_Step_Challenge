from datetime import date

monthly_steps = 200000

def main():
	days_28  = 28
	days_30  = 30
	days_31  = 31
	
	steps_per_day_28 = monthly_steps / days_28
	steps_per_day_30 = monthly_steps / days_30
	steps_per_day_31 = monthly_steps / days_31
	
	today      = date.today()
	this_day   = today.day
	
	for day in range(1, days_31 + 1):
		if day == this_day:
			highlight = '*'
		else:
			highlight = ''
		if day <= 28:
			print("{}{}\t{}\t{}\t{}".format(day, highlight, int(steps_per_day_28 * day), int(steps_per_day_30 * day), int(steps_per_day_31 * day)))
		elif day <= 30:
			print("{}{}\t \t{}\t{}".format(day, highlight, int(steps_per_day_30 * day), int(steps_per_day_31 * day)))
		else:
			print("{}{}\t \t \t{}".format(day, highlight, int(steps_per_day_31 * day)))
			
	
if __name__ == "__main__":
	main()
