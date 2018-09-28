#tuple is immutable but we can mutate the list

tup1 = (1,2,3)
# tup1[1]=5, changing this will return exception
print tup1


list1 = [1,2,3,4]
list1[2]=-1 #this will replace 3 with -1
print list1 #this list1 is still pointing towards orignal list


list1.append(5)
print list1

list1.insert(1,-1)
print list1


print list1.index(-1) #this will return sssst occurances of -1
print list1.count(-1) #count the number of times -1 has occured
list1.remove(-1) #this will remove first occurance og -1 from thr list
print list1
list1.reverse() #reverse list implace
print list1


list1.sort() #sort the list, we can send some function so that it would sort in the given order
print list1



