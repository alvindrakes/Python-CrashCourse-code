# 5.8 hello admin 

user = ['alvin','chan','shawn','kon','admin']

for username in user:
    if 'admin' in username:
        print('Hello sir, welcome back.\nWould you like to check status report?')
    else:
        print('Hello ' + username.title() + ' welcome back.\n')