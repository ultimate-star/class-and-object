class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    def change_name(self, new_name):
        self.name = new_name
        new_name = "peter"
        print (f"The student updated his name to {new_name}")

    def change_age(self, new_age):
            self.age = new_age
            new_age= "34"
            print (f"The student updated his age to {new_age}")

    def add_track(self, new_track):
            self.tracks = new_track
            new_track = "UI/UX"
            print(f"The student updated his tracks to {new_track}")

    def get_score(self, new_score):
            self.score = new_score 
            new_score = "30.50"
            print(f"The student updated his score to {new_score}")

        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score("30.50")
