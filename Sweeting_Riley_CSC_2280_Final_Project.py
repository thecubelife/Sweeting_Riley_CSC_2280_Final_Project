import string # Import ASCII Characters
import random # Randomly Generated Indicies
import enchant # Compare to English Dictionary
import pyperclip # Copy to Clipboard

# Variables
break_main_menu = False # Break from Outer Loop (Option 4)
break_second_menu = False # Break from Inner Loop (Select Task)
count = 0 # Defines count of string splices found in English Dictionary
d = enchant.Dict("en_US") # Defines English Dictionary
str = "" # Defines how to join list

# Defines List of ASCII Characters (Alphabet & Special Characters)
alphabet = list(string.printable)
alphabet = alphabet[:95] # Removes 'Unsavory' Characters like "\n" and "\t"
alphabet.remove("\\") # Removes a Double Character that would inhibit decrytpion

# Defined Functions

def yes_or_no(message):
    while True:
        print(message, end = "") # Prompted message is different for each function that called it
        response = input()
        print()
        if response.lower() == "yes": # .lower() converts to lowercase
            return True # Yes
        elif response.lower() == "no":
            return False # No
        else: # Invalid Response
            print("You have entered an invalid response. Please enter \"Yes\" or \"No\".")
            print() # Does not return anything so that the function will repeat

def select_task(): # Asks User if they would like to select another task
    while True: # Set question to repeat
        message = "Would you like to select another task? "
        repeat_choice = yes_or_no(message) # Returns TRUE (YES) or FALSE (NO)
        
        global break_main_menu # <--- Makes Variables Global (Not Local to Function)
        global break_second_menu
        
        if repeat_choice: # Just Breaks from Second Menu. Repeat Program
            break_second_menu = True
            break
        else: # repeat_choice == "no": # Completely break program. Do not repeat program
            break_main_menu = True
            break_second_menu = True
            break

def key_in_range():
    while True:
        print("Input a numerical key here (Between 1 and 94 inclusive): ", end = "")
        key = input() # prompt user to input key
        
        # Determines if Key is a digit
        if key.isdigit():
            key = int(key) # Integerizes Key
        else:
            print("You have entered an invalid response. Please enter a number between \"1\" and \"94\".")
            print()
            continue # Skips rest of iteration

        # Determines if Key is in range
        if (key > 94) or (key < 1): # Makes sure key is within range and a digit
            print("You have entered an invalid response. Please enter a number between \"1\" and \"94\".")
            print()
        else: # In Range
            print()
            break
    return key # Returns Key value once proper key is entered
        
def copy_clipboard(coded_message): # Ask user to copy encoded/decoded message to clipboard
    while True:
        message = "Would you like to copy the message to your clip board? "
        answer = yes_or_no(message)
        if answer:
            pyperclip.copy(str.join(coded_message)) # Copies message to clipboard
            print("** Message Copied to Clipboard **")
            print()
            break
        else:
            print("** Message NOT Copied to Clipboard **") # Does not copy message to clipboard
            print()
            break
        
def copy_article_clipboard(url): # Similar to Copy Clipboard function, but copies article instead of coded message
    while True:
        message = "Would you like to copy the Wikipedia article to your clipboard? "
        answer = yes_or_no(message) # Returns YES or NO (TRUE or FALSE)
        if answer: # IF TRUE/YES
            pyperclip.copy(str.join(url)) # Copies article to clipboard
            print("** Article Copied to Clipboard **")
            print()
            break
        else: # IF NO/FALSE
            print("** Article NOT Copied to Clipboard **") # Does not copy article to clipboard
            print()
            break
          
