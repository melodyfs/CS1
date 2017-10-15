import requests

start_date = '2017-10-21'
end_date = '2017-10-22'
nasa_response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=()&end_date=()&api_key=DEMO_KEY'.format(start_date, end_date))

nasa_response.text
