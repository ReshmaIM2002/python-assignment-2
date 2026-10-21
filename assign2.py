age_list = [24,25,26,27,28]
print(age_list)

name_list = ["reshma","ammu","anu",]
print(name_list)



name_list.append("yazhini")
print(name_list)

age_list.insert(2,30)
print(age_list)



name_list.remove("yazhini")
print(name_list)


age_list.pop()
print(age_list)


age_list.extend([29,30,26])
print(age_list)



age_list.sort(reverse=True)
print(age_list)



print("maximum age:",max(age_list))
print("minimun age:",min(age_list))


print("sum of all ages:",sum(age_list))


print(name_list[0])

print(name_list[2])


print(name_list[0:])


name_list.reverse()
print(name_list)


student_marks={"Reshma":100,"Anu":90,"ammu":86,"appu":45,"achu":72,"lechu":88}
print(student_marks)


print(student_marks["Reshma"])


student_marks["janani"]=80
print(student_marks)


student_marks["appu"]=82
print(student_marks)




print("keys:",student_marks.keys())

print("values:",student_marks.values())

print("items:",student_marks.items())


my_set={'a','e','i','o','u','a','a','i'}
print(my_set)


my_set.add('s')
print(my_set)


set1={1,3,5,7,9}
set2={3,3,5,8,10}
print(set1)
print(set2)

print("union:",set1.union(set2))

print("intersection:",set1.intersection(set2))


score=float(input("enter your score(0 to 10):"))

if score < 0 or score >10:
    print("invalid score! please enter a score between 0 and 10.")

elif score >7:
    print("above average:excellent work! keep it up!")
elif score >=4:
    print("average :good effort! keep practicing,there's room for improvement.")
else:
    print("below average: need to improve.")
