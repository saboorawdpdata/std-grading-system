#student grading system

print("******Student Grading System*******")

student_count=1
while student_count <= 5:
    print(f" *********** Student {student_count}******")          
    #Input       
    name=input("Your Full Name:")
    per=eval(input("Percentage:"))
    
    #if-elif-else-Grade
    
    if per >= 90:
        grade= "A+"
        remark= "Wonder Full"
    elif per >= 80:
        grade = "A"
        remark = "Good"
    elif per >=70:
        grade = "B+"
        remark = "Fair"
    elif per >= 60:
        grade = "B"
        remark = "Average"        
    elif per >=50:
        grade = "C"
        remark = "Below Average"
    elif per >=40:
        grade = "D"
        remark = "Just Passed"
    else:
        grade = "F"
        remark = "Failed!"
            
    #Nested if - for extra comments based on marks
        
    if per >= 75:
        if per >=95:
            special="Topper Studnet! and eligilbe for 100% scholarship"
        else:
            special = "Eligible for 50% scholarship"
    else:
        if per >=60:
            special = "work more,Efforts more!"
        else:
            special = "Practice Regularly"
            
    #Nest loop, For for extra subject analysis
            
    print(f"\n Dear {name}, Your Subject:")
    subjects= ["Maths", "Science", "English", "Urdu", "Chem", "S.St", "Isl", ]
    
    for subject in subjects:
        if subject == "Maths":
            sub_marks = per+5  #extra marks for maths
        elif subject== "Science":
            sub_marks= per-2
        elif subject== "English":
            sub_marks= per-3
        elif subject== "Urdu":
            sub_marks= per-4
        elif subject== "Chem":
            sub_marks= per-3
        elif subject== "S.St":
            sub_marks= per-4
        else:
            sub_marks = per-2
            
        #Nested if in for loop
        
        if sub_marks>100:
            sub_marks=100
        elif sub_marks <0:
            sub_marks=0
            
        print(f"{subject} : {sub_marks}")
        
#final result print
        
    print(f"\n Result for {name}, \n Percentage: {per} \nGrade: {grade} \nRemarks: {remark} \nSpecial: {special} \nUni Suggest: {uni_suggest}")
    
    student_count= student_count + 1
        