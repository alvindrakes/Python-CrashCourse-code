# 8.13 user_profile

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
                characteristics = 'Love to smile, serious when working, want to succeed badly',
                major = 'Computer science',
                dream = 'Change the world by contributing to it, help people improve their lives')

print(user_profile)