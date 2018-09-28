tu = (23, 'abc', 4.56, (2,3), 'def') #tuple, bracks,  defined using parentheses (and commas)
print tu
print tu[2] #We can access individual members of a tuple, list, or string using square bracket "array" notation. All are zero indexed
print tu[-1] #negative indices


#Slicing, returning subset of something
subsetTu = tu[1:2] #End is not included
print "Printing subset"
print subsetTu
subsetTu = tu[1:-1] #again it will normalise the index and won't include last index in the subset calculation
print "Printing subsetTu"
print subsetTu
print len(tu) #This will give the length of the list
tuCopy = tu[:] #this will give deep copy
print tu
print "copy list"
print tuCopy
#print tu = tuCopy, this will not work for immutable things



#in operator
print "Test of in operator"
print 23 in tu
print 233 in tu #this will return false
print 233 not in tu #this will return true




li = ["abc", 34, 4.34, 23] #Lists,  defined using square brackets (and commas).
print li
liCopy = li[:]
print "List comparision"
li.append("Hello")
print liCopy
print li
#this proves that both are not same

st = "Hello World"
st = 'Hello World'
st = """this is a multiline tuple
thankyou"""
#This will print in multiline
print st
print st[1]=='h'



#in Operator in strings
str = 'helloMan'
print 'h' in str
print 'H' in str
print 'hh' not in str



#+ operator
list1 = ["Hello",1,2,3,"are","you"]
print list1
list2 = ["You Hello",1,2,3,"are","you"]
list3 = list1+list2
print list3


print [1,2,3]+[4,5,6]



# * operator
print [1,2]*5 # List, this will replicate the list 5 times
print "Hello "*5
