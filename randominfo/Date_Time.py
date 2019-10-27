import random, pytz
from  datetime import datetime

class Date_Time:
	def __init__(self, _format = "%d-%m-%Y %H:%M:%S", startRange = datetime(1970, 1, 1, 0, 0, 0, 0, pytz.UTC), endRange = datetime.today()):
		self._format = _format
		self.startRange = startRange
		self.endRange = endRange
		startTs = startRange.timestamp()
		endTs = datetime.timestamp(endRange)
		self.datetime = datetime.fromtimestamp(random.randrange(int(startTs), int(endTs)))
	
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
