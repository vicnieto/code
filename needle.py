import requests
import json

token = "47098a3d5718c1178509ed5d7f1efde2"

githuburl = "https://github.com/vicnieto/git_code2040"

jsonObj = {"token":token, "github":"https://github.com/vicnieto/git_code2040"}

instructions = requests.post("http://challenge.code2040.org/api/haystack", json=jsonObj)

instructions = instructions.text

# gets dictionary object from instructions

instruct = json.loads(instructions)

# finds needle in haystack array value
def find_needle(dictionary):
# set listx equal to array obtained from using haystack key

	listx = dictionary['haystack']

# iterates through all elements of the list and looks for needle
# and returns index of needle value

	for i in range(len(listx)):
		if(listx[i] == dictionary['needle']):
			return i

index = find_needle(instruct)

answer = {"token":token, "needle":index}

response = requests.post("http://challenge.code2040.org/api/haystack/validate", json=answer)

# print(response.text)
