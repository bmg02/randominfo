from __future__ import unicode_literals
import sys, glob, csv, pytz
from os import listdir
from os.path import abspath, join, dirname, split, exists
sys.path.append("/randominfo/")
#from .Person import Person
from random import randint, choice, sample, randrange
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


__title__ = 'randominfo'
__version__ = '0.1'
__author__ = 'Bhuvan Gandhi'
__license__ = 'MIT'

full_path = lambda filename: abspath(join(dirname(__file__), filename))

def get_first_name(gender = None):
	firstNameFile = csv.reader(open(full_path('first-names.csv'), 'r'))
	filteredData = []
	if gender == None:
			for data in firstNameFile:
				filteredData.append(data)
	else:
		if gender.lower() == "male":
			for data in firstNameFile:
				if(data[2] == "male"):
					filteredData.append(data)
		elif gender.lower() == "female":
			for data in firstNameFile:
				if(data[2] == "female"):
					filteredData.append(data)
		else:
			raise ValueError("Only 'male' and 'female' are supported as gender.")
	
	return choice(filteredData)[0]

def get_last_name():
	lastNameFile = csv.reader(open(full_path('last-names.csv'), 'r'))
	filteredData = []
	for data in lastNameFile:
			filteredData.append(data)
	return choice(filteredData)[0]

def get_full_name(gender = None):
	return get_first_name(gender) + " " + get_last_name()

def get_digit_otp(len):
    otp = ""
    for _ in range(len):
        otp += str(randint(1,9))
    return otp

def get_chars_otp(len, lowerCase = True, upperCase = True):
    otp = ""
    chars = ""
    if lowerCase == True:
        if upperCase == True:
            chars = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
        else:
            chars = "qwertyuioplkjhgfdsazxcvbnm"
    else:
        if upperCase == True:
            chars = "QWERTYUIOPLKJHGFDSAZXCVBNM"
        else:
            return "Invalid combination."
    for _ in range(len):
        otp += str(chars[randint(0, len(chars) - 1)])
    return otp

def get_otp(len):
    otp = ""
    chars = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789"
    for _ in range(len):
        otp += str(chars[randint(0, len(chars) - 1)])
    return otp

def get_formatted_datetime(strDate, _format = "%d-%m-%Y %H:%M:%S"):
    return datetime.strptime(strDate, _format)

def get_email(Person = None):
	domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance", "company", "corporation", "community"]
	extentions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site', 'xyz', 'zero', 'tech']
	#email = "qwe@abc.com"
	#Comments starts here
	if Person == None:
		prsn = Person()
	else:
		prsn = Person
	
	c = randint(0,2)
	dmn = choice(domains)
	ext = choice(extentions)
	
	if c == 0:
		email = prsn.first_name + get_formatted_datetime(prsn.birthdate(), "%Y") + dmn + "." + ext
	elif c == 1:
		email = prsn.last_name + get_formatted_datetime(prsn.birthdate(), "%d") + dmn + "." + ext
	else:
		email = prsn.first_name + get_formatted_datetime(prsn.birthdate(), "%y") + dmn + "." + ext
	#Comments ends here
	return email

def random_password(length = 8, special_chars = True, digits = True):
    spec_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    alpha = "QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq"
    spec_char_len = 0
    chars = ""
    if special_chars == True:
        spec_char_len = randint(1,3)
        for _ in range(spec_char_len):
            chars += choice(spec_chars)

    if digits == True:
        spec_char_len = randint(0,9)
        for _ in range(spec_char_len):
            chars += str(randint(0,9))

    for _ in range(length - spec_char_len):
        chars += choice(alpha[randint(0, len(alpha) - 1)])

    paswd = ''.join(sample(chars, len(chars)))
    return paswd

def get_phone_number(country_code = True):
    phone = ""
    if country_code == True:
        cCodes = [91, 144, 141, 1, 44, 86, 52, 61, 32, 20, 33, 62, 81, 31, 7]
        phone = "+"
        phone += str(choice(cCodes))
        phone += " "
    for i in range(0,10):
        if i == 0:
            phone += str(randint(8,9))
        else:
            phone += str(randint(0,9))
    return phone

