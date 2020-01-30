# Load dats file, rename columns, and create csv files

import pandas as pd
import os

directory = '../../Data/School/0001'
original_file_names = ['0001_kou', '0001_otsu', '0001_hei', '0001_tei']
df = []

for file_name in original_file_names:
    original_file = os.path.join(directory, file_name + '.dat')
    df.append(pd.read_csv(original_file, sep='\t', error_bad_lines=False))

# Column Names
school_id = ['school_id']

# For schools
categories = ['_graduates', '_high_school', '_part_time_high_school',
              '_employed', '_home_and_high_school', '_home', '_others']
gender = ['male', 'female']
gender_and_categories = []
for g in gender:
    for c in categories:
        gender_and_categories.append(g + c)

# For students
student_gender = ['gender']
courses = ['course_1', 'course_2', 'course_3',
           'course_4', 'course_5', 'course_6']
guardian = ['heir', 'relation_to_the_guardian', 'occupation_of_the_guardian']
family = [' living_standard', 'family_size']
job = ['industry', 'location', 'firm_size',
       'job_description', 'trainee_or_apprentice',
       'starting_salary', 'commute_or_live_alone',
       'employment_channel', 'attend_school']
home = ['reasons_not_employed', 'career_plan', 'attending_school']
high_school = ['academic_scores', 'specialization', 'career_plan']

# Rename dataset for schools
df[0].columns = school_id + gender_and_categories

# Rename dataset for students who got employed
df[1].columns = school_id + student_gender + courses + guardian + family + job

# Rename dataset for students who stays at home
df[2].columns = school_id + student_gender + courses + guardian + family + home

# Rename dataset for students who proceeded to higher education
df[3].columns = school_id + student_gender + guardian + high_school

# Create CSV files
new_file_names = ['school', 'student_employed',
                  'student_home', 'student_high_school']

for i in range(len(new_file_names)):
    file_out = os.path.join(directory, new_file_names[i] + '.csv')
    df[i].to_csv(file_out, index=False)
