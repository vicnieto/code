import json 
import requests
# my token
token = "47098a3d5718c1178509ed5d7f1efde2"

# dictionary with my token and github url
jsonObj = {"token":token, "github":"https://github.com/vicnieto/git_code2040"}

# posts json object to registration end point so I could start working on challeng
instructions = requests.post("http://challenge.code2040.org/api/register", json=jsonObj)

# grabs text from instructions
instructions = instructions.text
