
usernames = ['grant', 'justine', 'cody', 'admin']
# 'grant', 'justine', 'cody', 'admin'

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello ' + username + ', would you like a status report?')
        else:
            print('Welcome ' + username)
else:
    print('We need more users!')

