class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user_id):
        if user_id not in self.graph:
            self.graph[user_id] = []

    def add_friendship(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            print("One or both users do not exist!")
            return

        if user2 not in self.graph[user1]:
            self.graph[user1].append(user2)
            self.graph[user2].append(user1)
            print(f"Friendship added between {user1} and {user2}")

    def remove_friendship(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            print("One or both users do not exist!")
            return

        if user2 in self.graph[user1]:
            self.graph[user1].remove(user2)
            self.graph[user2].remove(user1)
            print(f"Friendship removed between {user1} and {user2}")
        else:
            print("Friendship does not exist!")

    def get_friends(self, user_id):
        if user_id not in self.graph:
            print("User not found!")
            return []

        return self.graph[user_id]

    def display_connections(self, user_id):
        if user_id not in self.graph:
            print("User not found!")
            return

        print(f"\nConnections of {user_id}:")
        
        if not self.graph[user_id]:
            print("No connections found.")
        else:
            for friend in self.graph[user_id]:
                print(friend)