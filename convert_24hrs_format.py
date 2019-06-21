def convert(time_12hr_format):
	actual_time = "  "
	
	if(int(time_12hr_format[:2]) > 12 or int(time_12hr_format[3:5])>60 or int(time_12hr_format[6:8])>60 or 
		(time_12hr_format[-2:] != 'AM' or "PM")):
			raise ValueError("the given time is invalid")
	if(time_12hr_format[-2:] == 'AM' and time_12hr_format[:2] == '12'):
		actual_time = "00" + time_12hr_format[2:-2]
	elif (time_12hr_format == 'AM'):
		actual_time = time_12hr_format
	elif (time_12hr_format == 'PM' and time_12hr_format[:2] == "12"):
		actual_time = "12" + time_12hr_format[2:-2]
	else:
		
		actual_time = str((int(time_12hr_format[:2])+12)) + time_12hr_format[2:-2]
	return actual_time	
		
time = input("enter the time in 12 hours format:")
print("The given time in 24 hours format is:",convert(time))
