import requests as request

class bigdata:
    def apicall(self):
        response = request.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
        print(response.status_code)
        jsondata = response.json()
        print(jsondata)
        for listdata in jsondata:
            for key, value in listdata.items():
                if key == "category":
                    print(value)


obj = bigdata()
obj.apicall()