def get_alphabet_profile_img(char, bgColor = None, filePath = None, fileName = None):
	if char.isalpha():
		char = char[:1].upper()
		if bgColor == None:
			colors = ['red', 'green', 'royalblue', 'violet', 'pink', 'indigo', 'grey', 'yellowgreen']
			bgColor = choice(colors)
		img = Image.new('RGB', (512, 512), color = bgColor)
		d = ImageDraw.Draw(img)
		font = ImageFont.truetype("Candara.ttf", 280)
		d.text((170,140), char, fill=(255,255,255), font = font)
		if filePath == None:
			filePath = dirname(abspath(__file__)).replace('\\', '\\\\')
		else:
			if not exists(filePath):
				raise OSError("File is already exists there.")
		
		if fileName == None:
			fileName = char + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(':', '-')
		imgName = str(filePath) + "\\" + str(fileName) + '.png'
	else:
		raise ValueError("Specify valid alphabet character in argument.")
	return imgName

def get_real_profile_img(gender = None):
	if gender == None:
		imgName = choice(listdir("imgs/"))
	elif gender.lower() == "female":
		imgName = choice(glob.glob("images/people/female_*.jpg"))
	elif gender.lower() == "male":
		imgName = choice(glob.glob("images/people/male_*.jpg"))
	else:
		return ValueError("Invalid gender. It must be male or female.")
	return imgName


class Date_Time:
	def __init__(self, _format = "%d-%m-%Y %H:%M:%S", startRange = datetime(1970, 1, 1, 0, 0, 0, 0, pytz.UTC), endRange = datetime.today()):
		self._format = _format
		self.startRange = startRange
		self.endRange = endRange
		startTs = startRange.timestamp()
		endTs = datetime.timestamp(endRange)
		self.datetime = datetime.fromtimestamp(randrange(int(startTs), int(endTs)))
	
	def set_startRange(self, startRange):
		self.startRange = startRange
	
	def get_startRange(self):
		return self.startRange
	
	def set_endRange(self, endRange):
		self.endRange = endRange
	
	def get_endRange(self, endRange):
		return self.endRange

	def set_format(self, _format):
		self._format = _format

	def get_format(self):
		return self._format

	def get_today(self):
		return datetime.today().strftime(self._format)
	
	def get_date(self, _format = "%d %b, %Y"):
		return self.datetime.strftime(_format)

	def get_time(self, _format = "%H:%M:%S"):
		return self.datetime.strftime(_format)

	def get_datetime(self):
		return self.datetime

	def get_year_diff(self, year = datetime.now().year):
		return year - self.datetime.year

class Person:
	def __init__(self, gender = None, country = None):
		self.first_name = get_first_name()
		self.last_name = get_last_name()
		self.full_name = self.first_name + " " + self.last_name
		dob = Date_Time()
		self.birthdate = dob.get_date()
		self.phone = get_phone_number()
		self.email = get_email()
		self.gender = gender
		self.country = country
		self.paswd = random_password()

	def get_full_name(self):
		return self.full_name

	def get_first_name(self):
	    return self.first_name

	def get_last_name(self):
	    return self.last_name
	
	def get_gender(self):
		return self.gender
	
	def get_birthdate(self):
		return self.birthdate
	
	def get_email(self):
		return self.email
	
	def get_password(self):
		return self.paswd
	
	def get_country(self):
		return self.country

	def get_all(self):
		return [
			self.first_name,
			self.last_name,
			self.birthdate,
			self.gender,
			self.email,
			self.phone,
			self.paswd,
			self.country
		]


'''
REFERENCE:
http://www.first-names-meanings.com/country-indian-names.html
https://www.familyeducation.com/baby-names/browse-origin/surname/indian
https://thispersondoesnotexist.com/
'''