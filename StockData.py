import requests as request


class apiTest:
    def apiCaller(self, stockname):
        response = request.get("https://appfeeds.moneycontrol.com/jsonapi/market/marketmap&format=&type=0&ind_id=9")
        print("Call to API is "+str(response.status_code))
        jasonData = response.json()
        for x, y in jasonData.items():  # to fetch the first dict items
            for listdata in y:  # to fetch the list inside dict items
                for key, value in listdata.items():  # to fetch dict inside list
                    if value == stockname:
                        ltp = str(listdata["lastvalue"])
                        print("The price of "+str(stockname)+" is "+  str(ltp))


obj = apiTest()
obj.apiCaller("Asian Paints")
obj.apiCaller("Axis Bank")
obj.apiCaller("Bharti Airtel")
obj.apiCaller("GAIL")
obj.apiCaller("HCL Tech")
obj.apiCaller("Tech Mahindra")
obj.apiCaller("Hindalco")
obj.apiCaller("Nestle")
