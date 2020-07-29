import json
import requests
import re
import csv
import os
from os.path import  abspath
import pandas as pd
from commons.post_data import srp_headers
from commons.post_data import srp_post_data
from commons.post_data import dp_header
from commons.post_data import dp_post_data

input_file_dir = abspath("../commons")
file_name = os.path.join(input_file_dir, 'example_2.xlsx')
file_csv_name = os.path.join(input_file_dir, 'employee_file_2.csv')

class BookingScraper:
    def __init__(self, json_url):
        self.json_url = json_url

    def get_booking_response(self):
        try:
            page_no = 1
            url = "https://www.trip.com/hotels/list?city=1&countryId=1&checkin=2020/11/18&checkout=2020/11/25&optionId=1&optionType=City&display=Beijing&crn=1&adult=2&children=0&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=1"
            response = requests.post(self.json_url, data= json.dumps(srp_post_data(page_no,url)), headers=srp_headers(url))
            print("Getting Response - ",format(response.status_code))
            if response.status_code == 200:
                data_json = response.json()
                total_list_count = data_json['Response']['resultTitle']
                print("Total Listing count - ",format(total_list_count))
                expected_count = ''.join(re.findall(r'[0-9]+', total_list_count))
                print("Expected count - ",format(expected_count))
                page_start = 0
                write_headers = True
                while int(expected_count) > page_start:
                    response = requests.post(self.json_url, data=json.dumps(srp_post_data(page_no,url)), headers=srp_headers(url))
                    data_json = response.json()
                    data_listing_size = int(len(data_json['Response']['hotelList']['list']))
                    print(data_listing_size)
                    all_data = self.scraper_data(data_json['Response']['hotelList']['list'])
                    print(all_data)
                    # print("Here is your post{}-{}-{}".format(file_csv_name,all_data,write_headers))
                    self.write_to_csv(file_csv_name,all_data,write_headers=write_headers)
                    read_file = pd.read_csv(file_csv_name)
                    read_file.to_excel(file_name, index=None, header=True)
                    write_headers = False
                    print("Inventory fetch page_no - {}, listings_count - {}, fetched {}".format(page_no,expected_count,page_start+data_listing_size))
                    page_no = page_no + 1
                    page_start = page_start + data_listing_size
                    if page_start >= int(expected_count):
                        break
            else:
                print(response)
                return None
        except:
            return None

    def write_to_csv(self, file_csv_name, dump_info, write_headers=True):
        print("Here is your post{}-{}-{}".format(file_csv_name, dump_info, write_headers))
        keys = dump_info[0].keys()
        with open(file_csv_name, 'a+') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            if write_headers: dict_writer.writeheader()
            dict_writer.writerows(dump_info)

    def scraper_data(self,data_listing):
        lst = []
        data_listing_all_size = int(len(data_listing))
        count = 0
        while data_listing_all_size > count:
            more_info_url = data_listing[count]['base']['bookUrl']
            hotelId = data_listing[count]['base']['hotelId']
            hotelUuidKey = data_listing[count]['trace']['hoteluniquekey']
            if ('price' in data_listing[count]['money']) :
                min_price = data_listing[count]['money']['price']
            elif ('soldOut' in data_listing[count]['money']):
                data_listing[count]['money']['soldOut'] = 0
                min_price = data_listing[count]['money']['soldOut']
            mi_json_url = 'https://www.trip.com/restapi/soa2/16709/json/rateplan?testab=881596a7bd36bc8d299881a9539379e3044b300b90b0c189bcb9191d08e11bb1'
            response = requests.post(mi_json_url, data=json.dumps(dp_post_data(min_price,hotelId,hotelUuidKey)), headers=dp_header(more_info_url))
            resp = response.json()
            hotel_name = data_listing[count]['base']['hotelName']
            rating = data_listing[count]['score']['number']

            if ('priceNote' in data_listing[count]['money']):
                price = data_listing[count]['money']['priceNote']
            elif ('priceNote' not in data_listing[count]['money']):
                price = "soldOut"

            if ('note' in data_listing[count]['facility']):
                amenities = '|'.join(
                    list(map(lambda x: x['name'], data_listing[count]['facility']['list'])))
            elif ('note' not in data_listing[count]['facility']):
                amenities = "Notavailable"

            if ('baseRooms' in resp['Response']):
                for x in resp['Response']['baseRooms']:
                    for y in x["saleRoom"]:
                       if y["promotion"] != []:
                           for z in y["promotion"]:
                                if "Today's Lowest Price!" in z["text"]:
                                 bed = y['bed']['contentList'][0]
            elif ('baseRooms' not in resp['Response']):
                bed = "Notavailable"

            # amenities = '|'.join(list(map(lambda x: x['content'], resp['Response']['baseRooms'][0]['saleRoom'][0]['facility'])))
            if ('baseRooms' in resp['Response']):
                for x in resp['Response']['baseRooms']:
                    for y in x["saleRoom"]:
                        if y["promotion"] != []:
                            for z in y["promotion"]:
                                if "Today's Lowest Price!" in z["text"]:
                                    room_type = x["baseRoom"]["roomName"]
            elif ('baseRooms' not in resp['Response']):
                room_type = "Notavailable"

            print("hotel_name - {}, rating - {}, price - {}, room_type - {}, bed - {}, amenities - {}".format(hotel_name, rating, price, room_type, bed, amenities))
            hsh  = {"hotel_name":hotel_name,"rating":rating,"price":price,"room_type":room_type,"bed":bed,"amenities":amenities}
            lst.append(hsh)
            count = count + 1
        return lst

        # Start from the first cell. Rows and
        # columns are zero indexed.

if __name__ == "__main__":
    obj = BookingScraper('https://www.trip.com/restapi/soa2/16709/json/HotelSearch?testab=40265e0f06501d8aa1d4f1655bc537e5b1068af017500813babafcf37132a520')
    obj.get_booking_response()