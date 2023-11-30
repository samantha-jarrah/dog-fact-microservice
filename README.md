# Dog Fact Microservice

*This is a microservice that returns a random dog fact*
---

# Communication Contract
To **REQUEST** data from the microservice:

1. Ensure you have requests installed on local drive
2. Make an HTTP GET request using http://localhost/fact as the URL, saving it in a variable

**Example**

`URL = "http://127.0.0.1:5000/fact"`

`response = requests.get(URL)`

To **RECEIVE** data from the microservice:
1. The response that you saved from the GET request is a JSON object. Call .json() on it and parse the data to extract only the desired fact

`fact = response.json()["data"][0]["attributes"]["body"]`

# UML Sequence Diagram
<img width="1163" alt="image" src="https://github.com/samantha-jarrah/dog-fact-microservice/assets/99986399/20270b5a-8b0a-4834-9af8-e1e6d6be7e99">
