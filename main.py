# This file stores a dictionary of school club information
# and includes a function that displays all details
# about a selected club.
#
# The dictionary contains:
# - Club Name
# - Description
# - Meeting Time
# - Location
# - Club Moderator
# - Number of Members
#
# The get_club_info() function returns a formatted string
# containing all the information about the chosen club.




# Dictionary: clubs
# - Each key is a club name.
# - Each value is another dictionary storing that club’s
#   description, meeting time, location, moderator, and
#   number of members.


clubs = {
    "Chess Club": {
        "Description": "A club for chess enthusiasts of all skill levels.",
        "Meeting Time": "Every Wednesday 3:30–5:00 PM",
        "Location": "Room 405",
        "Club Moderator": "Mr. Santos",
        "Members": 20
    },
    "Music Club": {
        "Description": "A club for students who enjoy singing or playing instruments.",
        "Meeting Time": "Every Friday 4:00–5:30 PM",
        "Location": "Music Room 2",
        "Club Moderator": "Ms. Dela Cruz",
        "Members": 35
    },
    "Dance Club": {
        "Description": "A club open for all dance styles and performances.",
        "Meeting Time": "Every Tuesday 3:30–5:00 PM",
        "Location": "Gymnasium",
        "Club Moderator": "Coach Ramirez",
        "Members": 28
    }
}



# Function: get_club_info(club_name)

# Purpose:
#   Returns all club details in a nicely formatted string.

# Parameter:
#   club_name (string) – The name of the club to search for.

# Process:
#   Check if the club exists inside the dictionary.
#   If it exists, format the information into readable text.
#   If it doesn't exist, return a message saying so.

# Returns: A multi-line text containing all club details.


def get_club_info(club_name):
    if club_name in clubs:
        info = clubs[club_name]

        # Start with the club name as a title
        output = f"{club_name}\n"

        # Loop through all details inside the selected club
        for key, value in info.items():
            output += f"{key}: {value}\n"

        return output
    else:
        return "Club not found."

# print(get_club_info("Chess Club"))
# print(get_club_info("Music Club"))
# print(get_club_info("Dance Club"))
