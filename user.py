from file_tracker import file_tracker

class User:        
    def create_account(self, name, password):
        user_data = file_tracker.get_data("user.json")

        for user in user_data:
            if user["name"] == name:
                print("User already exists!")
                return
        
        file_tracker.append_to_file("user.json", "user" ,{"name": name, "password": password})
        print("Account created successfully!")
        
    def login(self, name, password):
        # if user exists return true
        # else return false
        user_data = file_tracker.get_data("user.json")
        
        for user in user_data:
            if user["name"] == name and user["password"] == password:
                print("Logged in successfully!")
                return True
            
            print("User does not exist!")
            return 
                        
                
        
user = User()

user.create_account("Nasif GenZ", "1234")
user.login("Nasif GesdfnZ1", "1234")