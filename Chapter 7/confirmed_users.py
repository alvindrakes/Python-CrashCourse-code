# start with a list of unconfirmed users
# then have an empty list that will hold the confirmed users

unconfirmed_users = ['alvin', 'jaden', 'kon']
confirmed_users =[]

# verify until there's no more unconfirmed users, move all confirmed to the confirmed list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Veryfying user: " + current_user.title())
    confirmed_users.append(current_user)

#display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())