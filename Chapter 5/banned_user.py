banned_user = ['marie', 'katie', 'nigga', 'josh']
user = 'jack'

if user in banned_user:
	print(user.title() + ', you are not allowed to post any comment')
else:
	print(user.title() + ', you can post any comments as you wish')