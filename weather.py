import forecastio
from geopy.geocoders import Nominatim



# latitude = 37.9101
# longitude= -122.0652

# forecast = forecastio.load_forecast(api_key, lat, lng).currently()

# print("{} and {}°".format(forecast.summary, forecast.temperature))


#get_weather(latitude, longitude, api_key):

# def get_weather(latitude, longitude, api_key):
#     forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
#     return "{} and {}°".format(forecast.summary, forecast.temperature)
    
# def get_location(city):
#     geolocator = Nominatim()
#     location = geolocator.geocode(city)
#     latitude = location.latitude
#     longitude = location.longitude
#     return coordinates = [latitude, longitude]

def get_weather(city):
    api_key = "97ad36d4370334b97c75fe673afbe26b"
    geolocator = Nominatim()
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    return "{} and {}° in {}".format(forecast.summary, forecast.temperature, city)


