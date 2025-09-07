import time
import operator
students_info=[]
students=set()
activities=[]
latest_index=0
activity_id=0
courses=({0:"cs50",1:"cs51",2:"cs52",3:"cs100",4:"cs101"})
class university:
    def __init__(self, student_name):
        self.student_name=student_name
        
    def register(self):
        if self.student_name not in students:
            global latest_index, activity_id
            students.add(self.student_name)
            activities.append({
                "activity_id":activity_id,
                "type":"registaration",
                "time_stamp":time.time()
            })
            
            students_info.append({
                "student_name":self.student_name,
                "student_id":latest_index,
                "courses":set(),
                "activities":[activities[activity_id]]
                ,"grade":[]
            })
            latest_index+=1
            activity_id+=1
            
        else:
            print("user already exist")
    def search_id_by_name(self):
        id=None
        for x in range(len(students_info)):
            if students_info[x]["student_name"]==self.student_name:
                id=students_info[x]["student_id"]
        return id
                
            
    def enroll(self):
        global activity_id
        course_id=int(input(f'choose one from these courses {courses}'))
        activities.append({
                "activity_id":activity_id,
                "type":"enrolling",
                "course_id":course_id,
                "time_stamp":time.time()
            })
        
        students_info[self.search_id_by_name()]["activities"].append(activities[activity_id])
        activity_id+=1
        
        students_info[self.search_id_by_name()]["courses"].add(courses[course_id])
    def completed_course(self, course_name, course_id):
        global activity_id
        if courses[course_id]==course_name:
            students_info[self.search_id_by_name()]["grade"].append(course_name)
            activities.append({
                "activity_id":activity_id,
                "type":"graduating",
                "course_id":course_id,
                "time_stamp":time.time()
            })
            
            students_info[self.search_id_by_name()]["activities"].append(activities[activity_id])
            activity_id+=1
    def enrollers(self, course_id):
        enrollers_list=[]
        for x in range(len(students_info)):
            if courses[course_id] in students_info[x]["courses"]:
                enrollers_list.append(students_info[x]["student_name"])
        print(f"enrollers in {courses[course_id]} : {enrollers_list}")
    def top_students(self):
        student_grades={}
        
        for x in range(len(students_info)):
            completed_courses=len(students_info[x]["grade"])
            student_grades[students_info[x]["student_name"]]=completed_courses
        print(f"the top students are {dict(sorted(student_grades.items(), key=operator.itemgetter(1)))}")
        
while True:
    name=input("enter your name to signin : ")
    while True:
        x=university(name)
        commands=int(input("""choose one of the followings commands
        1:register as new student
        2:enroll in a course
        3:complete a course
        4:see enrollers in a course
        5:see top students
        6:Admin control pannel
        7:exit               
                    """))
        if commands==1:
            x.register()
            
        elif commands==2:
            x.enroll()
            
        elif commands==3:
            x.completed_course(input("enter course name : "),int(input(f'enter course id from these {courses} : ')))
            
        elif commands==4:
            x.enrollers(int(input(f'enter course id from these {courses} : ')))
            
        elif commands==5:
            x.top_students()
        elif commands==6:
            while True:
                cp_cmd=int(input("""
                welcome to admin control pannel
                ___________________________
                choose one of the followings commands:
                1: see all students info
                2: see all activities
                3: see all registered students names
                4: exit
    """))
                if cp_cmd==1:
                    print(students_info)
                elif cp_cmd==2:
                    print(activities)
                elif cp_cmd==3:
                    print(students)
                elif cp_cmd==4:
                    break
        elif commands==7:
            break
    quit=input("enter y to exit ")
    if quit=="y" or quit=="Y":
        break
    else:
        print("welcome back")
        continue
    
    



            

        
  

