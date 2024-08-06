# Function to remove vowels from the input text
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

# Main function to get user input and display the result
def main():
    # Prompt the user for input
    user_input = input("Input: ")

    # Call the remove_vowels function to remove vowels from the input
    result = remove_vowels(user_input)

    # Display the output
    print("Output:", result)

# Check if the script is being run as the main module
if __name__ == "__main__":
    main()
