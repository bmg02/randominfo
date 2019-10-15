from __future__ import unicode_literals
import sys, os
sys.path.append("/randominfo/")
from .Date_Time import Date_Time
from .Person_Name import Person_Name


__title__ = 'randominfo'
__version__ = '0.1'
__author__ = 'Bhuvan Gandhi'
__license__ = 'MIT'

try:
    pass
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fileName = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    if exc_type == TypeError:
        print(fileName + ": " + "Invalid argument list. - line-" + str(exc_tb.tb_lineno))
    else:
        print(e)


'''REFERENCE:
http://www.first-names-meanings.com/country-indian-names.html
https://www.familyeducation.com/baby-names/browse-origin/surname/indian
'''