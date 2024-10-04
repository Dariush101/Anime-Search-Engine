# All of the genres
genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Romance', 'Slice of life', 
          'Supernatural', 'Horror', 'Mystery', 'Sci-Fi', 'Mecha', 'Sports', 'Shonen', 
          'Shojo', 'Isekai', 'Harem', 'Reverse Harem', 'Tragedy', 'Game']

# All of the Action Genres



def action_function():
    Action = ["JJK", "Chainsaw Man", "One Punch Man"]
    print(Action)
    
def adventure_function():
    Adventure = ["One piece","Hunter x Hunter","Dragon Ball"]
    print(Adventure)

def comedy_function():
    Comedy = ["Spy x Family","Mob Psycho","Konosuba"]
    print(Comedy)

def drama_function():
    Drama = ["classroom of the elite","Date a live ","charlotte "]
    print(Drama)

def fantasy_function():
    Fantasy = ["Overlord","Black clover","Fairy tail "]
    print(Fantasy)

def romance_function():
    Romance = ["My teenage romantic comedy","Alya somethimes hides her feleings in Russian","Darling inf franx"]
    print(Romance)

def slice_of_life_function():
    Slice_of_life = ["Komi can't communicate","Clannad","Fruits Basket "]
    print(Slice_of_life)

def supernatural_function():
    Supernatural = ["In/spectre","Fate/stay night","Demon Slayer"]
    print(Supernatural)

def horror_function():
    Horror = ["Eldien lied","Berserk","tokyo ghoul"]
    print(Horror)

def mystery_function():
    Mystery = ["Bungou stray dogs","Death Note","Jojos bizzare adventure"]
    print(Mystery)

def sci_fi_function():
    Sci_Fi = ["Cyberpunk edgerunners","sword art online","steins gate"]
    print(Sci_Fi)

def mecha_function():
    Mecha = ["Mobile Gundum","Gurren luagan","kill la kill"]
    print(Mecha)

def sports_function():
    sports = ["Blue lock","Hajime no ippo","Kuroko's basketball"]
    print(sports)

def shonen_function():
    shonen = ["Bleach","My hero acedemia","Dr. stone"]
    print(shonen)

def shojo_function():
    shojo = ["sailor moon","The irregular at a magic high school","whispers of the heart"]
    print(shojo)

def isekai_function():  
    isekai = ["That time I got reicnarnated as a slime","The Misfit of Demon King Academy","Eminence in shadow"]
    print(isekai)
    
def harem_function():
    Harem = ["High school dxd","I got a cheat skill in another world","Danmachi"]
    print(Harem)

def reverse_harem_function():
    Reverse_harem = ["Vampire knight","Code: Realize","Yona of the dawn"]
    print(Reverse_harem)

def tragedy_function():
    Tragedy = ["Alucard","Devilman crybaby","Code geass"]
    print(Tragedy)

def game_function(): 
    Game = ["Pokemon","Yu-gi-oh","Beyblade"]
    print(Game)

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

# Create a mapping of genre numbers to functions
genre_functions = {
    1: action_function,
    2: adventure_function,
    3: comedy_function,
    4: drama_function,
    5: fantasy_function,
    6: romance_function,
    7: slice_of_life_function,
    8: supernatural_function,
    9: horror_function,
    10: mystery_function,
    11: sci_fi_function,
    12: mecha_function,
    13: sports_function,
    14: shonen_function,
    15: shojo_function,
    16: isekai_function,
    17: harem_function,
    18: reverse_harem_function,
    19: tragedy_function,
    20: game_function,
}

# Get the unique chosen genres
chosen_genres = set([chosen_genre1, chosen_genre2, chosen_genre3])

# Loop through chosen genres and call the corresponding function if it exists
for genre in chosen_genres:
    if genre in genre_functions:
        genre_functions[genre]()
