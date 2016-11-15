import requests
import json
import datetime
from datetime import timedelta, datetime
import iso8601

token = "47098a3d5718c1178509ed5d7f1efde2"

githuburl = "https://github.com/vicnieto/git_code2040"

jsonObj = {"token":token, "github":"https://github.com/vicnieto/git_code2040"}

instructions = requests.post("http://challenge.code2040.org/api/dating", json=jsonObj)

instructions = instructions.text

# gets dictionary object from instructions
instruct = json.loads(instructions)

# print instructions

# creates datetime object using datestamp from given dictionary
datex = iso8601.parse_date(instruct['datestamp'])

# creates timedelta object with seconds equal to interval from given dictionary
sec = timedelta(seconds = instruct['interval'])

# can add datetime and timedelta objects. Creates new date that results
# from adding interval seconds to the given datestamp
new_date = datex + sec

# use strftime to format the new date exactly as the datestamp was formatted
formatted_date = new_date.strftime("%Y-%m-%dT%H:%M:%SZ")

# print(formatted_date)

# submits answer
answer = {"token":token, "datestamp":formatted_date}

response = requests.post("http://challenge.code2040.org/api/dating/validate", json=answer)

# print(response.text)


