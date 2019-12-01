### Assignment 4 - Question 1 ###
person = {
    'first_name': 'Jaweria',
    'last_name': 'Abbas',
    'age': 30,
    'city': 'Karachi',
    }

person['qualification'] = 'Biomedical Engineer'
print(person['qualification'])
print(person)
person.update(qualification = 'Masters in Mechatronics')
print(person)
del person['qualification']
print(person)

### Assignment 4 - Question 2 ###
cities = {
    'Lahore': {
        'country': 'Pakistan',
        'population': 15000000,
        'nearby building': 'Minar e Pakistan',
        },
    'Istabul': {
        'country': 'turkey',
        'population': 18000000,
        'nearby building': 'Isbank Tower',
        },
    'Cape Town': {
        'country': 'South Africa',
        'population': 9800000,
        'nearby building': 'Koopmans-de Wet House',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    river = city_info['nearby building'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + building + " building is nearby.")


### Assignment 4 - Question 3 ###
prompt = "What's Your Age?"
prompt += "\nPlease Enter Your Age to Get the Ticket. "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")

favorite_book('The Holy Quran')

# This is a guess the number game.

### Assignment 4 - Question 5 ###
import random
guessesTaken = 0
print('Please tell your name')
myName = input()
number = random.randint(1, 30)
print('Well, ' + myName + ', Guess a number between 1 and 30.')
while guessesTaken < 3:
        print('What is the number.') 
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
        if guess < number:
            print('The Number is bigger.') 
        if guess > number:
            print('The Number is lower.')
        if guess == number:
            break
        if guess == number:
            guessesTaken = str(guessesTaken)
            print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
            if guess != number:
                number = str(number)
            print('Nope. The number was ' + number)