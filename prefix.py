import requests
import json

token = "47098a3d5718c1178509ed5d7f1efde2"

githuburl = "https://github.com/vicnieto/git_code2040"

jsonObj = {"token":token, "github":githuburl}

instructions = requests.post("http://challenge.code2040.org/api/prefix", json=jsonObj)

instructions = instructions.text

# gets dictionary object from instructions
instruct = json.loads(instructions)

def refine_array(d):
    # empty list where words without prefix will be added
    result = []
    prefix = d['prefix']
    # goes through words in array's value
    for s in d['array']:
        # adds words that don't have prefix to result
        if prefix not in s:
            result.append(s)
    return result

post_array = refine_array(instruct)

answer = {"token":token, "array":post_array}

postAnswer = requests.post("http://challenge.code2040.org/api/prefix/validate", json=answer)

# print postAnswer.text

