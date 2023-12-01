translation  = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_converted_input(text):

    converted_text = ''
    for i in range(len(text)):
        check_text = converted_text + text[i]

        
        check_text_replaced = check_text
        for t, n in translation.items():
            check_text_replaced = check_text_replaced.replace(t, n)

        if check_text != check_text_replaced:
            converted_text = check_text_replaced
        else:
            converted_text = converted_text + text[i]

    return converted_text

def get_converted_input_v2(text):

    converted_text_start = ''
    converted_text_end = ''
    for i in range(len(text)):
        check_text_start = converted_text_start + text[i]
        check_text_end = text[len(text) - 1 - i] + converted_text_end
        
        check_text_start_replaced = check_text_start
        check_text_end_replaced = check_text_end
        for t, n in translation.items():
            check_text_start_replaced = check_text_start_replaced.replace(t, n)
            check_text_end_replaced = check_text_end_replaced.replace(t, n)

        if check_text_start != check_text_start_replaced:
            converted_text_start = check_text_start_replaced
        else:
            converted_text_start = converted_text_start + text[i]

        if check_text_end != check_text_end_replaced:
            converted_text_end = check_text_end_replaced
        else:
            converted_text_end = text[len(text) - 1- i] + converted_text_end


        if i > len(text) //2 + 3:
            break

    return converted_text_start + converted_text_end


def get_calibration_values(input):

    text = get_converted_input_v2(input)
    
    length = len(text)
    first = False
    first_value = 0
    first_pos = 0
    last = False
    last_value = 0
    last_pos = length - 1

    for i in range(length):
        if not first:
            if text[i].isnumeric():
                first = True
                first_value = int(text[i])

        if not last:
            if text[length-1-i].isnumeric():
                last = True
                last_value = int(text[length-1-i])

        if first and last:
            break

        if first and first_pos == length-1-i:
            break
        if last and last_pos == i:
            break
    value = 0
    if first:
        value = first_value * 10
    else:
        value = last_value * 10

    if last:
        value = value + last_value
    else: 
        value = value + first_value


    print(input, text, value)
    return value

def solve(file):
    result = 0
    with open(file) as fp:
        while line := fp.readline():
            value = get_calibration_values(line.strip())
            result = result + value
    print(result)

if __name__ == "__main__":
    solve("input.txt")

