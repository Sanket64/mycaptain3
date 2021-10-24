import csv
def writecsv_file(file_info):
    with open ('student_info.csv','a',newline='')as csv_file:
        
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            
            
            writer.writerow(["Name", "Age", "contact no", "Email_id"])
        writer.writerow(file_info)

condition = True
while(condition):
    student_info = input("Enter information of students")
    print(student_info)

    student_infolist = student_info.split(" ")
    print(student_infolist)

    choice = input("Entered info is correct or not? Y/N")

    if choice == "Y":
        writecsv_file(student_infolist)

        condition_check = input("type Y/N if want to continue")

        if condition_check == "Y":
            condition = True
        elif condition_check == "N":
            condition = False
    elif choice == "N":
        print("please re-enter info")
    
                            
    
    
