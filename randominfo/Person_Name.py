import random, csv
from os.path import abspath, join, dirname

full_path = lambda filename: abspath(join(dirname(__file__), filename))

class Person_Name:
	def __init__(self, gender = None, country = None):
		self.gender = gender
		self.country = country

	def set_gender(self, gender):
		self.gender = gender

	def get_gender(self):
		return self.gender
	
	def set_country(self, country):
		self.country = country

	def get_country(self):
		return self.country

	def get_full_name(self, firstName = True, lastName = True):
		firstNameFile = csv.reader(open(full_path('first-names.csv'), 'r'))
		lastNameFile = csv.reader(open(full_path('last-names.csv'), 'r'))
		filteredData = []
		full_name = ""
		if firstName == True:
			if self.gender == None:
				for data in firstNameFile:
					filteredData.append(data)
			else:
				if self.gender.lower() == "male":
					for data in firstNameFile:
						if(data[2] == "male"):
							filteredData.append(data)
				elif self.gender.lower() == "female":
					for data in firstNameFile:
						if(data[2] == "female"):
							filteredData.append(data)
				else:
					raise ValueError("Only 'male' and 'female' are supported as gender.")
			
			full_name += random.choice(filteredData)[0]

		if lastName == True:
			for data in lastNameFile:
				filteredData.append(data)
			full_name = full_name + " " + random.choice(filteredData)[0]
		
		return full_name.strip()

	def get_first_name(self):
	    return self.get_full_name(firstName = True, lastName = False)

	def get_last_name(self):
	    return self.get_full_name(firstName = False, lastName = True)