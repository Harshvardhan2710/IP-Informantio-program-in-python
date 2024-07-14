from requests import *

try:
	wa = "https://ipinfo.io/"
	res = get(wa)
	print(res)
	print(res.status_code)

	data = res.json()
	print(data)

	city_name = data['city']
	print(city_name)
		
	state_name = data['region']
	print(state_name)
	
	loc = data['loc']
	ll = loc.split(",")
	lat = ll[0]
	lon = ll[1]
	print("latitude", lat)
	print("longitude", lon)

except Exception as e:
	print("issue ", e)
