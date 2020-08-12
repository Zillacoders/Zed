#ex41
states = {
    'Hyderabad' : 'HYD',
    'Mumbai': 'BOM',
    'Kolkata': 'CCU',
    'Delhi': 'DL',
    'Chennai': "CH"
}

# create a basic set of states and some cities in them.
cities = {
    'HYD': 'Hyderabad',
    'BOM': 'Mumbai',
    'CH': 'Chennai'
}

#add some more cities
cities['DL'] = 'Delhi'
cities['CCU'] = 'Kolkata'

#print some more cities
print('-' * 10)
print("HYD State has: ", cities['HYD'])
print("DL State has: ", cities['DL'])

# print some states
print('-' * 10)
print("Kolkata's abbreviation is:", states['Kolkata'])
print("Chennai's abbreviation is: ", states['Chennai'])

# do it by using the state then cities dict
print('-' * 10)
print("Mumbai has: ", cities[states['Mumbai']])
print("Hyderabad has: ", cities[states['Hyderabad']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do the both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbrevaition by state that might ot be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city wit ha ddefault value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

list(states)
