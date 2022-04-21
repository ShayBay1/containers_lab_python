# 1
from operator import contains


students = ['bob', 'jay', 'billy']
print(students[1])
print(students[-1])
# 2
foods = ('grape', 'mango', 'pinapple')
for i in foods:
	print(f"{i} is a good fruit")
# 3
for i in foods[1:]:
    print(i)
# 4
home_town = {
	'city': 'boise',
	'state':'idaho',
	'population':100,
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")
# 5
for key,value in home_town.items():
    print("{}:{}".format(key,value))
# 6
cohort = []
for index, student in enumerate(students):
    cohort.append({
	   'student': student,
	    'fav_food': foods[index]
	})
print(cohort)
# 7
awesome_students=[]
for s in students:
    awesome_students.append(s+" is awesome")
print(awesome_students)
# 8
for a in foods:
    if 'a' in a:
        print(a)
