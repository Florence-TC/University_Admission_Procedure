max_students = int(input())
departments_list = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
dictionary_notes = {'Biotech': [2, 1], 'Chemistry': [2, 2], 'Engineering': [4, 3], 'Mathematics': [3, 3],
                    'Physics': [1, 3]}

with open('applicants.txt', 'r') as applicants:
    app_list = applicants.readlines()

for i in range(len(app_list)):
    app_list[i] = app_list[i].split()
    app_list[i] = [app_list[i][0] + ' ' + app_list[i][1], float(app_list[i][2]), float(app_list[i][3]),
                   float(app_list[i][4]), float(app_list[i][5]), float(app_list[i][6]), app_list[i][7], app_list[i][8],
                   app_list[i][9]]

admissions = {}

for department in departments_list:
    filtered_list = [applicant for applicant in app_list if applicant[6] == department]
    filtered_list.sort(key=lambda x: (min((-x[dictionary_notes[department][0]]
                                           - x[dictionary_notes[department][1]]) / 2, -x[5]), x[0]))
    admit_list = filtered_list[0:max_students]
    admissions[department] = admit_list
    for student in admit_list:
        app_list.remove(student)

for department in admissions:
    if len(admissions[department]) < max_students:
        filtered_list_2 = [applicant for applicant in app_list if applicant[7] == department]
        filtered_list_2.sort(key=lambda x: (min((-x[dictionary_notes[department][0]]
                                           - x[dictionary_notes[department][1]]) / 2, -x[5]), x[0]))
        admissions[department].extend(filtered_list_2)
        admissions[department] = admissions[department][0:max_students]
        for student in admissions[department]:
            if student in app_list:
                app_list.remove(student)

for department in admissions:
    if len(admissions[department]) < max_students:
        filtered_list_3 = [applicant for applicant in app_list if applicant[8] == department]
        filtered_list_3.sort(key=lambda x: (min((-x[dictionary_notes[department][0]]
                                           - x[dictionary_notes[department][1]]) / 2, -x[5]), x[0]))
        admissions[department].extend(filtered_list_3)
        admissions[department] = admissions[department][0:max_students]
        for student in admissions[department]:
            if student in app_list:
                app_list.remove(student)

for department in admissions:
    print(department)
    admissions[department].sort(key=lambda x: (min((-x[dictionary_notes[department][0]]
                                                - x[dictionary_notes[department][1]]) / 2, -x[5]), x[0]))
    for student in admissions[department]:
        print(student[0], max((student[dictionary_notes[department][0]] + student[dictionary_notes[department][1]]) / 2, student[5]))

    with open(f'{department}.txt', 'w') as result_file:
        for student in admissions[department]:
            result_file.write(student[0] + ' ' + str(max((student[dictionary_notes[department][0]]
                                        + student[dictionary_notes[department][1]]) / 2, student[5])) + '\n')

    print('\n')
