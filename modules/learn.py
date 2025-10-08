def menu():
    while True:
        print("\n--- Learn Section ---")
        print("1. Popping styles (Waving, Tutting, etc.)")
        print("2. History and cultural background")
        print("3. Advice from mentors")
        print("4. Back to Main Menu")

        choice = input("> ")

        if choice == "1":
            print("✨ Placeholder: Info about Popping styles")
        elif choice == "2":
            print("📜 Placeholder: Cultural history of Popping")
        elif choice == "3":
            print("💡 Placeholder: Mentor advice section")
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")