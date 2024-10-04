# All of the genres
genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Romance', 'Slice of life', 
          'Supernatural', 'Horror', 'Mystery', 'Sci-Fi', 'Mecha', 'Sports', 'Shonen', 
          'Shojo', 'Isekai', 'Harem', 'Reverse Harem', 'Tragedy', 'Game']

# All of the Action Genres
Action = ["JJK", "Chainsaw Man", "One Punch Man"]


def action_function():
def adventure_function():
def comedy_function():
def drama_function():
def fantasy_function():
def romance_function():
def slice_of_life_function():
def supernatural_function():
def horror_function():
def mystery_function():
def sci-fi_function():
def mecha_function():
def sports_function():
def shonen_function():
def shojo_function():
def isekai_function():
def harem_function():
def reverse_harem_function():
def tragedy_function():    
def game_function():    

name = input("What is your name? ")
print(f"Hello, {name}, welcome to the Anime app!")
age = int(input("How old are you: "))

# Anime lists for different age groups
above18 = ["JJK", "Chainsawman", "One Piece", "Bleach", "Dragonball", "Hunter x Hunter", "Naruto"]
under18 = ["Bleach", "Dragonball", "Hunter x Hunter", "Naruto"]

# Recommend based on age
if age >= 18:
    print("You are 18 or older, here are your options.")
else:
    print("You are under 18, here are your options.")

# Display genres
print("\nGenres:")
for i, genre in enumerate(genres, 1):
    print(f"{i}. {genre}")

# Get user's genre preferences
chosen_genre1 = int(input("Choose your first favorite genre that enjoy the most (by number, ): "))
chosen_genre2 = int(input("Choose your second favorite genre that enjoy the most (by number, ): "))
chosen_genre3 = int(input("Choose your third favorite genre that enjoy the most (by number, ): "))

