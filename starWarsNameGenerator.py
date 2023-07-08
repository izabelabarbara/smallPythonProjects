print('STAR WARS NAME GENERATOR')

questions = ["Enter your first name: ",
             "Enter your last name: ",
             "Enter your mum's maiden name: ",
             "Enter the city you were born in: "]
answers = []

for i in questions: 
  answers.append(input(i))

part1 = answers[0].strip()[0:3].title()
part2 = answers[1].strip()[0:2].lower()
part3 = answers[2].strip()[0:2].title()
part4 = answers[3].strip()[-3:].lower()

print()
print (f'Yout Star Wars name is {part1}{part2} {part3}{part4}.')
