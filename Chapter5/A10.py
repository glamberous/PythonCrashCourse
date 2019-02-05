
current_users = ['grant', 'justine', 'cody', 'admin']
# 'grant', 'justine', 'cody', 'admin'
new_users = ['aaron', 'wendy', 'justine', 'juan', 'grant']


#for cur_user in current_users:
#    taken = False
#    for new_user in new_users:
#        if cur_user.lower() == new_user.lower():
#            taken = True
#    if taken:
#        print('Username ' + cur_user + ' already taken.')
#    else:
#        print('Username ' + cur_user + ' is not taken.')

for new_user in new_users:
    if new_user in current_users:
        print("Username " + new_user + " already taken.")
    else:
        print("Username " + new_user + " is not taken.")
