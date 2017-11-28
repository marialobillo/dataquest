planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []
for name in planet_names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)
