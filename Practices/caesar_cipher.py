#AP 1st period, Caesar Cipher Encoder and Decoder
#Loop it
while True:
    #Make the lists of all characters
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #Make the functions
    def encode(message,shift):
        #Make the new message variable
        new_message = "Your new message is: "
        #Check each character
        for char in message:
            #Check if char in upper and lower lists
            if char in upper:
                #Shift the character up
                char = upper.index(char) + shift
                char = upper[char]
                #Add it to the new message
                new_message = new_message + char
            elif char in lower:
                #Shift the character up
                char = lower.index(char) + shift
                char = lower[char]
                #Add it to the new message
                new_message = new_message + char
        return new_message
    def decode(message,shift):
        #Make the new message variable
        new_message = "Your new message is: "
        #Check each character
        for char in message:
            #Check if char in upper and lower lists
            if char in upper:
                #Shift the character down
                char = upper.index(char) - shift
                char = upper[char]
                #Add it to the new message
                new_message = new_message + char
            elif char in lower:
                #Shift the character down
                char = lower.index(char) - shift
                char = lower[char]
                #Add it to the new message
                new_message = new_message + char
        return new_message
    #Ask the user if they want to encode or decode
    choice = input("Would you like to encode or decode: ")
    #If they choose encode then get all the information and run the encode function
    if choice == "encode":
        message = input("What message would you like to encode: ")
        shift = int(input("How many digits would you like to shift: "))
        print(encode(message,shift))
    #If they choose decode then get all the information and run the decode function
    elif choice == "decode":
        message = input("What message would you like to decode: ")
        shift = int(input("How many digits would you like to shift: "))
        print(decode(message,shift))
    #If they enter something else then loop it back
    else:
        print("Please enter a valid option")
        continue