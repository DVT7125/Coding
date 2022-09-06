banned_users = ['andrew', 'caroina', 'david']
user = 'andrew'

if user not in banned_users:
    print(f"{user.title()}, you can post a responce if you wish.")
else:
    print(f"{user.title()}, You have been banned. If you think this is a mistake please contact fuzziestdvt@gmail.com.")