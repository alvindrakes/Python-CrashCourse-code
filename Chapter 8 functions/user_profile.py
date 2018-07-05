#using abitraru keyword argument

def build_profile(first, last, **user_info):  #double asterisk enable python to create an empty dictionary 
#and store all name-value pairs in this dictionary

    """Build dictionary on user's info"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Alvin', 'drakes',
                location = 'Malaysia',
                major = 'Computer science')

print(user_profile)