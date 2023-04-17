import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

myNumber = phonenumbers.parse("numero du téléphone avec code du pays. Ex: +223", None)

location = geocoder.description_for_number(myNumber, "fr")

operators = carrier.name_for_number(myNumber, "fr")

key = "bcbcda4e97f346d1a515f8a403650ba9"

__geocoder = OpenCageGeocode(key)
endroit = str(location)
result = __geocoder.geocode(endroit)

latitude = result[0]["geometry"]["lat"]
longitude = result[0]["geometry"]["lng"]

_map = folium.Map(location=[latitude, longitude], zoom_start=12)
folium.Marker([latitude, longitude], popup=location).add_to(_map)

_map.save("index.html")

# print(myNumber)
# print(location)
# print(result)
# print(operators)
# print(latitude, longitude)