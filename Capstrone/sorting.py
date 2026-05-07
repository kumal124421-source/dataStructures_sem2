def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j][1] < key[1]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
def friend_suggestions(user_id, profiles, graph):
    if user_id not in profiles.users:
        print("User not found!")
        return

    user_interests = set(profiles.users[user_id]["interests"])
    friends = set(graph.graph[user_id])

    suggestions = []

    for other_user in profiles.users:
        if other_user != user_id and other_user not in friends:
            other_interests = set(profiles.users[other_user]["interests"])
            score = len(user_interests.intersection(other_interests))

            if score > 0:
                suggestions.append((other_user, score))

    sorted_suggestions = insertion_sort(suggestions)

    return sorted_suggestions[:5]