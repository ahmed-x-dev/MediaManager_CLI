import json
import os

FILENAME = "data/library.json" # will save inside 'data' folder

# ---------- Load library at startup ----------

def load_library():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "games": {
            "playing": [],
            "ended": [],
            "want_to_play": [],
            "end_it_later": [],
            "dont_want_to_end": []
        },
        "manga": {
            "reading": [],
            "read": [],
            "want_to_read": [],
            "end_it_later": [],
            "dont_want_to_end": []
        },
        "movies": {
            "watching": [],
            "watched": [],
            "want_to_watch": [],
            "end_it_later": [],
            "dont_want_to_end": []
        }
    }

library = load_library()

# ---------- Save library ----------

def save_library():
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(library, f, indent=4, ensure_ascii=False)

# ----------support functions------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_item(section):

    ds=(library[section])
    for key, value in ds.items():
        print(f"{key}: {value}")


def choose_category(section,type):
    clear_screen()
    """Show available categories for a section and return chosen one."""
    if section not in library:
        print("❌ Invalid section.")
        return None

    categories = list(library[section].keys())

    # Print numbered list
    print(f"{type} {section.replace("s","")} {"from" if type == "delet" else "to"}:")
    for i, category in enumerate(categories, start=1):
        print(f"{i} - {category}")

    # Get choice
    choice = input("Choose: ").strip()
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(categories):
            return categories[choice - 1]

    print("❌ Invalid choice.")
    return None



# ------------Core functions------------



def add_item(section):
    clear_screen()
    os.system('cls' if os.name == 'nt' else 'clear')

    choice = input("1- Online\n2- Manually\nChoice: ").strip()

    clear_screen()
    if choice == "1":
        import info_from_APIs
        print("Fetching data from online source...")

        if section == "games":
            game=info_from_APIs.get_game_info(input("Enter the game name: "))
            library[section][choose_category("games","add")].append(game)
            save_library()
    
        if section == "manga":
            manga= info_from_APIs.get_manga_info(input("Enter the manga name: "))
            library[section][choose_category("manga","add")].append(manga)
            save_library()
            
        if section == "movies":

            movie= info_from_APIs.shows_info(input("Enter the movie/series name: "))
            library[section][choose_category("movies","add")].append(movie)
            save_library()


    elif choice == "2":
        print("Adding data manually...")
        item = {
            "Source": section,
            "Name": input("Name: ").strip() or "Unknown",
            "Released": input("Released (year or date): ").strip() or "Unknown",
            "Rating": input("Rating: ").strip() or "N/A",
            "Genres": [g.strip() for g in input("Genres (comma-separated): ").split(",") if g.strip()],
            "plot": input("Enter the plot"),
            "Image": input("Image URL: ").strip() or "N/A",
        }
        # Section-specific fields
        if section == "games":
            item["Platforms"] = [g.strip() for g in input("platforms (comma-separated): ").split(",") if g.strip()]
        elif section == "movies":
            item["Runtime"] = input("Enter the runtime: ").strip() or "N/A"
        elif section == "manga":
            item["Chapters"] = input("Enter the number of chapters: ").strip() or "N/A"

        
        choice = input("\nDo you want to change any field? (yes/no): ").strip().lower()
        if choice == "yes":
            while True:
                for key in item.keys():
                    if key == "Source":  # Cannot change source
                        continue

                    new_value = input(f"Enter new value for '{key}' (leave empty to keep current): ").strip()
                    if new_value:
                        if key == "Genres":
                            item[key] = [genre.strip() for genre in new_value.split(",")]
                        else:
                            item[key] = new_value

                print(f"\n✅ Updated {section.replace("s","")} Information:")
                for key, value in item.items():
                    print(f"{key}: {value}")

                confirm = input("\nAre these changes good? (yes/no): ").strip().lower()
                if confirm == "yes":
                    break
        library[section][choose_category(section,"add")].append(item)
        save_library()
                
    else:
        print("❌ Invalid choice.")


