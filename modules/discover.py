def menu():
    while True:
        print("\n--- Discover Section ---")
        print("1. Local dance events or sessions")
        print("2. Dance crews or studios in a city")
        print("3. Kid-friendly events/classes")
        print("4. Popular tracks/music trends")
        print("5. Back to Main Menu")

        choice = input("> ")

        if choice == "1":
            print("📅 Placeholder: List of local events")
        elif choice == "2":
            print("👯 Placeholder: Dance crews/studios")
        elif choice == "3":
            print("🧒 Placeholder: Kid-friendly events")
        elif choice == "4":
            print("🎵 Placeholder: Trending music")
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")