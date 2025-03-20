"""
Object-Oriented Version of the Student Party System
"""

COURSE_GRADE_MAX = 500


class Student:
    """
    Represents a student with attributes and methods for management.
    """

    student_id_counter = 1  # Class variable for auto-incrementing student IDs

    def __init__(self, first_name: str, last_name: str, total_mark: int):
        self.student_id = Student.student_id_counter
        Student.student_id_counter += 1
        self.first_name = first_name
        self.last_name = last_name
        self.total_mark = total_mark

    def update_info(self, **kwargs):
        """
        Updates student's attributes except student_id.
        """
        for key, value in kwargs.items():
            if key != "student_id":
                setattr(self, key, value)

    def is_invited(self, min_grade: int = 250) -> bool:
        """
        Checks if the student is invited to the party based on grade.
        """
        return self.total_mark >= min_grade

    def __repr__(self):
        return f"Student({self.student_id}, {self.first_name} {self.last_name}, {self.total_mark})"


class StudentAnswer:
    """
    Represents a student's response regarding party invitation.
    """

    def __init__(self, student_id: int, answer: bool):
        self.student_id = student_id
        self.answer = answer

    def __repr__(self):
        return f"StudentAnswer(Student ID: {self.student_id}, Answer: {self.answer})"


class Party:
    """
    Manages party invitations, students, and pricing.
    """

    def __init__(self, ticket_price: float):
        self.invited_students = []
        self.ticket_price = ticket_price

    def invite_student(self, student: Student):
        """
        Adds a student to the invitation list if they qualify.
        """
        if student.is_invited():
            self.invited_students.append(student)
        else:
            self.notify_student_not_invited(student)

    def remove_student(self, student_id: int):
        """
        Removes a student from the invitation list.
        """
        for student in self.invited_students:
            if student.student_id == student_id:
                self.invited_students.remove(student)
                return True
        raise Exception(f"Student with ID {student_id} is not found in the invitation list.")

    def notify_student_not_invited(self, student: Student):
        """
        Notifies a student that they are not invited.
        """
        print(f"Sorry {student.first_name}, you are not invited to the party.")

    def get_invited_students(self):
        """
        Returns a list of invited students.
        """
        return self.invited_students

    def get_total_price(self):
        """
        Calculates the total ticket price based on invited students.
        """
        return len(self.invited_students) * self.ticket_price

    def __repr__(self):
        return f"Party(Invited Students: {len(self.invited_students)}, Ticket Price: {self.ticket_price})"


# Example Usage:

# Creating students
student1 = Student("Arthur", "Pendragon", 420)
student2 = Student("Guinevere", None, 301)
student3 = Student("Morgan", "le Fay", 520)
student4 = Student("Lancelot", "du Lac", 140)
student5 = Student("Merlin", "Hernandez", 500)

# Creating a Party
party = Party(ticket_price=50)

# Inviting students
party.invite_student(student1)
party.invite_student(student2)
party.invite_student(student3)
party.invite_student(student4)  # Should notify that Lancelot is not invited
party.invite_student(student5)

# Displaying invited students
print("Invited Students:", party.get_invited_students())

# Calculating total price
print("Total Party Cost:", party.get_total_price())

# Handling student answers
answer1 = StudentAnswer(student1.student_id, True)
answer2 = StudentAnswer(student2.student_id, False)

print(answer1, answer2)
