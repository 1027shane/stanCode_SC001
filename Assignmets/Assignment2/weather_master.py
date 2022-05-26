"""
File: weather_master.py
Name: Shane Liu
-------------------------
This program should implement a console program that asks weather data
from user to compute the average, highest, lowest, cold days among the inputs.
"""

EXIT = -1
COLDAY = 16


def main():
	"""
	This program asks weather data from user to compute the
	(1)average, (2)highest, (3)lowest, (4)cold days among the inputs.
	"""
	print('stanCode \"weather Master 4.0"!')
	temperature = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))

	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = minimum = temperature
		
		# total: to sum up of the weather data
		# count: to count the number of weather data
		# average = total/count
		# lowday: to count the number of cold days, temperature below the parameter "COLDAY"
		total = count = lowday = 0

		while True:
			temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if temperature == EXIT:
				break
			else:
				# Highest temperature
				if maximum < temperature:
					maximum = temperature
				
				# Lowest temperature
				if minimum > temperature:
					minimum = temperature
				
				if temperature < COLDAY:
					lowday += 1
				
				total += temperature
				count += 1

		print('Highest temperature = '+str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = '+str(total/count))
		print(str(lowday)+' cold day(s)')


if __name__ == "__main__":
	main()
