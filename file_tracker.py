import os
import json

data = {
    "name": "Nasif",
    "age": 25,
    "skills": ["Python", "JavaScript", "AI/ML"],
    "is_developer": True
}

class File_Tracker:        
    def create_file(self, filename, content):
        content["id"] = 0
        if not os.path.exists(filename):
            with open(filename, "w") as file:
                json.dump([content], file,  indent=4)
                print(f"File '{filename}' created successfully.")
        else:
            print(f"File '{filename}' already exists.")
            
    def get_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return data
        
    def append_to_file(self, filename, target, content):
        if os.path.exists(filename):
            prev_data = self.get_data(filename)[target]                        
            prev_data.append({"id": len(prev_data) + 1, **content})
            
            with open(filename, "w") as file:
                json.dump(prev_data, file,  indent=4)
                print(f"File '{filename}' updated successfully.")
            
        else:
            print(f"File '{filename}' does not exist.")
        
    def delete_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' does not exist.")
            

file_tracker = File_Tracker()


