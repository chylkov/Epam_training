
# coding: utf-8

# In[52]:


def coordinate(location):
    import requests

    url = "https://nominatim.openstreetmap.org/search.php"

    querystring = {"q":location,"polygon_geojson":"1","viewbox":"", "format":"json"}

    response = requests.request("GET", url, params=querystring)
    
    data = response.json()
    
    coordinates = (data[0]['lat'], data[0]['lon'])
    
    return coordinates



def weather(location, *appid):

    import requests

    url = "http://api.openweathermap.org/data/2.5/weather"
    
    lat = coordinate(location)[0]
    lon = coordinate(location)[1]
    
    if len(list(appid)) == 0:
        querystring = {"lat":lat,"lon":lon,"appid":"b4a9d8e16b916107e741f1e84440c660"}
    else:
        querystring = {"lat":lat,"lon":lon,"appid":appid}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    return data['weather'][0]['description']


