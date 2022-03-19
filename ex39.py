# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
page_break = '-' * 10
print(page_break)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#Print some states
print(page_break)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print(page_break)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")
	
# print every city in state
print(page_break)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")
	
# now do both at the same time
print(page_break)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}", end=' ')
	print(f"and has city {cities[abbrev]}")
	
# safely get a abbreviation that might not be there
print(page_break)
state = states.get('Texas')

if not state:
	print("Sorry, no Texas.")
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is {city}")
	