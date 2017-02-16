import csv
import sys
import requests

api_key = "AIzaSyDcL0tByE0VjR1crkRb1y3H2inldoXH2QA"

def get_address_from_lat_lng(latitude, longitude):
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}&key={2}'.format(latitude, longitude, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        address = api_response_dict['results'][0]['formatted_address']
        return address

input_file = open(sys.argv[1], 'rt')
output_file = open("/Users/shivakrishna/Downloads/Nevada/lower-assembly-output.csv", 'wt')
try:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    counter = 0
    for row in reader:
        if counter == 0:
            row.insert(0, 'Name')
            writer.writerow( tuple(row) )
        else:
            latitude = row[1]
            longitude = row[0]
            try:
                address = get_address_from_lat_lng(latitude, longitude)
                row.insert(0, address)
            except Exception as e:
                pass
            writer.writerow( tuple(row) )

        counter += 1
finally:
    input_file.close()
    output_file.close()
