def char_frequency(str1):
    dict = {}
    for n in str1:
        if n != ' ':
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
    return dict

def print_table(frequency):
    num_dashes = 10
    
    print('+', '-' * num_dashes, '+', '-' * num_dashes, '+')
    print('|', "{:<10}".format('CHARACTER'), '|', "{:<10}".format('FREQUENCY'), '|')
    print('+', '=' * num_dashes, '+', '=' * num_dashes, '+')

    for k, v in frequency.items():
        
        print('|', "{:<10}".format(k), '|', "{:<10}".format(v), '|')
        print('+', '-' * num_dashes, '+', '-' * num_dashes, '+')

text = input("Please enter a text: ")
frequency = char_frequency(text)
print_table(frequency)
