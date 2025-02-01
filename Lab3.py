"""
File: student.py
Resources to manage a student's name and test scores.
"""

import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
    
    def __eq__(self, other):
        """Returns True if two students have the same name."""
        if isinstance(other, Student):
            return self.name == other.name
        return NotImplemented

    def __lt__(self, other):
        """Returns True if this student's name is less than the other student's name."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns True if this student's name is greater than or equal to the other student's name."""
        return self.name >= other.name
        
    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """Define Students"""
    student1 = Student("Carlo", 5)
    student2 = Student("Mark", 5)
    student3 = Student("Carlo", 5)

    print("\nTesting equality:")
    print("student1 == student2:", student1 == student2)  # Expected: False
    print("student1 == student3:", student1 == student3)  # Expected: True
    
    # Testing less than
    print("\nTesting less than:")
    print("student1 < student2:", student1 < student2)    # Expected: True ("Carlo" < "Mark")
    print("student2 < student1:", student2 < student1)    # Expected: False
    
    # Testing greater than or equal to
    print("\nTesting greater than or equal to:")
    print("student1 >= student3:", student1 >= student3)  # Expected: True ("Carlo" >= "Carlo")
    print("student2 >= student1:", student2 >= student1)  # Expected: True ("Mark" >= "Carlo")
    print("student1 >= student2:", student1 >= student2)  # Expected: False ("Carlo" is not >= "Mark")

    #PROGRAMMING EX 2:
    print("------------------------\n")
    studentList = [Student("John", 3), Student("Patrick", 3), Student("Aaron", 3), Student("Claire", 3)]

    print("ORIGINAL LIST:")
    for student in studentList:
        print(student)

    print("\nSHUFFLED: ")
    random.shuffle(studentList)
    for student in studentList:
        print(student)
    
    print("\nSORTED: ")
    studentList.sort()
    for student in studentList:
        print(student)

if __name__ == "__main__":
    main()