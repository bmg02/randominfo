from selenium import webdriver
import time
import csv

with open('areas.csv', 'r') as f:
	reader = csv.reader(f.read().splitlines(), delimiter = ',')
	data = [row for row in reader]

#print(data[1][0])
##############
filename = 'areas1'
############

#driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver = webdriver.Firefox(executable_path=r'C:\\Users\\bhuvan_02\\Desktop\\geckodriver.exe')
driver.get('http://www.latlong.net/')

crash = 1
results = []
skipped = []
for i,row in enumerate(data[1:]):
	print (i)
	search = driver.find_element_by_id('place')
	search_term = row[0] + ", " + row[1] + ", " + row[2]
	search.clear()
	try:
		search.send_keys(search_term)
	except:
		print ('Skiped %s' %search_term)
		print (row)
		skipped.append(row)
		continue

	search.submit()
	time.sleep(1)
	try:
		lat = driver.find_element_by_id('latlngspan')
	except:
		alert = driver.switch_to_alert()
		alert.accept()
		driver.switch_to_default_content()
		print ('Couldnt find %s' %search_term)
		print (row)
		skipped.append(row)
		continue

	lat_long = lat.text.strip('() ').split(',')
	lat_long_clean = [float(n) for n in lat_long]

	try:
		driver.navigate().refresh()
	except:
		#with open(filename + 'recovered' + '%i' %crash + '.csv' , "wb") as f:
			#writer = csv.writer(f)
			#writer.writerows(results)
		crash +=1

	print (lat_long_clean)
	r = row
	r.extend(lat_long_clean)
	r.insert(0, i)
	print (r)
	results.append(r)

	#with open(filename + ".csv", "a") as f:
		#writer = csv.writer(f)
		#writer.writerow(r)

print(results)
#with open(filename + "complete.csv" , "wb") as f:
	#writer = csv.writer(f)
	#writer.writerows(results)