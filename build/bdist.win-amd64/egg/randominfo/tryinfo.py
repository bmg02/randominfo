import random, csv
from os.path import abspath, join, dirname
from .Date_Time import Date_Time
from . import get_email as getEmail, random_password, get_phone_number as getPhone, get_full_name as getFullName, get_last_name as getLName, get_first_name as getFName

full_path = lambda filename: abspath(join(dirname(__file__), filename))

class Person:
	def __init__(self, gender = None, country = None):
		self.first_name = getFName()
		self.last_name = getLName()
		self.full_name = self.first_name + " " + self.last_name
		dob = Date_Time()
		self.birthdate = dob.get_date()
		self.phone = getPhone()
		self.email = getEmail()
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