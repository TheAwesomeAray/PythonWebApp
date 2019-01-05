class Student:
    school_name = "Springfield Elementary"

    def __init__(self, first_name, last_name, student_id=1):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"Student {self.first_name}"

    def set_name(self, first_name):
        self.first_name = first_name

    def get_name_capitalize(self):
        return self.first_name.capitalize()

    def get_school_name(self):
        return self.school_name

