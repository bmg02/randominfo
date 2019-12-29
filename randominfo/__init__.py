from __future__ import unicode_literals
import sys, glob, csv, pytz, shutil
from os import listdir, getcwd
from os.path import abspath, join, dirname, split, exists, isfile
sys.path.append("/randominfo/")
from random import randint, choice, sample, randrange
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


__title__ = 'randominfo'
__version__ = '0.0.4'
__author__ = 'Bhuvan Gandhi'
__license__ = 'MIT'

full_path = lambda filename: abspath(join(dirname(__file__), filename))

class CustomError(Exception):
    def __init__(self, err):
        self.err = err
        pass
    def __str__(self):
        return self.err

def get_first_name(gender = None):
	firstNameFile = csv.reader(open(full_path('data.csv'), 'r'))
	filteredData = []
	if gender == None:
		for data in firstNameFile:
			if data[0] != '':
				filteredData.append(data)
	else:
		if gender.lower() == "male":
			for data in firstNameFile:
				if data[0] != '':
					if(data[2] == "male"):
						filteredData.append(data)
		elif gender.lower() == "female":
			for data in firstNameFile:
				if data[0] != '':
					if(data[2] == "female"):
						filteredData.append(data)
		else:
			raise CustomError("Enter gender male or female.")
	selectedData = choice(filteredData)
	return [selectedData[0], selectedData[2]]

def get_last_name():
	lastNameFile = csv.reader(open(full_path('data.csv'), 'r'))
	filteredData = []
	for data in lastNameFile:
		if data[1] != '':
			filteredData.append(data[1])
	return choice(filteredData)

def get_full_name(gender = None):
	return get_first_name(gender)[0] + " " + get_last_name()

def get_otp(len, onlyDigits = True, onlyAlpha = True, lowercase = True, uppercase = True):
	lwrChars = "qwertyuioplkjhgfdsazxcvbnm"
	uprChars = "QWERTYUIOPLKJHGFDSAZXCVBNM"
	digs = "0123456789"
	chars = ""
	if onlyDigits == True:
		chars += digs
	if onlyAlpha == True:
		if lwrChars == True:
			chars += lwrChars
		if uprChars == True:
			chars += uprChars
	for _ in range(len):
		otp += str(chars[randint(0, len(chars) - 1)])
	return otp

def get_formatted_datetime(strDate, _format = "%d-%m-%Y %H:%M:%S"):
    return datetime.strptime(strDate, _format)

def get_email(Person = None):
	domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance", "company", "corporation", "community"]
	extentions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site', 'xyz', 'zero', 'tech']
	
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

def get_face_profile_img(filePath, gender = None):
	if gender == None:
		imgName = choice(glob.glob(getcwd() + "\\randominfo\\images\\people\\*.jpg"))
	elif gender.lower() == "female":
		imgName = choice(glob.glob(getcwd() + "\\randominfo\\images\\people\\female_*.jpg"))
	elif gender.lower() == "male":
		imgName = choice(glob.glob(getcwd() + "\\randominfo\\images\\people\\male_*.jpg"))
	else:
		return ValueError("Invalid gender. It must be male or female.")
	return shutil.copyfile(imgName, filePath)

startRange = datetime(1970, 1, 1, 0, 0, 0, 0, pytz.UTC)
endRange = datetime.today()

def get_today(_format = "%d-%m-%Y %H:%M:%S"):
	return datetime.today().strftime(_format)

def get_date(tstamp = None, _format = "%d %b, %Y"):
	if tstamp == None:
		startTs = startRange.timestamp()
		endTs = datetime.timestamp(endRange)
		tstamp = datetime.fromtimestamp(randrange(int(startTs), int(endTs)))
		return datetime.fromtimestamp(int(tstamp)).strftime(_format)
	else:
		if type(tstamp).__name__ != 'int':
			raise CustomError("Timestamp must be an integer.")
		else:
			return datetime.fromtimestamp(int(tstamp)).strftime(_format)

def get_birthdate(startAge = None, endAge = None, _format = "%d %b, %Y"):
	if startAge != None:
		if type(startAge).__name__ != 'int':
			raise CustomError("Starting age value must be integer.")
	if endAge != None:
		if type(endAge).__name__ != 'int':
			raise CustomError("Ending age value must be integer.")
	if startAge != None and endAge != None: #If both are given in arg
		if startAge >= endAge:
			raise CustomError("Starting age must be less than ending age.")
		else:
			startRange.year = endRange.year - startAge
			endRange.year = endRange.year - endAge
	if startAge != None or endAge != None: #If anyone is given in arg
		ageYear = startAge if startAge != None else endAge
		startRange = datetime(endRange.year - ageYear, 1, 1, 0, 0, 0, 0, pytz.UTC)
		endRange = datetime(endRange.year - ageYear, 12, 31, 0, 0, 0, 0, pytz.UTC)
	else:
		pass
	startTs = startRange.timestamp()
	endTs = datetime.timestamp(endRange)
	tstamp = datetime.fromtimestamp(randrange(int(startTs), int(endTs)))
	return datetime.fromtimestamp(int(tstamp)).strftime(_format)

def get_address():
	full_addr = []
	addrParam = ['street', 'landmark', 'area', 'city', 'state', 'pincode']
	for i in range(4,10):
		addrFile = csv.reader(open('data.csv', 'r'))
		allAddrs = []
		for addr in addrFile:
			if addr[i] != '':
				allAddrs.append(addr[i])
		full_addr.append(choice(allAddrs))
	full_addr = dict(zip(addrParam, full_addr))
	return full_addr

def get_hobbies():
	hobbiesFile = csv.reader(open(full_path('data/hobbies.csv'), 'r'))
	allHobbies = []
	for data in hobbiesFile:
		allHobbies.append(data)
	hobbies = []
	for _ in range (1, randint(2,6)):
		hobbies.append(choice(allHobbies))
	return hobbies

class Person:
	def __init__(self, gender = None):
		firstName = get_first_name(gender)
		self.first_name = firstName[0]
		self.last_name = get_last_name()
		self.full_name = self.first_name + " " + self.last_name
		self.birthdate = get_birthdate()
		self.phone = get_phone_number()
		self.email = get_email()
		self.gender = firstName[2]
		self.country = firstName[1]
		self.paswd = random_password()
		self.hobbies = get_hobbies()
		self.address = get_address()

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
	
	def get_hobbies(self):
		return self.hobbies
	
	def get_address(self):
		return self.address

	def get_details(self):
		return {
			"first_name": self.first_name,
			"last_name": self.last_name,
			"birthdate": self.birthdate,
			"gender": self.gender,
			"email": self.email,
			"phone": self.phone,
			"paswd": self.paswd,
			"country": self.country,
			"hobbies": self.hobbies,
			"address": self.address
		}


'''
REFERENCE:
http://www.first-names-meanings.com/country-indian-names.html
https://www.familyeducation.com/baby-names/browse-origin/surname/indian
https://thispersondoesnotexist.com/
https://en.wikipedia.org/wiki/List_of_hobbies
'''