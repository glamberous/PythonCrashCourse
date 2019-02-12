

poll = {'justine':'python', 'eric':'c', 'billy':'c#', 'jordan':'ruby'}
names_list = ['justine', 'jimmmy', 'becky', 'eric']

for name in names_list:
    if name in poll.keys():
        print("Thanks for taking the poll, " + name)
    elif name not in poll.keys():
        print(name + ", please take the poll at your first available chance")

