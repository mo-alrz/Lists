# "Saturn" is missing from the planetList
# Insert it into the correct position
# Create a method called "put_saturn()" which has a list parameter and returns the correct list

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]


def put_sturn():
    planet_list.insert(planet_list.index("Uranus"), 'Saturn')
    return planet_list


print(put_sturn())
