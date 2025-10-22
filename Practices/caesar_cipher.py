#AP 1st period, Caesar Cipher Encoder and Decoder
while True:
    #Make lists of all upper and lowercase leters
    upper = r"[A-Z]"
    lower = r"[a-z]"
    #Make a function for encoding
    def encoding(message, shift):
        #Check if each character is an upper or lowercase letter
        for i in message:
            if i.isupper:
                i = upper.index(i)+shift
                new_message += i
            elif i.islower:
                i = lower.index(i)+shift
                new_message += i

    #Make a function for decoding
    def decoding(message, shift):
        print("Hi")

    #Ask the user whether they want to encode or decode and call the corresponding function
    choice = input("To encode a message, type encode, to decode a message type decode: ").strip().lower()
    #Have the user choose how many characters they want to shift
    shift = int(input("How many digits would you like to shift, please enter a digit not a word: "))
    #Have the user type their message
    message = input("Please type the message: ")
    #Encode the message if the user chose to encode and print it
    if choice == "encode":
        encoded_message = encoding(message, shift)
        print(f"Your encoded message is {encoded_message}")
    #Decode the message if the user chose to decode and print it
    elif choice == "decode":
        decoded_message = decoding(message,shift)
        print(f"Your decoded message is {decoded_message}")
    #Have the user try again if they didn't choose either
    else:
        print("That's not a valid input, please try again")
        continue