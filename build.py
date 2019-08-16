import sys

# load and env file
file = open("variables.env", "r")
data = file.read().splitlines()

# parse personal data
personal = {}

for line in data:
    pair = line.split('=')
    if len(pair) == 2:
        if len(pair[1].strip()) == 0:
            print('ERROR: ' + pair[0] + ' was not specified')
            sys.exit(1)
        key = "{" + pair[0] + "}"
        personal[key] = pair[1].strip()
if len(personal) != 6:
    print('ERROR: Not enough or too many variables in .env file')
    sys.exit(1)

file.close()

# load template 
file = open("template.html", "r")
data = file.read()



for key, value in personal.items():
    data = data.replace(key, value)



f = open("signature.html","w+")
f.write(data)
f.close()

print('Successfully generated signature')