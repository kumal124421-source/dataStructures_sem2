from profiles import UserProfiles
from network_graph import SocialGraph
from algorithms import bfs_shortest_path, dfs_depth_search
from sorting import friend_suggestions


profiles = UserProfiles()
graph = SocialGraph()

def demo_data():
    users = [
        ("u1", "Aman", 20, ["music", "coding", "sports"]),
        ("u2", "Riya", 21, ["movies", "music", "travel"]),
        ("u3", "Karan", 22, ["coding", "gaming", "sports"]),
        ("u4", "Neha", 20, ["dance", "music", "travel"]),
        ("u5", "Rahul", 23, ["coding", "AI", "gaming"]),
        ("u6", "Simran", 21, ["sports", "fitness", "travel"])
    ]
    for user in users:
        profiles.add_user(*user)
        graph.add_user(user[0])

connections = [
        ("u1", "u2"),
        ("u1", "u3"),
        ("u2", "u4"),
        ("u3", "u5"),
        ("u4", "u6"),
        ("u5", "u6"),
        ("u2", "u5"),
        ("u3", "u6")
    ]
for connection in connections:
        graph.add_friendship(*connection)

def menu():
    while True:
        print("\n===== SOCIAL NETWORK EXPLORER =====")
        print("1. Add User")
        print("2. View User Profile")
        print("3. Update User Profile")
        print("4. Add Friendship")
        print("5. Remove Friendship")
        print("6. Show Connections")
        print("7. Shortest Path (BFS)")
        print("8. Friends of Friends (DFS)")
        print("9. Friend Suggestions")
        print("10. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            user_id = input("User ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            interests = input("Interests (comma separated): ").split(",")

            profiles.add_user(user_id, name, age, interests)
            graph.add_user(user_id)

        elif choice == "2":
            user_id = input("Enter User ID: ")
            profiles.display_profile(user_id)

        elif choice == "3":
            user_id = input("Enter User ID: ")
            name = input("New Name: ")
            age = int(input("New Age: "))
            interests = input("New Interests: ").split(",")

            profiles.update_user_profile(user_id, name, age, interests)
        elif choice == "4":
            u1 = input("User 1: ")
            u2 = input("User 2: ")

            graph.add_friendship(u1, u2)

        elif choice == "5":
            u1 = input("User 1: ")
            u2 = input("User 2: ")

            graph.remove_friendship(u1, u2)

        elif choice == "6":
            user_id = input("Enter User ID: ")
            graph.display_connections(user_id)

        elif choice == "7":
            start = input("Start User: ")
            end = input("End User: ")
            path = bfs_shortest_path(graph.graph, start, end)

            if path:
                print("Shortest Path:", " -> ".join(path))
            else:
                print("No path found!")

        elif choice == "8":
            start = input("Start User: ")
            depth = int(input("Depth: "))

            result = dfs_depth_search(graph.graph, start, depth)
            print("Reachable Users:", result)

        elif choice == "9":
            user_id = input("Enter User ID: ")
            suggestions = friend_suggestions(user_id, profiles, graph)
            print("\nTop Friend Suggestions:")
            for user, score in suggestions:
                print(f"{user} -> Common Interests: {score}")

        elif choice == "10":
            print("Thank You!")
            break

        else:
            print("Invalid choice!")
if __name__ == "__main__":
    demo_data()

    print("\n===== DEMO MODE =====")

    profiles.display_profile("u1")
    profiles.display_profile("u2")
    profiles.update_user_profile("u2", age=22)

    print("\nBFS Query 1:")
    print(bfs_shortest_path(graph.graph, "u1", "u6"))

    print("\nBFS Query 2:")
    print(bfs_shortest_path(graph.graph, "u2", "u5"))

    print("\nDFS Query:")
    print(dfs_depth_search(graph.graph, "u1", 2))

    print("\nFriend Suggestions for u1:")
    print(friend_suggestions("u1", profiles, graph))

    menu()


