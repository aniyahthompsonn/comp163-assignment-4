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