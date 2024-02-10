def count_words(input_text):
    """
    Function to count the number of words in a given text.
    """
    # Check if the input text is empty
    if not input_text:
        print("Error: Input text is empty.")
        exit()
    
    # Check if the input is paragraph or string
    if is_string(input_text):
        # Split the input text into words using the space character as a delimiter
        words = input_text.split()

        # Count the number of words
        word_count = len(words)

        return word_count
    #Return error  message for invalid input
    else:
        print("Error: The input should be either a paragraph or a sentence.")
        exit()

#Function to check given input is string i.e paragraph or sentence
def is_string(s):
    #check the given input is  string or not
    if  type(s)  == 'str':
        return True
    else :
        return False

def main():
    """
    Main function to handle user input and display the word count.
    """
    # Prompt the user to enter a sentence or paragraph
    input_text = input("Please enter a sentence or paragraph: ")

    # Count the number of words in the input text
    word_count = count_words(input_text)

    # Display the word count to the console
    print(f"The word count is: {word_count}")


if __name__ == "__main__":
    main()