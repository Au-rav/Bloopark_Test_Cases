#1. Create Python classes that represent these data definitions
#TABLE students
    #id INTEGER PRIMARY KEY,
    #firstName VARCHAR(30) NOT NULL,
    #lastName VARCHAR(30) NOT NULL
#TABLE enrollments
    #id INTEGER NOT NULL PRIMARY KEY
    #year INTEGER NOT NULL
    #studentId INTEGER NOT NULL
    
class students:
	def __init__(self, firstName,lastName):
		self.firstName=firstName
		self.lastName=lastName


class enrollments:
	def __init__(self,
id,year,studentId):
		self.id=id
		self.year=year
		self.studentId=studentId
        
  
