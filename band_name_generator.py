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
