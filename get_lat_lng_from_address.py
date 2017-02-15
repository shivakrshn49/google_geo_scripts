import csv
import sys
import requests

api_key = "AIzaSyDcL0tByE0VjR1crkRb1y3H2inldoXH2QA"

def get_lat_lng_from_google(address):
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        return (latitude, longitude)

input_file = open(sys.argv[1], 'rt')
output_file = open("/Users/shivakrishna/Desktop/output.csv", 'wt')
try:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    counter = 0
    for row in reader:
        if counter == 0:
            row.append('Latitude')
            row.append('Longtitude')
            writer.writerow( tuple(row) )
        else:
            address_list = row[:3]
            address_list.reverse()
            address = ' '.join(address_list)
            try:
                lat, lng = get_lat_lng_from_google(address)
                row.append(lat)
                row.append(lng)
            except Exception as e:
                pass
            writer.writerow( tuple(row) )

        counter += 1
finally:
    input_file.close()
    output_file.close()
