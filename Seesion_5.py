# Task 1 = Create a list called playlist_ids with 5 song IDs (as integers) that you might see in a Spotify playlist, and print the list.

playlist_ids = [1, 2, 3, 4, 5]
print(playlist_ids)

# Task 2 = Add two more song IDs to your playlist_ids list using both append() and extend(), then print the updated list.<br><br><em><strong>Hint:</strong> Use append() for a single ID and extend() for adding multiple IDs at once.</em>

playlist_ids = [420, 421, 422, 423, 424]
playlist_ids.append(425)
list=[725,726,727,728,729]
playlist_ids.extend(list)
print(playlist_ids)

# Task 3 = Simulate removing the last played song from your playlist_ids list using pop(), and display the removed ID along with the remaining playlist.

playlist_ids = [101, 205, 309, 412, 518, 620, 725]

removed_id = playlist_ids.pop(3)

print("Removed song ID:", removed_id)
print("Remaining playlist:", playlist_ids)

# Task 4 = Create a tuple called insta_filters with 4 Instagram filter names (as strings). Try to change the first filter name and observe what error you get.<br><br><em><strong>Hint:</strong> Tuples are immutable. Note down the error message.</em>

insta_filters = ("No Filter", "8 Hour", "Filter", "Original")
print(insta_filters)
insta_filters[0] = "8 hour"     

# Task 5 = Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names) and prints which one should use a list and which should use a tuple, explaining your choice in a comment.

# Recent Zomato orders can change, so we should use a list.
zomato_orders = ["Pizza", "Burger", "Biryani"]

# Fixed IPL team names should not change, so we should use a tuple.
ipl_teams = ("CSK", "MI", "RCB", "KKR")

print("Zomato orders should use a List:", zomato_orders)
print("IPL team names should use a Tuple:", ipl_teams)