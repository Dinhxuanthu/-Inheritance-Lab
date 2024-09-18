class person:
    def sleep(self):
        return 'sleeping'
class Empolyee: 
    def get_fried():
        return 'fried'
class Teacher(person,Empolyee):
    def teach(self):
        return 'teaching'
h=person()
teacher=Teacher()
print(teacher.teach())
print(h.sleep())