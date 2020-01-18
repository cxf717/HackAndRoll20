class passenger(object):
    def __init__(self, role, description):
        self.role = role
        self.description = description

    def role(self):
        print(self.role)
        # return self.role

    def description(self):
        print(self.description)
        # return self.description

class DurianLover(passenger):
    def __init__(self):
            super().__init__("Durian Lover", "You are the Durian Lover!" + "\U0001f60d"
                             
class PretendSleeper(passenger):
    def __init__(self):
            super().__init__("Pretend Sleeper", "You are the Pretend Sleeper!"+ "\U0001f634")
            

	

