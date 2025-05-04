import json

# Function to save the library to a JSON file
def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)
    print("Library saved to library.json")

# Function to load the library from a JSON file
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Initialize library (load existing or start empty)
library = load_library()

# Main Menu Loop
while True:
    print("\nLibrary Menu:")
    print("1. View Books")
    print("2. Search Books")
    print("3. Add Book")
    print("4. Mark Book as Read")
    print("5. Delete Book")
    print("6. Edit Book")
    print("7. Save Library")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == "1":
        print("\nBooks in Library:")
        for book in library:
            status = "Read" if book["read"] else "Unread"
            authors = ", ".join(book["authors"])
            genres = ", ".join(book["genres"])
            print(f"- {book['title']} | Authors: {authors} | Genres: {genres} | Status: {status}")

    elif choice == "2":
        search = input("Enter title to search: ")
        found = False
        for book in library:
            if book["title"].lower() == search.lower():
                status = "Read" if book["read"] else "Unread"
                authors = ", ".join(book["authors"])
                genres = ", ".join(book["genres"])
                print(f"{book['title']} by {authors} (Genres: {genres}) - Status: {status}")
                found = True
        if not found:
            print(f"{search} not found in library.")

    elif choice == "3":
        new_title = input("Enter the title of the new book: ")

        new_authors = input("Enter the author(s) (comma-separated): ").split(",")
        new_authors = [a.strip() for a in new_authors]

        new_genres = input("Enter the genre(s) (comma-separated): ").split(",")
        new_genres = [g.strip() for g in new_genres]

        read_status_input = input("Have you read it? (yes/no): ").strip().lower()
        read_status = read_status_input == "yes"

        library.append({
            "title": new_title,
            "authors": new_authors,
            "genres": new_genres,
            "read": read_status
        })
        print(f"'{new_title}' added to library.")

    elif choice == "4":
        mark_title = input("Enter the title to mark as read: ")
        updated = False
        for book in library:
            if book["title"].lower() == mark_title.lower():
                book["read"] = True
                print(f"Marked '{book['title']}' as read.")
                updated = True
        if not updated:
            print(f"{mark_title} not found in library.")

    elif choice == "5":
        delete_title = input("Enter the title to delete: ")
        deleted = False
        for book in library:
            if book["title"].lower() == delete_title.lower():
                library.remove(book)
                print(f"Deleted '{delete_title}' from the library.")
                deleted = True
                break
        if not deleted:
            print(f"{delete_title} not found in library.")

    elif choice == "6":
        edit_title = input("Enter the title of the book to edit: ")
        found = False
        for book in library:
            if book["title"].lower() == edit_title.lower():
                print(f"Editing '{book['title']}'")

                new_title = input("New title (leave blank to keep current): ").strip()
                if new_title:
                    book["title"] = new_title

                new_authors = input("New authors (comma-separated, leave blank to keep current): ").strip()
                if new_authors:
                    book["authors"] = [a.strip() for a in new_authors.split(",")]

                new_genres = input("New genres (comma-separated, leave blank to keep current): ").strip()
                if new_genres:
                    book["genres"] = [g.strip() for g in new_genres.split(",")]

                print("Book updated successfully.")
                found = True
                break
        if not found:
            print(f"'{edit_title}' not found in the library.")

    elif choice == "7":
        save_library(library)

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
