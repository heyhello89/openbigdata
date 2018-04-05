from addition_super import Restourant

class Restourant_korea(Restourant):

    def greet(self):
        print("어서오세요. 일식당입니다.")

    def menu(self):
        print("스시 나왔습니다.")

korea=Restourant_korea("한식")
korea.greet()
korea.menu()