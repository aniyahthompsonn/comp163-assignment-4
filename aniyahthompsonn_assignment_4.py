# Step 1
student_name = "Aniyah" # Replace with your actual name
current_gpa = 3.8 # Float between 1.0-4.0
study_hours = 48 # Integer (Ex. 25)
social_points = 50 # Integer (Ex. 50)
stress_level = 85 # Integer 0-100

# Display Welcome Stats
print (f"--- Welcome, {student_name} to your Academic Profile! ---")
print (f"GPA: {current_gpa}")
print (f"Study Hours: {study_hours}")
print (f"Social Points: {social_points}")
print (f"Stress Level: {stress_level}")



#Step 2
print ("")
print ("--- Course Planning: ---")
print ("Choose your course load:")
print ("A) Light (12 credits)")
print ("B) Standard (15 credits)")
print ("C) Heavy (18 credits)")
print ("")
choice = input("Your choice: ")

if choice == "A":
    if current_gpa <= 2.0:
        study_hours += 5
        stress_level += 8
    else:
        study_hours += 3
        stress_level += 5
    print ("You chose a light course load.")
elif choice == "B":
    if current_gpa < 2.8:
        study_hours += 8
        stress_level += 10
    else:
        study_hours += 6
        stress_level += 8
    print ("You chose a standard course load.")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 10
        stress_level += 12
    else:
        study_hours += 8
        stress_level += 10
    print ("You chose a heavy course load.")
else:
    print ("Invalid choice. Please select A, B, or C.")

print ("")
print ("--- Updated Status:--- ")
print (f"Study Hours: {study_hours}")
print (f"Stress Level: {stress_level}")
print ("")



#Step 3
study_options = ["Programming", "Math", "English"]


print ("--- Time to Study ---")
print ("Choose a subject to study to focus on:")
print ("Subjects", study_options)
print ("")
subject_choice = input ("What subject will you study? ")

if subject_choice in study_options:
    print (f"You chose to study {subject_choice}.")

    if subject_choice == "Programming" and not stress_level < 80:
        current_gpa += 0.2
        social_points += 5
        print ("You coded all week! GPA boosted, but your social life took a hit.")
    elif subject_choice == "Math" or current_gpa < 2.5:
        current_gpa += 0.1
        social_points -= 15
        print ("You solved so much math examples, GPA up !")
    elif subject_choice == "English" and social_points < 60:
        current_gpa += 0.1
        social_points += 2
        print ("You wrote an essay while learning how to balance your social life!")
    else:
        print ("You studided but nothing else happened, try again next week.")
elif subject_choice not in study_options:
    print ("That's not a valid subject. Skipped study week = no progress")

current_gpa = round(current_gpa, 2)

print ("")
print ("--- Update Status ---")
print (f"GPA: {current_gpa}")
print (f"Social Points: {social_points}")



# Step 4
print ("")
print ("--- Final Semester Assessment ---")

if (current_gpa > 1.0) and (study_hours > 0):
    print ("Evaluating your results...")
    print ("")

    honors_candidate = True if current_gpa >= 3.5 else False
    if honors_candidate is True:
        print ("Your eligible for honors recognition!")
    elif honors_candidate is not True:
        print ("You ar enot eligible for honors.")
    if study_hours >= 50 and current_gpa >= 3.5:
        ending = "Your hard work paid off! Congratulations!"
        print ("")
    elif stress_level >= 95 and current_gpa >= 3.0:
        ending = "Your academics paid off but you ended up burnt out."
    elif current_gpa < 2.0 and stress_level > 70:
        ending: "Unfortunately, you're on academic probation."
    elif social_points >= 80 and current_gpa < 2.0:
        ending = "You didn't pass but at least you had fun"
    else:
        ending = "Semester completed. Lets try better next semester."
else:
    ending = "Cannot determine ending"

print ("--- Final Results: ---")
print (f"Name: {student_name}")
print (f"GPA: {current_gpa}")
print (f"Study Hours: {study_hours}")
print (f"Social Points: {social_points}")
print (f"Stress Level: {stress_level}")
print ("")
print ("--- Your Ending: ---")
print (ending)