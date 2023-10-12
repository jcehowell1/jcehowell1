date = input("Enter today's date: ")
mood = input("How would you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"python/journal/{date}.txt", "w") as file:
          file.write("Mood Rating: " + mood + 2 * "\n")
          file.write(thoughts)