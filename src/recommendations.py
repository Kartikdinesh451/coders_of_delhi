"""Core recommendation and data-cleaning functions for the Coders of Delhi project."""
import json
from pathlib import Path


def load_data(filename):
    """Load JSON data from a file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def clean_data(data):
    """Clean missing names, duplicate friends, inactive users, and duplicate pages."""
    data["users"] = [user for user in data["users"] if user["name"].strip()]

    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    data["users"] = [
        user for user in data["users"]
        if user["friends"] or user["liked_pages"]
    ]

    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page["id"]] = page
    data["pages"] = list(unique_pages.values())

    return data


def find_people_you_may_know(user_id, data):
    """Suggest users based on mutual-friend counts."""
    user_friends = {
        user["id"]: set(user["friends"]) for user in data["users"]
    }

    if user_id not in user_friends:
        return []

    direct_friends = user_friends[user_id]
    suggestions = {}

    for friend in direct_friends:
        for mutual in user_friends.get(friend, set()):
            if mutual != user_id and mutual not in direct_friends:
                suggestions[mutual] = suggestions.get(mutual, 0) + 1

    sorted_suggestions = sorted(
        suggestions.items(), key=lambda x: x[1], reverse=True
    )
    return [user_id for user_id, _ in sorted_suggestions]


def find_pages_you_might_like(user_id, data):
    """Recommend pages using shared interests between users."""
    user_pages = {
        user["id"]: set(user["liked_pages"]) for user in data["users"]
    }

    if user_id not in user_pages:
        return []

    user_liked_pages = user_pages[user_id]
    page_suggestion = {}

    for other_user, pages in user_pages.items():
        if other_user == user_id:
            continue

        shared_pages = user_liked_pages.intersection(pages)

        for page in pages:
            if page not in user_liked_pages:
                page_suggestion[page] = (
                    page_suggestion.get(page, 0) + len(shared_pages)
                )

    sorted_pages = sorted(
        page_suggestion.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_pages


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    data = load_data(root / "data" / "massive_data.json")

    print("People you may know for user 10:")
    print(find_people_you_may_know(10, data))

    print("\nPages you might like for user 1:")
    print(find_pages_you_might_like(1, data))
