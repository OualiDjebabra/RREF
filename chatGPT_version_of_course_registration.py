import time
import operator


class UniversitySystem:
    def __init__(self):
        self.students_info = []
        self.students = set()
        self.activities = []
        self.latest_index = 0
        self.activity_id = 0
        self.courses = {
            0: "cs50",
            1: "cs51",
            2: "cs52",
            3: "cs100",
            4: "cs101",
        }

    # -------- Helpers -------- #
    def _log_activity(self, activity_type, **kwargs):
        """Create and store an activity record."""
        activity = {
            "activity_id": self.activity_id,
            "type": activity_type,
            "time_stamp": time.time(),
            **kwargs
        }
        self.activities.append(activity)
        self.activity_id += 1
        return activity

    def _find_student(self, name):
        """Return student dict or None."""
        return next((s for s in self.students_info if s["student_name"] == name), None)

    # -------- Core Features -------- #
    def register(self, student_name):
        if student_name in self.students:
            print("User already exists.")
            return

        self.students.add(student_name)
        activity = self._log_activity("registration")

        self.students_info.append({
            "student_name": student_name,
            "student_id": self.latest_index,
            "courses": set(),
            "activities": [activity],
            "grade": []
        })
        self.latest_index += 1

    def enroll(self, student_name, course_id):
        student = self._find_student(student_name)
        if not student:
            print("Student not found. Register first.")
            return
        if course_id not in self.courses:
            print("Invalid course ID.")
            return

        course = self.courses[course_id]
        activity = self._log_activity("enrolling", course_id=course_id)
        student["courses"].add(course)
        student["activities"].append(activity)

    def complete_course(self, student_name, course_name, course_id):
        student = self._find_student(student_name)
        if not student:
            print("Student not found.")
            return
        if self.courses.get(course_id) != course_name:
            print("Course name and ID mismatch.")
            return

        student["grade"].append(course_name)
        activity = self._log_activity("graduating", course_id=course_id)
        student["activities"].append(activity)

    def enrollers(self, course_id):
        course = self.courses.get(course_id)
        if not course:
            print("Invalid course ID.")
            return

        enrollers_list = [s["student_name"] for s in self.students_info if course in s["courses"]]
        print(f"Enrollers in {course}: {enrollers_list}")

    def top_students(self):
        student_grades = {
            s["student_name"]: len(s["grade"]) for s in self.students_info
        }
        sorted_students = dict(sorted(student_grades.items(), key=operator.itemgetter(1), reverse=True))
        print(f"The top students are {sorted_students}")

    # -------- Admin -------- #
    def admin_panel(self):
        commands = {
            1: lambda: print(self.students_info),
            2: lambda: print(self.activities),
            3: lambda: print(self.students),
        }

        while True:
            cp_cmd = int(input("""
            Welcome to Admin Control Panel
            ___________________________
            Choose one:
            1: See all students info
            2: See all activities
            3: See all registered students names
            4: Exit
            """))

            if cp_cmd == 4:
                break
            commands.get(cp_cmd, lambda: print("Invalid choice"))()

    # -------- Menu Loop -------- #
    def run(self):
        while True:
            name = input("Enter your name to sign in: ")
            while True:
                x = int(input(f"""
Choose one of the following commands:
1: Register as new student
2: Enroll in a course
3: Complete a course
4: See enrollers in a course
5: See top students
6: Admin control panel
7: Exit
"""))

                commands = {
                    1: lambda: self.register(name),
                    2: lambda: self.enroll(name, int(input(f"Choose one from these courses {self.courses}: "))),
                    3: lambda: self.complete_course(
                        name,
                        input("Enter course name: "),
                        int(input(f"Enter course id from these {self.courses}: "))
                    ),
                    4: lambda: self.enrollers(int(input(f"Enter course id from these {self.courses}: "))),
                    5: self.top_students,
                    6: self.admin_panel,
                    7: exit
                }

                commands.get(x, lambda: print("Invalid choice"))()


if __name__ == "__main__":
    system = UniversitySystem()
    system.run()
