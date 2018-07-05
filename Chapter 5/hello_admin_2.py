# 5.9 no users 


user = ['alvin','chan','shawn','kon','admin']

if user:
    for username in user:
        if 'admin' in username:
            print('Hello sir, welcome back.\nWould you like to check status report?\n')
        else:
            print('Hello ' + username.title() + ' welcome back.\n')
else:
    print('We need to find some users!')


del user[:]

if user:
    for username in user:
        if 'admin' in username:
            print('Hello sir, welcome back.\nWould you like to check status report?')
        else:
            print('Hello ' + username.title() + ' welcome back.\n')
else:
    print('ERROR: We need to find some users!')
