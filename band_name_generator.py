# Band Name Generator

def get_user_input():
    """Prompt the user to enter their preferences for generating a band name."""
    print("Welcome to the BNG - Band Name Generator!")
    color = input("Enter your favorite color: ")  # Prompt for user's favorite color
    animal = input("Enter your favorite animal: ")  # Prompt for user's favorite animal
    music_style = input("Enter a word that describes your music style: ")  # Prompt for a music style descriptor
    number = input("Enter your favorite number: ")  # Prompt for user's favorite number
    return color, animal, music_style, number  # Return user inputs as a tuple

def generate_band_name(inputs):
    """Create a band name using the provided user inputs."""
    color, animal, music_style, number = inputs
    band_name = f"The {color} {animal}s"  # Combine color and animal to form a band name
    return band_name  # Return the generated band name
  
def main():
    """Main function to execute the Band Name Generator."""
    user_inputs = get_user_input()  # Get user inputs for band name generation
    band_name = generate_band_name(user_inputs)  # Generate the band name based on user inputs
    print(f"Your generated Band Name is: {band_name}")  # Print the generated band name to the user

if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly

