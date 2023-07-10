info = {}
keys = ['name', 'type', 'special move', 'starting HP', 'starting MP']


print ("👾 PokéBeast - The Non-Copyright Generic Beast Battle Game")

for key in keys:
  info[key] = input(f"\033[35mInput your beast\'s {key} > \033[36m")

natures = ['water','fire','earth','air']
colors = {'water':'\033[34m',
       'fire':'\033[31m',
       'earth':'\033[32m',
       'air':'\033[37m',
       'else':'\033[33m'}
if info['type'].strip().lower() in natures:
  nature = type.strip().lower()
else:
  nature = 'else'
color = colors[nature]


print (f"{color} Your beast is called {info['name']}. It is an {info['type']} beast with a special move of {info['special move']}.")
print (f"Starting HP: {info['starting HP']}")
print (f"Starting MP: {info['starting MP']}\033[0m")

