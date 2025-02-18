from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Reverse Morse Code Dictionary for decoding
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # Serve index.html from the templates folder

# Encode endpoint
@app.route('/encode', methods=['POST'])
def encode():
    data = request.json
    message = data.get('message', '').upper()
    encoded_message = ''

    for char in message:
        if char != ' ':
            encoded_message += MORSE_CODE_DICT.get(char, '') + ' '
        else:
            encoded_message += ' '  # Separate words by a double space

    return jsonify({'encoded_message': encoded_message.strip()})

# Decode endpoint
@app.route('/decode', methods=['POST'])
def decode():
    data = request.json
    morse_code = data.get('morse_code', '').strip() + ' '
    decoded_message = ''
    citext = ''
    i = 0

    for letter in morse_code:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decoded_message += ' '
            else:
                decoded_message += REVERSE_MORSE_CODE_DICT.get(citext, '')
                citext = ''

    return jsonify({'decoded_message': decoded_message})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Allow access via 127.0.0.1:5000
