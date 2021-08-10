# list == array

friends = ['istiak', 'mahfuz', 'rifat', 'rimon', 'sumi']

print(friends[0])  # istiak
print(friends[1])  # mahfuz
print(friends[1:])  # ['mahfuz', 'rifat', 'rimon', 'sumi']
print(friends[1:3])  # ['mahfuz', 'rifat']


# copy list. now if i put or delete any data in main list then second list wouldn't change
my_friends = friends.copy()
print(my_friends)

# new_friends = friends[:]  # copy all item in new_friends var
# print(new_friends)  # ['istiak', 'mahfuz', 'rifat', 'rimon', 'sumi']

# methods
friends.append('joya')
print(friends)  # ['istiak', 'mahfuz', 'rifat', 'rimon', 'sumi', 'joya']

friends.insert(0, 'nihal')  # first index number, second data
print(friends)  # ['nihal', 'istiak', 'mahfuz', 'rifat', 'rimon', 'sumi', 'joya']

friends.remove('rimon')  # ['nihal', 'istiak', 'mahfuz', 'rifat', 'sumi', 'joya']
print(friends)

# friends.clear()     # this method clear all list element
# print(friends)  # []

friends.pop()  # remove last item

# get index number pass by list item
print(friends.index('sumi'))  # 4

# sort list
friends.sort()

# reverse list item
friends.reverse()

