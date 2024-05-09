def tamilnum(number):
    # இந்து அராபிய எண்களுக்கு இணையான தமிழ் எண்களை பட்டியலிடல்
    # Dictionary mapping Hindu-Arabic digits to Tamil digits
    hindu_arabic_to_tamil = {
        '0': '௦',
        '1': '௧',
        '2': '௨',
        '3': '௩',
        '4': '௪',
        '5': '௫',
        '6': '௬',
        '7': '௭',
        '8': '௮',
        '9': '௯',
        '-': '-'
    }

    num_str = str(number)

    if not num_str.lstrip('-').isdigit():
        return "தவறான உள்ளீடு. தொகுவெண்ணை மட்டுமே உள்ளிடுக."

    tamil_number = ''

    for char in num_str:
        tamil_number += hindu_arabic_to_tamil.get(char, char)

    #   உள்ளீட்டு எண்ணுக்கு இணையான தமிழ் எண்ணைத் திருப்பி அனுப்புதல்
    # Return the modern Tamil numeral equivalent of the input number
    return tamil_number


def tamilnum_traditional(number):
    #   தமிழ் எண்கள் மற்றும் இட மதிப்புகளை வைத்திருப்பதற்கான பட்டியல்கள்
    # Lists to hold Tamil numerals and place values
    tamil_numerals = ["", "௧", "௨", "௩", "௪", "௫", "௬", "௭", "௮", "௯"]
    place_values = ["", "௰", "௱", "௲"]

    input_str = str(number)
    if not input_str.lstrip('-').isdigit():
        return "தவறான உள்ளீடு. தொகுவெண்ணை மட்டுமே உள்ளிடுக."

    # Convert negative numbers to positive for processing
    if input_str.startswith('-'):
        is_negative = True
        number = input_str[1:]
    else:
        is_negative = False

    # Convert the input to an integer
    number = int(number)


    #   உள்ளீடு சரிபார்ப்பு
    # Input validation
    '''if not isinstance(number, int):
        return "தவறான உள்ளீடு. தொகுவெண்ணை மட்டுமே உள்ளிடுக."'''

    #   பாழை (0) கையாளுதல்
    # Handling zero input
    if number == 0:
        return "பாழ் "

    #   எதிர்மறை எண்களை கையாளுதல்
    # Handling negative numbers
    negative = False
    if number < 0:
        negative = True
        number = abs(number)

    #   ௯௯௯௯ (௯௲௯௱௯௰௯) ஐ விட அதிகமான எங்களை கையாளுதல்
    # Handling numbers greater than 9999
    if number > 9999:
        thousands = number // 1000
        thousands_text = tamilnum_traditional(thousands) + place_values[3]
        number %= 1000
    else:
        thousands_text = ''

    #   இந்து அரபி எண்ணை தமிழ் எண்ணாக மாற்றுதல்
    # Converting the Hindu Arabic number to Tamil text
    tamil_number = ''
    digits = []
    while number > 0:
        number, remainder = divmod(number, 10)
        digits.append(remainder)

    for i, digit in enumerate(digits):
        if digit == 0:
            continue
        if i == 0:
            tamil_number = tamil_numerals[digit] + tamil_number
        else:
            if digit == 1:
                tamil_number = place_values[i] + tamil_number
            else:
                tamil_number = tamil_numerals[digit] + place_values[i] + tamil_number

    tamil_number = thousands_text + tamil_number

    #   எண் எதிர்மறையாக இருந்தால் '-' ஐ முன்னோட்டமாகச் சேர்த்தல்
    # Adding '-' prefix if the number was negative
    if is_negative:
        tamil_number = '-' + tamil_number


    #   உள்ளீட்டு எண்ணுக்கு இணையான தமிழ் எண்ணைத் திருப்பி அனுப்புதல்
    # Return the traditional Tamil numeral equivalent of the input number
    return tamil_number