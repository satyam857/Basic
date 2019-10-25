import datetime
import sys
def calculate_age(age):				#Calculating  Age
	today = datetime.date.today()
	try:
		day = abs(today.day - int(age[0:1]))
		month = abs(today.month - int(age[2:3]))
		year = abs(today.year - int(age[4:8]))
		#print([str(day),str(month),str(year)])
		return ([str(day),str(month),str(year)])
	except:
		help()

def format_date(accepted_age):		#convet date dd/mm/yyyy to ddmmyyyy
	if (len(accepted_age) == 10 and accepted_age[2] == "/" and accepted_age[5] == "/"):
		accepted_age = accepted_age.replace("/","")
		#print len(accepted_age)
		if (len(accepted_age) == 8):
			#print accepted_age
			return accepted_age
	help()

def help():
	print("Print a valid Date of Birth")
	print """Invalid Date Format\nUse This format : python Age.py dd/mm/yyyy """

def main():
		if (len(sys.argv) == 2):
			date = format_date(sys.argv[1])
			if date is not None:
				actual_age = calculate_age(date)
				print("{0} Year {1} Month and {2} Day".format(actual_age[2],actual_age[1],actual_age[0]))
				if actual_age[2]<=9:
					print("Your a kid")
				elif 10<=actual_age[2]<=13:
					print("Early Adolescence")
				elif 14<=actual_age[2]<=17:
					print("Middle Adolescence")
				elif 18<= actual_age[2] <=21:
					print("Late Adolescents")
				else:
					print("Your and adult now!")
		else:
			help()

main()
