print "Hello to dictionary"



d = {'user':'bozo', 'pswd':1234}
print d
print d['pswd']

print d['user'] #suppose this user is not in dictionary,then this will given an exception
d['pswd'] = 11
print d
d['new pswd'] = 10
print d


del d['new pswd']
print d


print d.keys()
print d.values()
print d.items()