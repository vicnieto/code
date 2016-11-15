import requests
import json

token = "47098a3d5718c1178509ed5d7f1efde2"

githuburl = "https://github.com/vicnieto/git_code2040"

jsonObj = {"token":token, "github":"https://github.com/vicnieto/git_code2040"}

instructions = requests.post("http://challenge.code2040.org/api/reverse", json=jsonObj)


# print(instructions.text)

# instruct is equal to the word given by api 
instruct = instructions.text

def reverse_word(word):
	# j is index of last letter in word
	j = len(word) - 1
	# empty string used to create new reversed word
	result = ""
	while j > -1:
		# add each letter from word starting with last letter and moving from right to left
		result += word[j]
		j--
	return result

# answer = reverse_word(instruct)

# print(answer)

jsonObj2 = {"token":token, "string":answer}

instructions2 = requests.post("http://challenge.code2040.org/api/reverse/validate", json=jsonObj2)

# print(instructions2.text)
