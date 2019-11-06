import requests as request

class jsonSchemaTest():
    def apiTest(self):
        response = request.get("http://json-schema.org/draft-04/schema#")
        #print(response.status_code)
        jsonData = response.json()
        #print(jsonData)
        for key, value in jsonData.items():
            if key == "dependencies":
                print(value)


obj = jsonSchemaTest()
obj.apiTest()