# -------------------------------------------------------------------------------------------------------
# Beginning of Program
# -------------------------------------------------------------------------------------------------------
while True: # <--- Set Program to Loop until Broken (Option 4)
    # Greet User with Main Menu
    print("---------------------------------------------------------------")
    print("|{:^61}|".format("Welcome to my Cyrptography Program!")) # <--- Center Align
    print("---------------------------------------------------------------")
    print("| What would you like to do?                                  |")
    print("|  1. Encrypt a Message                                       |")
    print("|  2. Decrypt a Message                                       |")
    print("|  3. Brute Force a Ciphertext (ONLY WORKS FOR CAESAR CIPHER) |")
    print("|  4. History of Caesar & Vigenere Cipher                     |")
    print("|  5. Exit                                                    |")
    print("---------------------------------------------------------------")
    
    while True: # <--- Ask Repeatedly until Valid Input is Given
        print("Enter your choice: ", end = "")
        main_choice = input()
        print() # <--- Spacing
        
        # -----------------------------------------------------------------------------------------------
        # ENCRYPT A PLAIN TEXT
        # -----------------------------------------------------------------------------------------------
        if main_choice == "1":
            # Encryption Menu
            print("You have chosen to: Encrypt a Message")
            print() # Provides User with Secondary Options Menu
            print("----------------------------------------------------")
            print("|{:^50}|".format("Encryption Program"))
            print("----------------------------------------------------")
            print("| What would you like to do?                       |")
            print("|  1. Encrypt using Caesar Cipher                  |")
            print("|  2. Encrypt using Vigenere Cipher                |")
            print("|  3. Exit                                         |")
            print("----------------------------------------------------")
            
            while True: # Set to repeat until broken by completing full iteration
                print("Enter your choice: ", end = "")
                second_choice = input()
                print() # <--- Spacing
                
                if second_choice == "1":
                    # Ceaser Encryption Option
                    print("----------------------------------------------------")
                    print("|{:^50}|".format("Ceaser Encryption Program"))
                    print("----------------------------------------------------")
                      
                    # Ask User to Input a Plain Text Message
                    print("Enter message to be encrypted here: ", end = "")
                    plain_text = input()
                    plain_message = list(plain_text) # <--- Converts String to List
                    print() # <--- Spacing

                    # Ask User to Input a Numerical Key
                    key = key_in_range()

                    # Defines Rotated (CODED) Alphabet based on Key (Key = Number of Rotations)
                    rotated_alphabet = alphabet[key:] + alphabet[:key] # If Key = 3, [A, B, C, D, E] = [D, E, A, B, C]

                    # Defines List for Final Encoded Message
                    encoded_message = []

                    # Convert Plain Text Message to Cipher Text Message -----------------------------------------

                    # Number of Characters in Plain Text Message
                    positions = len(plain_message)

                    # Convert Every Character to Cipher Text Character
                    for index in range(positions):
                        
                        # Finds Letter Associated with Given Index of Plain Message List
                        letter = plain_message[index]
                        
                        # Finds Index of Letter in Alphabet List
                        index_letter_alphabet = alphabet.index(letter)
                        
                        # Finds Letter Associated with Index in Rotated Alphabet List
                        coded_character = rotated_alphabet[index_letter_alphabet]
                        
                        # Appends Coded Letter to List 
                        encoded_message.append(coded_character)
                        
                    # Prints Encrypted Message
                    print("Here is your encrypted message: {}".format(str.join(encoded_message))) # Converts List to String
                    print("Remember to save your key, as it is needed to decrypt the message! Key: {}".format(key))
                    print()
                    
                    # Asks User is they wish to Copy Message to Clipboard
                    copy_clipboard(str.join(encoded_message))
                    
                    # Ask User if they wish to do anything else
                    select_task()
                    
                elif second_choice == "2":
                    # Vigenere Encryption Option
                    print("----------------------------------------------------")
                    print("|{:^50}|".format("Vigenere Encryption Program"))
                    print("----------------------------------------------------")
                    
                    # Ask User to Input a Plain Text Message
                    print("Enter message to be encrypted here: ", end = "")
                    message = input()
                    message = list(message) # <--- Converts String to List
                    message_positions = len(message)
                    print() # <--- Spacing

                    # Ask User to Enter Key Passphrase
                    print("Please enter a secret passphrase to encrypt the message here: ", end = "")
                    key = key_saved = input() # Saves another copy of key for printing purposes
                    key = list(key)
                    print()

                    # Set Key Length Greater Than or Equal to Message Length
                    while True:
                        key_positions = len(key)
                        if key_positions >= message_positions:
                            break
                        else: # Key Length Less than Message Length
                            key = key * 2
                            
                    # Reduces key length equal to message length
                    key = key[:message_positions]

                    # Defines Encoded Character List
                    encoded_message = []

                    for index in range(message_positions): # In range of the length of the plain text message
                        
                        # Given an Index, finds the matching characters in the message and passphrase
                        message_character = message[index] # Message Character For Index i
                        key_character = key[index] # Key Character for Index i
                        
                        current_key = alphabet.index(key_character) # Returns position of key character in alphabet.
                        # ^^ This is the value which defines how far the letter rotates
                        current_alphabet = alphabet[current_key:] + alphabet[:current_key]
                        # ^^ Defines the alphabet for the current key. 
                        
                        alphabet_index = alphabet.index(message_character) # Gives index of character in alphabet
                        encoded_character = current_alphabet[alphabet_index] # Returns character of above index of the current/rotated alphabet
                        
                        encoded_message.append(encoded_character) # Appends encoded character to list
                    
                    # Prints Encrypted Message
                    print("Here is your encrypted message: {}".format(str.join(encoded_message))) # Converts List to String
                    print("Remember to save your key, as it is needed to decrypt the message! Key: {}".format(key_saved))
                    print()
                    
                    # Asks User if they wish to Copy Message to Clipboard
                    copy_clipboard(str.join(encoded_message))
                    
                    # Ask User if they wish to do anything else
                    select_task()
                
                elif second_choice == "3":
                    # Exit Secondary Menu
                    print("You have chosen to exit the menu.")
                    print()
                    break_second_menu = True
                    break
                
                else: # Second Choice not in range (1, 3)
                    print("You have entered an invalid response. Please enter 1, 2, or 3.")
                    print()
                    continue
                
                # Sends back to outer loop, 
                break
                    
        # -----------------------------------------------------------------------------------------------
        # DECRYPT A CIPHERTEXT
        # -----------------------------------------------------------------------------------------------
        elif main_choice == "2":
            # Decryption Menu
            print("You have chosen to: Decrypt a Message")
            print()
            print("----------------------------------------------------")
            print("|{:^50}|".format("Decryption Program"))
            print("----------------------------------------------------")
            print("| What would you like to do?                       |")
            print("|  1. Decrypt using Caesar Cipher                  |")
            print("|  2. Decrypt using Vigenere Cipher                |")
            print("|  3. Exit                                         |")
            print("----------------------------------------------------")
            
            while True: # Repeat until full iteration occurs
                print("Enter your choice: ", end = "")
                second_choice = input()
                print() # <--- Spacing
                
                if second_choice == "1":
                    # Ceaser Decryption Option
                    print("----------------------------------------------------")
                    print("|{:^50}|".format("Ceaser Decryption Program"))
                    print("----------------------------------------------------")
                    
                    # Ask User to Input a Cipher Text Message
                    print("Enter the message to be decrypted here: ", end = "")
                    cipher_text = input()
                    cipher_message = list(cipher_text) # <--- Converts String to List
                    print() # <--- Spacing

                    # Ask User to Input a Numerical Key
                    key = key_in_range()

                    # Defines Rotated (CODED) Alphabet based on Key (Key = Number of Rotations)
                    rotated_alphabet = alphabet[key:] + alphabet[:key] # If Key = 3, [A, B, C, D, E] = [D, E, A, B, C]

                    # Defines List for Final Decoded Message
                    decoded_message = []

                    # Convert Cipher Text Message to Plain Text Message -----------------------------------------------------

                    # Number of Characters in Cipher Text Message
                    positions = len(cipher_message)

                    # Convert Every Character to Plain Text Character
                    for index in range(positions):
                        
                        # Finds Character Associated with Given Index of Cipher Message List
                        character = cipher_message[index]
                        
                        # Finds Index of Character in Rotated Alphabet List
                        index_letter_rotated_alphabet = rotated_alphabet.index(character)
                        
                        # Finds Character Associated with Index in Rotated Alphabet List
                        decoded_character = alphabet[index_letter_rotated_alphabet]
                        
                        # Appends Coded Character to List 
                        decoded_message.append(decoded_character)
                    
                    # Prints Decrypted Message
                    print("Here is the decrypted message: {}".format(str.join(decoded_message)))
                    print()
                    
                    # Asks User is they wish to Copy Message to Clipboard
                    copy_clipboard(str.join(decoded_message))
                    
                    # Ask User if they wish to do anything else
                    select_task()
                    
                elif second_choice == "2":# Defines Encoded Character List
                    # Vigenere Encryption Option
                    print("----------------------------------------------------")
                    print("|{:^50}|".format("Vigenere Decryption Program"))
                    print("----------------------------------------------------")
                    
                    # Ask User to Input a Plain Text Message
                    print("Enter the message to be decrypted here: ", end = "")
                    message = input()
                    message = list(message) # <--- Converts String to List
                    message_positions = len(message)
                    print() # <--- Spacing

                    # Ask User to Enter Key Passphrase
                    print("Please enter the secret passphrase used to encrypt the message here: ", end = "")
                    key = key_saved = input() # Saves another copy of key for printing purposes
                    key = list(key)
                    print()

                    # Set Key Length Greater Than or Equal to Message Length
                    while True:
                        key_positions = len(key)
                        if key_positions >= message_positions:
                            break
                        else: # Key Length Less than Message Length
                            key = key * 2
                            
                    # Reduces key length equal to message length
                    key = key[:message_positions]

                    # Defines Decoded Character List                    
                    decoded_message = []

                    for index in range(message_positions):
                        
                        # Given an Index, finds the matching characters in the message and passphrase
                        message_character = message[index] # Message Character For Index i
                        key_character = key[index] # Key Character for Index i
                        
                        current_key = alphabet.index(key_character) # This is the value that defines how far a letter rotates. Different for each character
                        current_alphabet = alphabet[current_key:] + alphabet[:current_key] # Defines alphabet list for current key
                        
                        current_alphabet_index = current_alphabet.index(message_character) # Finds position/index of encoded character in rotated/current alphabet
                        decoded_character = alphabet[current_alphabet_index] # Returns the decoded character by finding the character at position of above index of alphabet
                        
                        decoded_message.append(decoded_character) # Appends decoded character to list
                        
                    # Prints Decrypted Message
                    print("Here is the decrypted message: {}".format(str.join(decoded_message)))
                    print()
                    
                    # Asks User is they wish to Copy Message to Clipboard
                    copy_clipboard(str.join(decoded_message))
                    
                    # Ask User if they wish to do anything else
                    select_task()
                    
                elif second_choice == "3":
                    # Exit Secondary Menu
                    print("You have chosen to exit the menu.")
                    print()
                    break_second_menu = True
                    break
                
                else: # Second Choice not in range (1, 3)
                    print("You have entered an invalid response. Please enter 1, 2, or 3.")
                    print()
                    continue
                
                # Sends back to outer loop, 
                break
                    
        
        # -----------------------------------------------------------------------------------------------
        # BRUTE FORCE A CIPHERTEXT
        # -----------------------------------------------------------------------------------------------
        elif main_choice == "3":
            
            # Count List
            count_list = list([]) # Defines List that holds possible decoded messages and their corresponding counts

            # Ask User to Input a Cipher Text Message
            print("Please input message to be decoded: ", end = "")
            cipher_text = input() # Encoded Message to be Decoded
            cipher_message = list(cipher_text) # <--- Converts String to List (Each character becomes list element)
            print() # <--- Spacing

            # Number of Characters in Cipher Text Message
            positions = len(cipher_message)
            
            for key in range(1, 95): # Each Iteration Defines each Possible Alphabet Key (Key Increases)
                # Defines Rotated (CODED) Alphabet based on Key (Key = Number of Rotations)
                rotated_alphabet = alphabet[key:] + alphabet[:key] # If Key = 3, [A, B, C, D, E] = [D, E, A, B, C]

                # Defines List for Final Decoded Message. Decoded characters are appended to this list
                decoded_message = list() # Resets Decoded Message at the end of each iteration

                # Convert Every Character to Plain Text Character
                for index in range(positions):
                    
                    # Finds Character Associated with Given Index of Cipher Message List
                    character = cipher_message[index] # Index increases 0, 1, 2, 3, 4, etc. Finds character of each index
                    
                    # Finds Index of Character in Rotated Alphabet List
                    index_letter_rotated_alphabet = rotated_alphabet.index(character)
                    
                    # Finds Character Associated with Index in Original Alphabet List
                    decoded_character = alphabet[index_letter_rotated_alphabet]
                    
                    # Append Coded Character to List 
                    decoded_message.append(decoded_character)
                    
                joined_decoded_message = str.join(decoded_message) # Converts Decoded Message List to String
                
                for i in range(50): # Checks if splices within the decoded message are English Words 50 times
                    if positions < 6: # If length of the message is less than 6, distance between indicies are smaller
                        spaces = random.randint(2, positions)
                    else: # Defines the amount of space between the 2 indices 
                        spaces = random.randint(3, 6)
                    index_1 = random.randint(0, positions - spaces) # Index 1 (Minus Spaces so that Not out of Range)
                    index_2 = index_1 + spaces # Index 2
                
                    decoded_message_splice = joined_decoded_message[index_1:index_2] # Generates Message Splice
                    
                    if d.check(decoded_message_splice): # Checks if splice is a word in English Dictionary
                        count += 1 # If so, count of corresponsing decoded message gets 1 added to it
                
                # Add Decoded Message and English Count to Count List
                item_list = list() # Defines and Resets List each Iteration
                item_list.append(count) # Appends count to item list
                item_list.append(joined_decoded_message) # Appends message to list as well, as sorting is based on first element
                count_list.append(item_list) # Appends item list to bigger count list
                # count_list = [item_list1, item_list2]
                # item_list = [count, message]
                # count_list = [[count1, message1], [count2, message2], [count3, message3]]
                    # ^^^ count is places first, as message is sorted by highest count

                count = 0 # Resets Count at the end of each iteration
                
            # Sorted List
            sorted_message_list = sorted(count_list, reverse = True) # "Reverse = True" means Sort in Descending Order

            # Differing Choices
            count = 0
            while True: # Repeat until user receives correct decrypted message
                likely_message_splice = sorted_message_list[count]
                likely_message = likely_message_splice[1] # Second Element of Item List (Count is First)
                message1 = "\"{}\"\n".format(likely_message)
                message = message1 + "Does this look like the correct message? (YES or NO): "
                user_choice = yes_or_no(message)
                if user_choice: # user_choice == "yes"
                    if count + 1 == 1: # One Try to get correct message
                        print("It took {} try to get the correct message!".format(count + 1))
                    else: # More than one try to get correct message
                        print("It took {} tries to get the correct message!".format(count + 1))
                    print()
                    break
                else: # user_choice == "no"
                    count += 1 # Adds count for every time user says no. It took (count) times to get correct message.
            
            # Ask User if they would like to Select Another Task
            select_task()
            break
            
        # -----------------------------------------------------------------------------------------------
        # HISTORY OF CIPHERS
        # -----------------------------------------------------------------------------------------------
        elif main_choice == "4": # if user selects option 4
            print("You have chosen to: View the History of Ciphers")
            print()
            print("----------------------------------------------------")
            print("|{:^50}|".format("History of Ciphers Program"))
            print("----------------------------------------------------")
            print("| What would you like to do?                       |")
            print("|  1. Learn the History the Caesar Cipher          |")
            print("|  2. Learn the History the Vigenere Cipher        |")
            print("|  3. Exit                                         |")
            print("----------------------------------------------------")
            
            while True:
                print("Enter your choice: ", end = "")
                second_choice = input()
                print() # <--- Spacing
                
                if second_choice == "1":
                    # History of Caesar Cipher
                    print("----------------------------------------------------")
                    print("|{:^50}|".format("History of Caesar Cipher"))
                    print("----------------------------------------------------")
                    print()
                    
                    # Paragraph of Text on Caesar History & Explanation
                    print("The Caesar Cipher is one of the simplest and most common encryption technique found around the world. ")
                    print("It is a substitution cipher, which involves substituting letter in the message with another letter a ")
                    print("fixed number of positions ahead in the alphabet. For example, with a key of 3, the letter \"A\" would ")
                    print("shift forward 3 places in the alphabet to the letter \"D\". (A, B (+1), C (+2), D (+3)). Its name derives ")
                    print("from Roman Emperor Julius Caesar, who first used the cipher when sending sensitive military documents. ")
                    print("Given this is a single substitution cipher, where each letter corresponds to exactly one other letter, it ")
                    print("can easily be decrytped through frequency analysis. This renders it useless for any communication security. ")
                    print("There are only as many possible combinations/encryptions as there are characters in the alphabet. In the case ")
                    print("of this program, there are 95 possible combinations, including lowercase letters, uppercase letters, digits, ")
                    print("and special characters. The Brute Force algorithm analyzes each of these combinations, and selects the most ")
                    print("likely solution depending on the frequency of English words in the combination string. Due to the nature of ")
                    print("random selection, and there sometimes being English words in the incorrect ciphers, the program may not return ")
                    print("the correct combination message as the first choice.")
                    print()
                    
                    # Asks user if they would like to copy wikipedia article to clipboard
                    print("More information on the Caesar Cipher can be found on Wikipedia. ")
                    print()
                    copy_article_clipboard("https://en.wikipedia.org/wiki/Caesar_cipher") # Function Asks if User would like to copy article to clipboard
                
                elif second_choice == "2":
                    # History of Vigenere Cipher
                    print("----------------------------------------------------")
                    print("|{:^50}|".format("History of Vigenere Cipher"))
                    print("----------------------------------------------------")
                    print()
                    
                    # Paragraph of Text on Vigenere History & Explanation
                    print("The Vigenere Cipher, similar to the Caesar Cipher, is an encryption method that uses a more complex version ")
                    print("of the Caesar Cipher. It is a polyalphabetic substitution cipher, meaning letters in an encrypted message may ")
                    print("correspond to more than one other letter. For example, the letter \"A\" can correspond to both \"C\" and \"Y\" ")
                    print("depending on the key used. For Vigenere Ciphers, the key is not a single number, but rather a passphrase which ")
                    print("can contain letters. Each letter is rotated a number of spaces forward in the alphabet. That number is the index ")
                    print("of the passphrase that corresponds to the index of the letter in the message. For example, given the message \"Hello\" ")
                    print("and the passphrase \"Smile!\", the letter \"H\" will be rotated forward in the alphabet 19 spaces, which is the index ")
                    print("of \"S\" in the alphabet. As you can probably see, there are thousands of possible combinations for a Vigenere Cipher, ")
                    print("varying with the length of the passphrase and length of the alphabet used. Because of this, in the past it has even been")
                    print("called, \"le chiffrage indechiffrable,\" French for \"the indecipherable cipher\". The Vigenere Cipher was founded by ")
                    print("Giovan Battista Bellaso in 1553, but was given the name Vigenere due to the misattribution of the cipher creation to ")
                    print("Blaise de Vigenere. ")
                    print()
                    
                    # Asks user if they would like to copy wikipedia article to clipboard
                    print("More information on the Vigenere Cipher can be found on Wikipedia. ")
                    print()
                    copy_article_clipboard("https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher") # Function Asks if User would like to copy article to clipboard
                    
                elif second_choice == "3":
                    # Exit Secondary Menu
                    print("You have chosen to exit the menu.")
                    print()
                    break_second_menu = True
                    break
                
                else: # Second Choice not in range (1, 3)
                    print("You have entered an invalid response. Please enter 1, 2, or 3.")
                    print()
                    continue
                
                # Sends back to outer loop, 
                break
        
        # -----------------------------------------------------------------------------------------------
        # EXIT THE SYSTEM
        # -----------------------------------------------------------------------------------------------
        elif main_choice == "5":
            # Exit
            print("You have chosen to: Exit")
            break_main_menu = True
            break

        else: # Invalid Input for Main Menu Selection
            print("You have entered an invalid response. Please enter 1, 2, 3, 4, or 5.")
            print()
            continue
        
        # Breaks 2nd Menu from an Inner Loop
        if break_second_menu:
            break
    
    # Breaks Outer Main Program from an Inner Loop
    if break_main_menu:
        print("Thanks for your time. Goodbye!")
        break