# All of the genres 
genres = ['Action', "Adventure", "Comedy", "Drama", "Fantasy", "Romance", "Slice of life", "Supernatural", "Horror", "Mystery", "Sci-Fi", "Mecha", "Sports", "Shonen", "Shojo", "Isekai", "Harem", "Reverse Harem", "Tragedy", "Game"]
# All of the Actions Genres
Action = ["JJK", "Chainsaw Man" "One Punch Man"]
name = input("what is your name? ")
print("Hello, welcome to the Anime app")
Date_of_birth = int(input("how old are you: "))
under18 = ["Bleach", "Dragonball", "Hunter x Hunter", "Naruto"]

Age = Date_of_birth
if Date_of_birth > 18:
        
        print(Action)
elif Date_of_birth < 18:
        print(under18)
    #genre1 = int(input("Choose 3 Generes that you enjoy the most: "))