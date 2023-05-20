# Shape23
Project allocation code for Shape23


This code reads data from three CSV files, namely "student_marks.csv", "projects.csv", and "choices.csv". It then processes the data to allocate projects to students based on their project choices and marks. Finally, it outputs the result in the form of a JSON file named "person_projects.json".

The first part of the code reads student marks data from "student_marks.csv" and stores it in a dictionary named "students_marks". It then reads project details data from "projects.csv" and stores it in two dictionaries named "projects_by_category" and "project_details". The "projects_by_category" dictionary groups projects by their category, and the "project_details" dictionary stores details of each project by its title.

The second part of the code reads project choices data from "choices.csv" and stores it in a dictionary named "student_projects". This dictionary contains the name of the student as the key and a dictionary of project choices as the value. The "project_choices" dictionary contains the category as the key and the project title as the value.

In the third part of the code, the students are sorted based on their marks in descending order. Then, the code checks the availability of projects based on the maximum number of students allowed for each project. The code assigns a project to each student based on their project choices and the availability of the project.

In the final part of the code, the allocated project details are printed for each student, and a dictionary named "project_name_details" is created to store the allocated projects' details. This dictionary contains a list of student details, including their name and the details of the allocated project. Finally, the code dumps this dictionary as a JSON file named "person_projects.json".

In summary, this code processes student marks, project details, and project choices data to allocate projects to students and stores the allocated project details in a JSON file.
