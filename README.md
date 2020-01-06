# Randominfo #
Random data generator for IDs, names, emails, passwords, dates, numbers, addresses, images, OTPs etc. This package includes data like names and addresses regarding Indian regions.

## Installation ##
To install package from python-pip:

`$ pip install randominfo`

## Features ##
This package provides dummy data like...

* **Name**: First name, last name and full name.
* **Gender**: Male or female.
* **Birthdate**: Date generation based on given age range.
* **Email**: Email address generation.
* **Password**: Password generation based on specified pattern.
* **Phone**: Mobile number generation based on given country code.
* **Address**: Full address generation including street address, landmark, area, state, country, country and pincode of India.
* **Unique ID**: ID generator based on specific pre-fix value or next value based on given value or with random values.
* **Profile Image**: profile image generator based on specified gender or alphabetic character.
* **Hobbies**: random hobbies selector.
* **OTPs**: OTP generation with different types like only digits, only alphabets or digits and alphabets both.
* **Other**: random int or float number generation based on specific range or any value.

## Functions ##
#### `get_first_name(gender = None)`: ####
* Desc.: Returns the first name and the gender.
* Argument value: gender = 'male' or 'female'.
* Return value: String value.

#### `get_last_name()`: ####
* Desc.: Returns the last name.
* Return value: String value.

#### `get_full_name(gender = None)`: ####
* Desc.: Returns the first and last name.
* Arguments: gender = 'male' or 'female'.
* Return value: String value (Combined first name and last name).

#### `get_gender(first_name)`: ####
* Desc.: Returns the gender from the first name.
* Arguments: first_name for selecting gender based on first name.
* Return value: String value - 'male' or 'female'.

#### `get_country(first_name = None)`: ####
* Desc.: Returns the country from the first name.
* Arguments: first_name for selecting country based on first name. If first name is not specified then it will return random country name.
* Return value: String value.

#### `get_birthdate(startAge = None, endAge = None, _format = '%d %b, %Y')`: ####
* Desc.: Generates random date or the date specified between years from the starting age or ending age.
* Arguments:
    * startAge: The starting age for year.
    * endAge: The ending age for year.
    * _format: Specifies the format of the date.
* Return value: Date as string.

#### `get_otp(length = 6, digit = True, alpha = True, lowercase = True, uppercase = True)`: ####
* Desc.: Generates one time password or random value in specified length of characters.
* Arguments:
    * onlyDigits: Allow only digits in random string.
    * onlyAlpha: Allow only alphabets in random string.
    * lowercase: Allow only lowercase alphabets in random string.
    * uppercase: Allow only uppercase alphabets in random string.
* Return value: String value.

#### `get_formatted_datetime(outFormat, strDate, strFormat = "%d-%m-%Y %H:%M:%S")`: ####
* Desc.: Convert string date into datetime object in specified format.
* Arguments:
	* outFormat: A format in which we want output.
    * strDate: A date which we want to convert.
    * _format: A date format of which we have specified in strDate argument.
* Return value: Datetime object in specified format.

#### `get_email(Person = None)`: ####
* Desc.: Random email generator.
* Arguments: Person: Person object. Function will generate a random email address related to specified person.
* Return value: Email address as string.

#### `random_password(length = 8, special_chars = True, digits = True)`: ####
* Desc.: Generates random password of specified length and it includes special characters like !, @, #, $, %, ^, &, * and digits.
* Arguments:
    * length: The length of password.
    * special_chars: True if we want to include special characters in password.
    * digits: True if we want to include digits in password.
* Return value: Password as string.

#### `get_alphabet_profile_img(char, filePath, imgName, charColor = None, bgColor = None)`: ####
* Desc.: Generates image of specified character with background color and it stores on specified file path with given file name.
* Arguments:
    * char: A character for writing in image.
    * filePath: A path where the image will store.
    * imgName: A name of image file.
    * charColor: Character color name.
    * bgColor: Background color name.
* Return value: A full path of stored image.

#### `get_face_profile_img(filePath, imgName, gender = None)`: ####
* Desc.: Generates random person's image.
* Arguments:
    * filePath: A full path from root to file name. Specifies where to store image.
    * gender: To generates image from specified gender's person. 'male' or 'female'.
* Return value: A full path of stored image.

#### `get_today(_format = "%d-%m-%Y %H:%M:%S")`: ####
* Desc.: Generates today's datetime in specified format.
* Arguments:
    * _format: A format for generating today's datetime.
* Return value: String value.

#### `get_datetime(tstamp = None, _format = '%d %b, %Y')`: ####
* Desc.: Returns the random or timestamp datetime in specified format.
* Arguments:
    * tstamp: Generates date based on specified timestamp.
    * _format: Specifies the format of the date.
* Return value: Date as string.

#### `get_address()`: ####
* Desc.: Generates random address with street name, landmark, area, city, state and pincode.
* Return value: `[street, landmark, area, city, state, pincode]` | Type: List.

#### `get_hobbies()`: ####
* Desc.: Generates minimum 1 and maximum 6 hobbies.
* Return value: `[hobby1, hobby2, ..., hobby6]` | Type: List.

## Objects ##
#### `Person()`: ####
* Desc.: An object which holds information related to a person. Information like first name, last name, gender, birthdate, phone number, email address, password, country, hobbies and address.
* Variables:
    * `Person.first_name`: Returns the first name of a person.
    * `Person.last_name`: Returns the last name of a person.
	* `Person.full_name`: Returns the full name of a person.
    * `Person.gender`: Returns the gender of a person.
    * `Person.birthdate`: Returns the birthdate of a person.
    * `Person.phone`: Returns the phone number of a person.
    * `Person.email`: Returns the email address of a person.
    * `Person.password`: Returns the password of a person.
    * `Person.country`: Returns the country of a person.
    * `Person.hobbies`: Returns the hobbies of a person.
    * `Person.address`: Returns the address of a person.
    * `Person.custom_attr`: Returns the list of custom attributes specified for a person.
* Functions:
    * `Person.set_attr(attr_name, value = None)`:
        * Desc.: Set the custom attribute of a person.
        * Arguments.:
            * attr_name: Attribute name for a person.
            * value: Value for specified attribute.
        * Return value: Attribute `attr_name` is added.
    * `Person.get_attr(attr_name)`:
        * Desc.: Returns the value of attribute specified for a person.
        * Arguments.:
            * attr_name: Attribute name of a person.
        * Return value: Attribute value as string.
    * `Person.get_details()`: Returns all the details of a person. Type: Dictionary.

## Reference ##
http://www.first-names-meanings.com/country-indian-names.html

https://www.familyeducation.com/baby-names/browse-origin/surname/indian

https://thispersondoesnotexist.com/

https://en.wikipedia.org/wiki/List_of_hobbies
