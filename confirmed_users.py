# Start with users that need to be verified, and a empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace', 'Dominic', 'Dada', 'Mom']
confirmed_users = []

# Verify each user untill there are no more unconfirmed users. Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifing user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been Verified:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
