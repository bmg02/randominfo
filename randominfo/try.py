from os.path import isdir
from random import choice
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime

def get_alphabet_profile_img(char, filePath, imgName = None, charColor = None, bgColor = None):
	if char.isalpha() and isdir(filePath):
		if charColor != None:
			if not charColor.isalpha():
				raise CustomError("Character color must be a name of color.")
		if bgColor != None:
			if not bgColor.isalpha():
				raise CustomError("Background color must be a name of color.")
		if imgName != None:
			if not imgName.isalpha():
				raise CustomError("Image name must be a str.")
		char = char[:1].upper()
		if bgColor == None:
			colors = ['red', 'green', 'royalblue', 'violet', 'pink', 'indigo', 'grey', 'yellowgreen', 'teal']
			bgColor = choice(colors)
		if charColor == None:
			charColor = (40, 40, 40)
		img = Image.new('RGB', (512, 512), color = bgColor)
		d = ImageDraw.Draw(img)
		font = ImageFont.truetype("Candara.ttf", 280)
		d.text((170,140), char, fill=charColor, font = font)
		if imgName == None:
			imgName = char + "_" + datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(':', '-')
		filePath = filePath + "\\" + imgName + ".jpg"
		img.save(filePath)
	else:
		raise CustomError("Type mismatch in either char or filePath or charColor or bgColor.")
	return filePath

get_alphabet_profile_img("B", "B:", "dsf", "olive", "white")