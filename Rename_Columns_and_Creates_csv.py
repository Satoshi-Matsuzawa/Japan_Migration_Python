import pandas as pd
import os

directory = '../../Data/School/0001'


# Dataset for schools
school_file = os.path.join(directory, '0001_kou.dat')

df_school = pd.read_csv(school_file, sep='\t', error_bad_lines=False)
df_school.columns = ['school_id',
                     'male_graduates', 'male_high_school',
                     'male_part_time_high_school', 'male_employed',
                     'male_home_and_high_school', 'male_home', 'male_others',
                     'female_graduates', 'female_high_school',
                     'female_part_time_high_school', 'female_employed',
                     'female_home_and_high_school', 'female_home',
                     'female_others']

school_file_out = os.path.join(directory, 'school_statistics.csv')
df_school.to_csv(school_file_out)

# Dataset for students who got employed
employed_file = os.path.join(directory, '0001_otsu.dat')

df_employed = pd.read_csv(employed_file, sep='\t', error_bad_lines=True)
df_employed.columns = ['school_id', 'gender',
                       'course_1', 'course_2', 'course_3',
                       'course_4', 'course_5', 'course_6',
                       'heir', 'relation_to_the_guardian',
                       'occupation_of_the_guardian',
                       'living_standard', 'family_size',
                       'job_industry', 'job_location', 'job_firm_size',
                       'job_description', 'job_trainee_or_apprentice',
                       'job_starting_salary', 'job_commute_or_independent',
                       'job_employment_channel', 'attend_school']

employed_file_out = os.path.join(directory, 'employed.csv')
df_employed.to_csv(employed_file_out)

# Dataset for students who stays at home
home_file = os.path.join(directory, '0001_hei.dat')

df_home = pd.read_csv(home_file, sep='\t', error_bad_lines=True)
df_home.columns = ['school_id', 'gender',
                   'course_1', 'course_2', 'course_3',
                   'course_4', 'course_5', 'course_6', 'heir',
                   'relation_to_the_guardian', 'occupation_of_the_guardian',
                   'living_standard', 'family_size',
                   'reasons_not_employed', 'career_plan', 'attending_school']

home_file_out = os.path.join(directory, 'home.csv')
df_home.to_csv(home_file_out)

# Dataset for students who proceeded to higher education
higher_ed_file = os.path.join(directory, '0001_tei.dat')

df_higher_ed = pd.read_csv(higher_ed_file, sep='\t', error_bad_lines=True)
df_higher_ed.columns = ['school_id', 'gender', 'heir', 'relation_to_guardian',
                        'occupation_of_the_guardian', 'academic_scores',
                        'specialization', 'career_plan']

higher_ed_file_out = os.path.join(directory, 'higher_ed.csv')
df_higher_ed.to_csv(higher_ed_file_out)
