# REMINDER: Only do one challenge at a time! Save and test after every one.


# For this challenge, we are going to build up a set of functions to create
# code for a semi-realistic situation: We will be building helper functions to
# manage data about a patient at a hospital. You can imagine the final software
# being useful for nurses and doctors to keep track of information on patients.

# The information about patients will be in a dictionary that is passed around
# via parameters to and from functions.

print('Challenge 1 -------------')
# Challenge 1:
# Uncomment and examine the following code. See if you can explain what every
# line is doing.

def patient_initialize(patient, first_name, last_name):
    patient['first_name'] = first_name
    patient['last_name'] = last_name
    patient['is_checked_in'] = False


terry = {}
patient_initialize(terry, 'Terry', 'Gilliam')
print(terry)

print('Challenge 2 -------------')
# Challenge 2:
# 1. Rewrite patient_initialize so that it has 2 more arguments: first_name,
# and last_name.
# 2. Write 2 more invocations of the function to create a patient for
# yourself and the student sitting next to you.
# 3. Use print to confirm that your function is working correctly by printing
# out the patient variable before and after the invocation of the function.

print('Challenge 3 -------------')
# Challenge 3:
# 1. Write a new function called "patient_check_in".
# 2. This function should accept a patient dictionary as an argument, and then
# modify that argument to make "is_checked_in" set to be True.
# 3. Again, use print to verify it's working.

def patient_check_in(patient):
    patient['is_checked_in'] = True


patient_check_in(terry)
print('Terry', terry)


print('Challenge 4 -------------')
# Challenge 4:
# 1. Write a new function called "patient_nurse_check_up". It should take a
# patient dictionary as an argument.
# 2. It should then ask the following questions.
#     1. Does the patient smoke?
#     2. Does the patient drink?
#     3. Patient blood-pressure?
# 3. After each question, it should store that information into the patient
# dictionary. It should ask them using input() and storing the result in
# separate variables, or assigning keys in the dictionary.
# 4. Again, use print to verify it's working.

def patient_nurse_check_up(patient):
    patient['smoke'] = input('Do you smoke?')
    patient['drink'] = input('Do you drink?')
    patient['bp'] = int(input('What is your blood pressure?'))
    
patient_nurse_check_up(terry)
print('Terry', terry)





print('Challenge 5 -------------')
# Challenge 5:
# Time to bring it all together.
# 1. Write a new function called "patient_visit".
# 2. Using inputs, it should ask the name of the patient, then initialize the
# patient with that information.
# 3. It should then use all of the above functions to "process" the patient
# (e.g. invoking them one at a time in sequence)

# Hint: Feel free to comment out the previous invocations of the above function
# Add a prints as needed to report back on the process.

def patient_visit(patient):
    first_name = input('First name?')
    last_name = input('Last name?')
    patient_initialize(patient, first_name, last_name)
    patient_check_in(patient)
    patient_nurse_check_up(patient)

patient = {}
patient_visit(patient)

print('-------------')
# Bonus Challenge:
# Create another function called "patient_doctor_diagnose". It should only
# accept patients who have already been checked in and visited a nurse. It
# should allow a doctor to enter a "diagnosis" and "recommendation".
#
# 1. Check that blood-pressure is below 120. If between 120-130 it should
#    diagnose "Stage 1 Hypertension", if between 130-180 "Stage 2 Hypertension"
# 2. Recommend the patient a) visit the ER if blood pressure is above 180, or
#    b) if the patient smokes, recommend the patient stop.






print('-------------')
# Advanced Bonus Challenge:
# Where does our data go? At the end of every check up, we should store it in a
# file. Maybe try writing a CSV?

