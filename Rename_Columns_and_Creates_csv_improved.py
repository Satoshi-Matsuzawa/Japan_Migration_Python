import pandas as pd
import os

directory = '../../Data/School/0001'
original_file_names = ['0001_kou', '0001_otsu', '0001_hei', '0001_tei']
df = []

for i in range(len(original_file_names)):
    original_file = os.path.join(directory, original_file_names[i]+'.dat')
    df.append(pd.read_csv(original_file, sep='\t', error_bad_lines=False))

# Rename dataset for schools
df[0].columns = ['school_id',
                 'male_graduates', 'male_high_school',
                 'male_part_time_high_school', 'male_employed',
                 'male_home_and_high_school', 'male_home', 'male_others',
                 'female_graduates', 'female_high_school',
                 'female_part_time_high_school', 'female_employed',
                 'female_home_and_high_school', 'female_home',
                 'female_others']

# Rename dataset for students who got employed
df[1].columns = ['school_id', 'gender',
                 'course_1', 'course_2', 'course_3',
                 'course_4', 'course_5', 'course_6',
                 'heir', 'relation_to_the_guardian',
                 'occupation_of_the_guardian',
                 'living_standard', 'family_size',
                 'job_industry', 'job_location', 'job_firm_size',
                 'job_description', 'job_trainee_or_apprentice',
                 'job_starting_salary', 'job_commute_or_live_alone',
                 'job_employment_channel', 'attend_school']

# Rename dataset for students who stays at home
df[2].columns = ['school_id', 'gender',
                 'course_1', 'course_2', 'course_3',
                 'course_4', 'course_5', 'course_6', 'heir',
                 'relation_to_the_guardian', 'occupation_of_the_guardian',
                 'living_standard', 'family_size',
                 'reasons_not_employed', 'career_plan', 'attending_school']

# Rename dataset for students who proceeded to higher education
df[3].columns = ['school_id', 'gender', 'heir', 'relation_to_guardian',
                 'occupation_of_the_guardian', 'academic_scores',
                 'specialization', 'career_plan']

# Create CSV files
new_file_names = ['school', 'student_employed',
                  'student_home', 'student_high_school']

for i in range(len(new_file_names)):
    file_out = os.path.join(directory, new_file_names[i]+'.csv')
    df[i].to_csv(file_out)
