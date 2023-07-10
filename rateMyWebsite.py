data = {}

keys = ['the website name','the URL','your description','the star rating out of 5']

for key in keys:
  data[key] = input(f"\033[33mPlease, tell me {key} > \033[32m")

print()
print ('\033[35m🌟Website Rating🌟')

for key, value in data.items():
  print (f"\033[35m{key.title()}: {value}")