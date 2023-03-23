# import library to handle sounds
import winsound

# total morse dictionary
morse_dictionary = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}

# dictionary to assign beep duration on morse signals
dic_sound_durations = {
    ".":
        {
            "frequency": 1500,
            "duration": 100
        },
    "-": {
        "frequency": 1500,
        "duration": 300
    },
}


# function to convert string message to morse code
def convert_msg_to_morse(msg: str):
    msg = msg.upper()
    morse_code = ""
    for letter in msg:
        if letter.isspace():
            letter = '/'
        if letter in morse_dictionary.keys():
            morse_code_letter = morse_dictionary[letter]
            morse_code += morse_code_letter
    return morse_code


# main loop morse program - enter 'exit' to close the program
while True:
    print("Welcome to the Text to Morse Converter")
    message = input("Enter your actual message or 'exit' to terminate: ")
    if message.lower() == "exit":
        print("End of Morse Converter Program...")
        exit(0)
    msg_converted_to_morse = convert_msg_to_morse(message)
    print(f"The message converted to morse: {msg_converted_to_morse}")
    for sc in msg_converted_to_morse:
        winsound.Beep(dic_sound_durations[sc]["frequency"], dic_sound_durations[sc]["duration"])
