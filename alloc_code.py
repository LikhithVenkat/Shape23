import csv
import json
#read student mark details from csv file
students_marks={}
with open('student_marks.csv') as f:
    next(f)
    reader=csv.reader(f)
    for row in reader:
        name,marks=row
        name=name.lower()
        students_marks[name]=float(marks)
#read projects from csv file, grouped by category
projects_by_category={}
project_details={}
with open('projects.csv') as f:
    reader=csv.DictReader(f)
    for row in reader:
        category=row['category']
        if category not in projects_by_category:
            projects_by_category[category]=[]
        projects_by_category[category].append(row)
        project_details[row['title']]=row

#read name and choices from csv file
student_projects={}
with open('choices.csv') as f:
    reader=csv.reader(f)
    for row in reader:
        name,choice1,choice2,choice3=row
        name=name.lower()
        project_choices={}
        project_choices[1]=project_details[choice1]
        project_choices[2]=project_details[choice2]
        project_choices[3]=project_details[choice3]
        student_projects[name]=project_choices
#student_projects dictionary contains name of student as key and project_choices dictionary as value
#project_choices dictionary contains category as key and project title as value

students=student_projects.keys()
students=sorted(students,key=lambda x:students_marks[x],reverse=True)
x=student_projects
student_projects={}
for i in range(len(x)):
    student_projects[students[i]]=x[students[i]]

projects_by_name={}
for category,projects in projects_by_category.items():
    for project in projects:
        title=project['title']
        max_students=int(project['max_students'])
        projects_by_name[title]={
            'category':project['category1'],
            'title':title,
            'department':project['department'],
            'guide_name':project['guide_name'],
            'email':project['email'],
            'phone':project['phone'],
            'max_students':max_students,
            'students':[]
        }
for name,project_choices in student_projects.items():
    projects=[ projects_by_name[choice['title']] for choice in project_choices.values()]
    for project in projects:
        if len(project['students'])< project['max_students']:
            project['students'].append(name)
            break

#output the result
project_name_details={}
project_name_details['students']=[]
for name,project_choices in student_projects.items():
    projects=[ choice['title'] for choice in project_choices.values()]
    allocated_projects=None

    for project in projects_by_name.values():
        if name in project['students']:
            allocated_project=project['title']
            break
    print(f"{name}: {allocated_project}")
    student={}
    student['name']=name
    for i in project.keys():
        student[i]=project[i]
    project_name_details['students'].append(student)
with open('person_projects.json','w') as f:
    json.dump(project_name_details,f)


