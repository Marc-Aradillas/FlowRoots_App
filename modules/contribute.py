def menu():
    while True:
        print("\n--- Contribute Section ---")
        print("1. Submit a question or suggestion")
        print("2. Add an event or session")
        print("3. Share a playlist or track")
        print("4. List your dance class or studio")
        print("5. Back to Main Menu")

        choice = input("> ")

        if choice == "1":
            print("📨 Placeholder: Submit suggestion")
        elif choice == "2":
            print("➕ Placeholder: Add event")
        elif choice == "3":
            print("🎶 Placeholder: Share playlist")
        elif choice == "4":
            print("🏫 Placeholder: List dance class/studio")
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")