from pyscript import document, display
#club information dictionary
club_info = {
    "sc": {
        "name": "Science Club",
        "description": "A club for experiments, research, and scientific exploration.",
        "meeting_time": "Every Tuesday, 3:00 PM - 4:00 PM",
        "Venue": "Room 404",
        "moderator": "Ms. Jameelyn Maramag",
        "members": 24
    },

    "ssc": {
        "name": "Social Science Club",
        "description": "A club that delves into history, culture, and societal issues.",
        "meeting_time": "Every Tuesday and Wednesday, 3:00 PM - 4:00 PM",
        "Venue": "Room 409",
        "moderator": "Mr. Roberto Lim Jr.",
        "members": 22
    },

    "cac": {
        "name": "Communications Arts Club",
        "description": "A club focused on media, journalism, and public speaking.",
        "meeting_time": "Every Wednesday and Friday, 3:00 PM - 4:00 PM",
        "Venue": "Room 406",
        "moderator": "Ms. Yannis Fernandez",
        "members": 19
    },

    "mc": {
        "name": "Math Club",
        "description": "A club for math enthusiasts to explore concepts and solve problems.",
        "meeting_time": "Every Monday, 2:30 PM - 3:00 PM",
        "Venue": "Room 408",
        "moderator": "Mr. Nicole Gabuya",
        "members": 20
    },

    "mb": {
        "name": "Marching Band",
        "description": "A club for students interested in music and band performances.",
        "meeting_time": "Every Tuesday and Wednesday, 3:00 PM - 4:30 PM",
        "Venue": "Band Room",
        "moderator": "Mr. Emilio Alumno",
        "members": 30
    },

    "dc": {
        "name": "Dance Club",
        "description": "A club for students who love to dance and perform.",
        "meeting_time": "Every Tuesday, 3:00 PM - 5:00 PM",
        "Venue": "Teatro Preciosa",
        "moderator": "Mr. Alfred Cases",
        "members": 32
    },

    "gc": {
        "name": "Glee Club",
        "description": "A club for students who enjoy singing and musical performances.",
        "meeting_time": "Every Monday, 3:00 PM - 5:00 PM",
        "Venue": "High School Music Room",
        "moderator": "Mr. Denver Martin",
        "members": 25
    },

    "cocc": {
        "name": "Cadet Officer Candidate Course",
        "description": "A club for students interested in military training and leadership.",
        "meeting_time": "Every Wednesday, 2:30 PM - 4:30 PM",
        "Venue": "Quadrangle / Teatro Preciosa",
        "moderator": "SSgt. Jemima David PA (Res)",
        "members": 21
    },

    "vbv": {
        "name": "Volleyball Varsity",
        "description": "A club for students passionate about volleyball and competitive play.",
        "meeting_time": "Every Wednesday, 3:00 PM - 4:00 PM",
        "Venue": "Quadrangle",
        "moderator": "Mr. Adrian Ruiz",
        "members": 18
    },

    "bbv": {
        "name": "Basketball Varsity",
        "description": "A club for students who love basketball and competitive play.",
        "meeting_time": "Every Monday, 3:00 PM - 4:00 PM",
        "Venue": "Quadrangle",
        "moderator": "Mr. Adrian Ruiz",
        "members": 20
    }
}
#function to display club information
def show_club_info(e):
    selected_club = document.getElementById("Clubs").value
    info = club_info.get(selected_club)
#summary
    if info:
        summary = f"""
<b>Club Name:</b> {info["name"]}<br>
<b>Description:</b> {info["description"]}<br>
<b>Meeting Time:</b> {info["meeting_time"]}<br>
<b>Venue:</b> {info["Venue"]}<br>
<b>Moderator:</b> {info["moderator"]}<br>
<b>Number of Members:</b> {info["members"]}
        """
        document.getElementById("output").innerHTML = summary
    else:
        document.getElementById("output").innerHTML = "Club information not found."
