
# Atom class
class atom(object):
    def __init__(self, atno, x, y, z):
        self.atno = atno
        self.position = (x, y, z)

    def symbol(self):  # a class method
        return self.atno

    def __repr__(self):  # overloads printing
        return '%d %10.4f %10.4f %10.4f' % (self.atno, self.position[0], self.position[1], self.position[2])


# Defined class variables (atno,position) that are persistent and local to the atom object


# Molecule Class
class molecule:
    def __init__(self, name='Generic'):
        self.name = name
        self.atomlist = []

    def addatom(self, atom):
        self.atomlist.append(atom)

    def __repr__(self):
        s = 'This is a molecule named %s\n' % self.name
        s = s + 'It has %d atoms\n' % len(self.atomlist)
        for atom in self.atomlist:
            s = s + str(atom) + '\n' #this str function will convert atom to its strign value
        return s



aa = atom(5, 3, 4, 1)
ab = atom(1, 2, 3, 4)

print aa
print ab

ma = molecule("Molecule A")
ma.addatom(aa)
ma.addatom(ab)
print "Printing molecule"
print ma
