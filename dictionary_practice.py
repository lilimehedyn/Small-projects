#create a dict
study_hard = {'course': 'PythonDev', 'period': 'The first month', 'topics': ['Linux', 'Git', 'Databases','Tests', 'OOP'] }

# add new item
study_hard['tasks'] = ['homework', 'practice online on w3resourse', 'read about generators', 'pull requests',
                       'peer-review', 'status', 'feedback']

#print out items
print(study_hard)
print(study_hard.get('course'))
print(study_hard.get('period'))
print(study_hard.get('topics'))
print(study_hard.get('tasks'))

#updating the dict
study_hard.update({'course': 'Phyton Developer'})
print(study_hard)
print("The lenth of dictionary is", len(study_hard))
print(study_hard.keys())
print(study_hard.values())

# for loop for dict
for key, value in study_hard.items():
    print(key, value)

for value in study_hard:
    print(study_hard['period'])

    