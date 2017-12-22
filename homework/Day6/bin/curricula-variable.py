class School(object):
    def __init__(self, school_name, school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.grade = []
        self.students = []
        self.staff = []
        self.course = []

    def create_grade(self, obj_course):
        print("Grade %s create is success.." % obj_course.name)
        self.grade.append(obj_course)

    def enroll(self, stu_obj):
        print("Student %s enroll finished,ID:%s" % (stu_obj.name, stu_obj.id))
        self.students.append(stu_obj)

    def staff(self, teacher_obj):
        print("Staff %s was finish ")
        self.staff.append(teacher_obj)


