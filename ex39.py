states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-'*10)
print('NY States has: {}'.format(cities['NY']))
print('OR States has: {}'.format(cities['OR']))

# print out some states
print('-'*10)
print("Michigan's Abbreviation is {}".format(states['Michigan']))
print("Florida's Abbreviation is {}".format(states['Florida']))

# do it by using the state then cities dict
print('-'*10)
print("Michigan has {}".format(cities[states['Michigan']]))
print("Florida has {}".format(cities[states['Florida']]))

# print every state abbreviation
# loop through a state
print('-'*10)
for state, abbrev in states.items():
    print("{} is abbreviated as {}".format(state, abbrev))

# now do both at the same time
print('-'*10)
for state, abbrev in states.items():
    print("{} is abbreviated as {} and has city {}".format(state, abbrev, cities[abbrev]))

# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state : 
    print("Sorry, No Texas")

# get a city with default value.
city = cities.get('Tx', "Does not exit")
print("The city for the state 'TX' is {}".format(city))
