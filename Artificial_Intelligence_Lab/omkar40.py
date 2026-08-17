from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='data structure'), StudentFacts(likes='operating system'))
    def AIDS(self):
        print("Suggested Career Path: AIDS Engineering")
        
    @Rule(StudentFacts(likes='maths'), StudentFacts(likes='graphics'))
    def Civil(self):
    	print("Suggested Career Path: Civil Engineering")
    	
    @Rule(StudentFacts(likes='irrigation'), StudentFacts(likes='fertiliser'))
    def Agriculture(self):
    	print("Suggested Career Path: Agriculture Engineering")


def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    
    print(" | Maths ")
    print(" | physics ")
    print(" | programming ")
    print(" | biology ")
    print(" | chemistry ")
    print(" | data structure ")
    print(" | operating system ")

    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()


	


