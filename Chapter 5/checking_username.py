# 5.10 checking username 

current_users = ['jack', 'jaden', 'kon', 'shawn', 'samuel']

new_users = ['kitty', 'lisa', 'john', 'jaCk', 'jAden']

for user in new_users:
    if user.lower() in current_users:
        print('Username has been taken. Please enter a new username.')
    else:
        print('Username is available.')