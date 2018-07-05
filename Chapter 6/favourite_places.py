# 6.9 favourite places

favourite_places = {
    'jaden' : ['japan', 'china', 'europe'],
    'shawn' :['china', 'europe'],
    'kon' : ['new york', 'dubai'],
    }

for name, places in favourite_places.items():
    print(name.title() + "'s favourite places are:")
    for place in places:
        print("\t" + place)

