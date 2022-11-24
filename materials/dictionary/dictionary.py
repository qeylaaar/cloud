planet = {
    'name' : 'Earth',
    'moons' : 1
}
print(planet.get('name'))

# planet['name'] is identical to using planet.get('name')
print(planet['name'])

# Displays Earth
wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError
planet['name'] = 'Makemake'

# name is now set to Makemake

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

# delete & add
planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

# complex data type

# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

# Output: Jupiter polar diameter: 133709
