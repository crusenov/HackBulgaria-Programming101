"""
 d = {   "Aries": (21,3), (20,3)	21 March – 20 April
    	 "Taurus": (21,4), (21,5)	21 April – 21 May
    	 "Gemini": (22,5), (21,6)	22 May – 21 June
    	 "Cancer": (22,6), (22,7)	22 June – 22 July
    	 "Leo": (23, 7), (22,8)		23 July – 22 August
    	 "Virgo": (23,8), (23,9)	23 August – 23 September
    	 "Libra": (24,9), (23,10)	24 September – 23 October
    	 "Scorpio": (24,10), (22,11)	24 October – 22 November
    	 "Sagittarius": (23,11), (21,12)	23 November – 21 December
    	 "Capricorn": (22,12), (20,1)	22 December – 20 January
    	 "Aquarius": (21,1), (19,2)	21 January – 19 February
    	 "Pisces": (20,1), (20,3)	20 February – 20 March
}
"""

def what_is_my_sign(day, month):
	if (day >= 21 and month == 3) or (day <= 20 and month == 4):
		return "Aries"
	elif (day >= 21 and month == 4) or (day <= 21 and month == 5):
		return "Taurus"
	elif (day >= 22 and month == 5) or (day <= 21 and month == 6):
		return "Gemini"
	elif (day >= 22 and month == 6) or (day <= 22 and month == 7):
		return "Cancer"
	elif (day >= 23 and month == 7) or (day <= 22 and month == 8):
		return "Leo"
	elif (day >= 23 and month == 8) or (day <= 23 and month == 9):
		return "Virgo"
	elif (day >= 24 and month == 9) or (day <= 23 and month == 10):
		return "Libra"
	elif (day >= 24 and month == 10) or (day <= 23 and month == 11):
		return "Scorpio"
	elif (day >= 23 and month == 11) or (day <= 21 and month == 12):
		return "Sagittarius"
	elif (day >= 22 and month == 12) or (day <= 20 and month == 1):
		return "Capricorn"
	elif (day >= 21 and month == 1) or (day <= 19 and month == 2):
		return "Aquarius"
	elif (day >= 20 and month == 2) or (day <= 20 and month == 3):
		return "Pisces"
