class Student:
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level
        self.Grades = []
        
    def add_grades(self, score: float):            
        self.Grades.append(score)
            
    def calculate_avg(self):
        if self.Grades: 
            return sum(self.Grades) / len(self.Grades)
        else:
            return 0.0
                
    def get_letter_grade(self):
        grd = self.calculate_avg()
        if grd >= 90:
            return "A+"
        elif grd >= 80:
            return "B"
        elif grd >= 70:
            return "C"
        elif grd >= 60:
            return "D"
        else:
            return "F"
            
    def display_info(self):
        print(f"Student: {self.name} ({self.grade_level} Grade) | Average: {self.calculate_avg()} | Grade: {self.get_letter_grade()}")
            
if __name__ == "__main__":
    Student1 = Student("Ali", "12th")
    Student1.add_grades(93)
    Student1.add_grades(81)
    Student1.add_grades(73)
    Student1.display_info()