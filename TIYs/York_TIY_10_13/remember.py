from pathlib import Path
import json

def get_stored_details(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_details = json.loads(contents)
        return user_details
    else:
        return None

def get_new_username(path):
    """Prompt for a new username and a few details about the user."""
    user_details = {}
    username = input("What is your name? ")
    user_place = input("Where do you live? ")
    user_color = input("What is your favorite color? ")

    user_details[username] = {"Place" : user_place, "Color" : user_color}

    contents = json.dumps(user_details)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    user_details = get_stored_details(path)
    if user_details:
        for name in user_details.keys():
            print(f"Welcome back, {name}!")
            for key, detail in user_details[name].items():
                if key == "Place":
                    print(f"You live in {detail}.")
                elif key == "Color":
                    print(f"Your favorite color is {detail}.")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
