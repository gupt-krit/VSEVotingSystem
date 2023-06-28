class Voter:
    name = str()
    grade = int()
    section = str()
    point = int()
    def __init__(self,name,grade,section) -> None:
        self.name=name
        self.grade=grade
        self.section=section
        self.point=0