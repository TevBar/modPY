# main.py

import text_utils as tu  # type: ignore # Import the custom module with an alias

def main():
    print("Welcome to the Text Utilities Program!")
    
    # User input
    user_string = input("Enter a string: ")
    
    # Reverse the string
    reversed_string = tu.reverse_string(user_string)
    print(f"Reversed String: {reversed_string}")
    
    # Capitalize the string
    capitalized_string = tu.capitalize_string(user_string)
    print(f"Capitalized String: {capitalized_string}")

if __name__ == "__main__":
    main()
