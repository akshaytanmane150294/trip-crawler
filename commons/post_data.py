


def srp_headers(url):
    header = {'authority': 'www.trip.com', 'accept': 'application/json', 'p': '96457056205',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
               'content-type': 'application/json;charset=UTF-8', 'origin': 'https://www.trip.com',
               'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors',
               'referer': url,
               'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
    return header

def srp_post_data(page_no,url):
    post_data = {
	      "seqid": "7daacb343a904f8fb552521d5851f45e",
	       "deduplication": [],
	    "filterCondition": {
		"star": [],
		"rate": "",
		"priceRange": {
			"lowPrice": 0,
			"highPrice": -1
		},
		"priceType": 0,
		"breakfast": [],
		"payType": [],
		"bedType": [],
		"bookPolicy": [],
		"bookable": [],
		"discount": [],
		"zone": [],
		"landmark": [],
		"metro": [],
		"airportTrainstation": [],
		"location": [],
		"cityId": [],
		"amenty": [],
		"category": [],
		"feature": [],
		"brand": [],
		"popularFilters": [],
		"hotArea": []
	},
	"searchCondition": {
		"sortType": "AppointRank",
		"adult": 2,
		"child": 0,
		"age": "",
		"pageNo": page_no,
		"optionType": "City",
		"optionId": "1",
		"lat": 0,
		"destination": "",
		"keyword": "",
		"cityName": "Beijing",
		"lng": 0,
		"cityId": 1,
		"checkIn": "2020-11-18",
		"checkOut": "2020-11-25",
		"roomNum": 1,
		"mapType": "gg",
		"travelPurpose": 0,
		"countryId": 1,
		"url": url,
		"pageSize": 10,
		"timeOffset": 28800,
		"radius": 0,
		"directSearch": 0,
		"signInHotelId": 0,
		"signInType": 0
	},
	"meta": {
		"fgt": "",
		"hotelId": "",
		"priceToleranceData": "",
		"priceToleranceDataValidationCode": "",
		"mpRoom": [],
		"hotelUniqueKey": "",
		"shoppingid": "",
		"minPrice": "",
		"minCurr": ""
	},
	"queryTag": "NORMAL",
	"Qid": "397163124417",
	"Head": {
		"Locale": "en-XX",
		"Currency": "USD",
		"AID": "",
		"SID": "",
		"ClientID": "1595654660546.1jiyi3",
		"OUID": "",
		"TimeZone": "5.5",
		"PageID": "10320668148",
		"HotelExtension": {
			"WebpSupport": "true",
			"Qid": "",
			"hasAidInUrl": "false",
			"group": "TRIP",
			"PID": "84e110dd-4984-4b7f-bf74-bb5ffd20e79f",
			"hotelUuidKey": "83dJ1drlCYQ9inQjCJ5BJ6fwlJL8Y5TjqNjSUIsJHTYAfWhpvGmxAJDfKTarqGv0LeTJD4R7NW8sJ4Gw7JU9IaVJm8rLTigFvbOY3pRzPiV4r3JuLvpgvCXEmBRsziqXY3LYahJqJ3JPAeDaYHpJNdvM7YqETQYSAiosRBNJMgRl0wBJXJb1w9DKA5R7CjNgWfbiZEAmJb6ylzraEPTJu0Ia6vp3xSXYoGJngxpUxu4JsOjCPRzLiXHwoAylFIfnigEmByVoj0ORaTvfSWLsizmJhaiAEsZrFpjVGR6QW4lwMBi08xNzxauwC6wAuwTzIFSY41RC0wPHiGlYpbjBqJDUEf9Yd5YuXxsXj7Bj3LxQXIabi5lYNsRAVKnZR5hj6DWhli0dYGXw0Prp7v40j95wMDrlovzAKVzw1fKqQROTjdaWfpiPEOqJs7yX4r5EQuiZOYbGi7qK86is0RFSxGDxn8xAOxQzwdow0zw73I4gY1dRLTwhniZHYFljQ6JXzEM4w8BroBvf8juVw5lrhpvUZK45IGZw9HiDVYFpxd1iCEZlwluIUuY5FiXaJsqiMGxb0xzmxXzxL4wgNwQawqUINSY6SRCgwo8igaYAXj04JHnEfUYTPYFMJU5wafR6fIXaj44KHnwGswlVwu5IdzY19RMCwZpiC7YXBjmQJ36EdfYo5YOfwMoJH4wBzRAgIGBjBJZlJTUjhUjhHjG0iAJnOiabyQSvnMvMLImpJshiMTyGJB8WQUyd5vBbyp6RG7yQLwNMr1VvFqI0Gj9gJbCjdJ15J8drZpv9qyTGwUfJfdRQhJNZr4VIGZyHAICOyN8RVqyXpvqmIpZwXJ7SWZoyCnv1ayVpR4QyBFwMaRbzRFSIBuyGPwsoRHJ7SioNRCPvNd",
			"hotelUuid": "P7fSp2TA7lqlbcqu04"
		},
		"Frontend": {
			"vid": "1595654660546.1jiyi3",
			"sessionID": 1,
			"pvid": 2
		},
		"P": "50614627421",
		"Device": "PC",
		"Version": "0"
	}
}
    return post_data

def dp_header(more_info_url):
	dp_header =  {'Authority':'www.trip.com',
 'Accept':'application/json',
 'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
 'Content-type':'application/json',
 'Origin':'https://www.trip.com',
 'Sec-fetch-site':'same-origin',
 'Sec-fetch-mode':'cors',
 'Referer':more_info_url,
 'Accept-encoding':'gzip, deflate, br',
 'Accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
	return dp_header


def dp_post_data(min_price,hotelId,hotelUuidKey):
	dp_post_data = {
	"checkIn": "2020-11-18",
	"checkOut": "2020-11-25",
	"priceType": "0",
	"adult": 2,
	"popularFacilityType": "",
	"fgt": "",
	"hotelUniqueKey": "H4sIAAAAAAAAAOO6y8TFK8Fk8B8GGIWYOBiljjNxrL__gNngP6sjAwgsSHDwBDP2THAI4JnEKMmZBgJyyQ6CZ88AgU6cgxMrR7OgBMskRmlMOQ1GvLJMeGWZ8cqy4JVlxSvLBpWdwbjsU9QKRsaNjGA_NiQ67GBkOsEovIDpbmf4LiZWjunlEiyHgPRxRgmmU0wMl5gYbjExPGJieMXE8ImJ4RcTxJgmZoYuZoZJzKwcc5kkWGYxMyxiZhBiAYWjlIJloomRoWVyqqlxormJkbmBhXGqhUVSappZYlJSWlqSuQKTxsIp73-wGjFYMUsxunmwB7EZWTpaWjpFyXAxO_tFCoJdxvDBXoo5NNhFMeCPRPF1IRmHJNbUPN2IiIz1rAWMXYxMAoyTGDnAMQd0_QxGRgB3PuH-3gEAAA((",
	"child": 0,
	"roomNum": 1,
	"masterHotelId": hotelId,
	"age": "",
	"cityId": "1",
	"minCurr": "USD",
	"minPrice": min_price,
	"hotel": str(hotelId),
    "versionControl": [{"key": "RoomCardVersionB", "value": "F"}],
	"signInRoomKey": "",
	"signInType": 0,
	"Head": {
		"Locale": "en-XX",
		"Currency": "USD",
		"AID": "",
		"SID": "",
		"ClientID": "1595654660546.1jiyi3",
		"OUID": "",
		"TimeZone": "5.5",
		"PageID": "10320668147",
		"HotelExtension": {
			"WebpSupport": "true",
			"Qid": "",
			"hasAidInUrl": "false",
			"group": "TRIP",
			"PID": "98ade6fe-eaff-486a-9ceb-0f76525ada17",
			"hotelUuidKey": hotelUuidKey,
			"hotelUuid": "P7fSp2TA7lqlbcqu04"
		},
		"Frontend": {
			"vid": "1595654660546.1jiyi3",
			"sessionID": 5,
			"pvid": 12
		},
		"P": "54632620979",
		"Device": "PC",
		"Version": "0"
	}
}
	return dp_post_data

