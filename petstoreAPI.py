import requests as request

class bigdata:
    def apicall(self):
        response = request.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
        if response.status_code == 200:
            jsondata = response.json()
            print(jsondata)
            for listdata in jsondata:
                for key, value in listdata.items():
                    if key == "category":
                        print(value)
        else:
            print("Call Failed with response code "+str(response.status_code))



obj = bigdata()
obj.apicall()