class UserProfiles:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name, age, interests):
        if user_id in self.users:
            print("User ID already exists!")
            return

        self.users[user_id] = {
            "name": name,
            "age": age,
            "interests": interests
        }

        print(f"User {name} added successfully!")

    def get_user_profile(self, user_id):
        if user_id not in self.users:
            print("User not found!")
            return None

        return self.users[user_id]

    def update_user_profile(self, user_id, name=None, age=None, interests=None):
        if user_id not in self.users:
            print("User not found!")
            return

        if name:
            self.users[user_id]["name"] = name

        if age:
            self.users[user_id]["age"] = age

        if interests:
            self.users[user_id]["interests"] = interests

        print("Profile updated successfully!")

    def display_profile(self, user_id):
        profile = self.get_user_profile(user_id)

        if profile:
            print("\n===== USER PROFILE =====")
            print(f"User ID : {user_id}")
            print(f"Name    : {profile['name']}")
            print(f"Age     : {profile['age']}")
            print(f"Interests : {', '.join(profile['interests'])}")
            print("========================\n")