def delete_item(section):
    clear_screen()
    """Delete an item from a chosen category in the given section."""
    if section not in library:
        print("❌ Invalid section.")
        return
    
    category = choose_category(section,"delet")
    if category is None:
        return
    
    items = library[section][category]
    if not items:
        print("❌ No items to delete in this category.")
        return

    # Show items with index numbers
    print(f"\nItems in {section} → {category}:")
    for i, item in enumerate(items, start=1):
        # Try to display a friendly name if available
        name = item.get("Name") if isinstance(item, dict) else str(item)
        print(f"{i} - {name}")
    
    choice = input("\nEnter the number of the item to delete (or 'cancel'): ").strip()
    if choice.lower() == "cancel":
        print("❎ Deletion cancelled.")
        return
    
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(items):
            removed = items.pop(index)
            save_library()
            print(f"✅ Deleted: {removed.get('Name', removed) if isinstance(removed, dict) else removed}")
        else:
            print("❌ Invalid index.")
    else:
        print("❌ Invalid input.")


def edit(section):
    clear_screen()
    """Edit the info of an item OR change its category."""
    if section not in library:
        print("❌ Invalid section.")
        return
    
    # Step 1: Ask which action to take
    action = input("\nWhat do you want to do?\n1 - Edit info\n2 - Change category\n> ").strip()
    if action not in ["1", "2"]:
        print("❌ Invalid choice.")
        return
    
    # Step 2: Choose category
    category = choose_category(section, "edit" if action == "1" else "move")
    if category is None:
        return
    
    items = library[section][category]
    if not items:
        print("❌ No items in this category.")
        return
    
    # Step 3: Choose item
    print(f"\nItems in {section} → {category}:")
    for i, item in enumerate(items, start=1):
        name = item.get("Name") if isinstance(item, dict) else str(item)
        print(f"{i} - {name}")
    
    choice = input("\nEnter the number of the item (or 'cancel'): ").strip()
    if choice.lower() == "cancel":
        print("❎ Cancelled.")
        return
    if not choice.isdigit() or not (1 <= int(choice) <= len(items)):
        print("❌ Invalid choice.")
        return
    
    index = int(choice) - 1
    item = items[index]

    if not isinstance(item, dict):
        print("❌ This item format cannot be edited (not a dictionary).")
        return
    
    # Step 4: Perform the selected action
    if action == "1":  # Edit info
        print("\n--- Edit Info ---")
        for key in list(item.keys()):
            if key == "Source":  # Cannot change source type
                continue
            new_value = input(f"Enter new value for '{key}' (leave empty to keep '{item[key]}'): ").strip()
            if new_value:
                if key in ["Genres", "Platforms"]:  # Convert comma-separated to list
                    item[key] = [v.strip() for v in new_value.split(",") if v.strip()]
                else:
                    item[key] = new_value
            

        for key, value in item.items():
            print(f"{key}: {value}")

        choice = input("\nAre these changes good? (yes/no): ").strip().lower()
        if choice == "no":
            while True:
                for key in item.keys():
                    if key == "Source":  # Cannot change source
                        continue

                    new_value = input(f"Enter new value for '{key}' (leave empty to keep current): ").strip()
                    if new_value:
                        if key == "Genres":
                            item[key] = [genre.strip() for genre in new_value.split(",")]
                        else:
                            item[key] = new_value

                
                for key, value in item.items():
                    print(f"{key}: {value}")
                ask = input("are these changes good? (yes/no)").lower().strip()
                if ask == "yes":
                    break

        save_library()
        print("✅ Info updated successfully.")

    elif action == "2":  # Change category only
        new_category = choose_category(section, "move")
        if new_category and new_category != category:
            library[section][category].pop(index)
            library[section][new_category].append(item)
            save_library()
            print(f"✅ Moved to {new_category}.")
        else:
            print("❌ Invalid category or same category chosen.")




