from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random


__title__ = 'randominfo'
__version__ = '0.1'
__author__ = 'Bhuvan Gandhi'
__license__ = 'MIT'

#full_path = lambda filename: abspath(join(dirname(__file__), filename))

def get_full_name(gender = None, country = None, first = False, last = False):
    if gender.lower() == "male":
        pass
    elif gender.lower() == "female":
        pass
    else:
        raise ValueError("Only 'male' and 'female' are supported as gender")

def get_first_name(gender = None, country = None):
    get_full_name(gender,  country, first = True)

def get_last_name(country = None):
    get_full_name(country, last = True)






'''REFERENCE:
http://www.first-names-meanings.com/country-indian-names.html
https://www.familyeducation.com/baby-names/browse-origin/surname/indian
'''