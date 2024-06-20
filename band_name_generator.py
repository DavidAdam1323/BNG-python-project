# Band Name Generator

def get_user_input():
  print("Welcome to the BNG - Band Name Generator!")
  color = input("Enter your favorite color: ")
  animal = input("Enter your favorite animal: ")
  music_style = input("Enter a word that describes your music style: ")
  number = input("Enter your favorite number: ")
  return color, animal, music_style, number

def generate_band_name(inputs):
  color, animal, music_style, number = inputs
  band_name = f"The {color} {animal}s"
  return band_name
  
def main():
  user_inputs = get_user_input()
  band_name = generate_band_name(user_inputs)
  print(f"Your generated Band Name is: {band_name}")

if __name__ == "__main__": main()

# 1. Start

# 2. Define function: get_user_input() ✅
#     a. Print welcome message ✅
#     b. Ask user for their favorite color ✅
#     c. Ask user for their favorite animal ✅
#     d. Ask user for a word that describes their music style ✅
#     e. Ask user for their favorite number ✅
#     f. Return collected inputs ✅

# 3. Define function: generate_band_name(inputs) ✅
#     a. Extract individual inputs from the input list ✅
#     b. Combine inputs in a creative way to form a band name ✅
#         - Example: "The [Favorite Color] [Favorite Animal]s" ✅
#         - Or: "[Music Style] [Favorite Animal] [Number]"
#     c. Return generated band name ✅

# 4. Main program execution ✅
#     a. Call get_user_input() to collect inputs from the user ✅
#     b. Store returned inputs ✅
#     c. Call generate_band_name(inputs) with the collected inputs ✅
#     d. Store returned band name ✅
#     e. Print the generated band name ✅

# 5. End
