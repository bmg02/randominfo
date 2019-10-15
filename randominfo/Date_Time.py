import random, pytz
from  datetime import datetime

class Date_Time:
	def __init__(self, _format = "%d-%m-%Y %H:%M:%S"):
		self._format = _format

	def set_format(self, _format):
		self._format = _format

	def get_format(self):
		return self._format

	def get_today(self):
		return datetime.today().strftime(self._format)

	def get_datetime(self, startRange = datetime(1970, 1, 1, 0, 0, 0, 0, pytz.UTC), endRange = datetime.today()):
		startTs = startRange.timestamp()
		endTs = datetime.timestamp(endRange)
		return datetime.strftime(datetime.fromtimestamp(random.randrange(int(startTs), int(endTs))), self._format)