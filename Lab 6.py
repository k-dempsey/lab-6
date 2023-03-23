#Code by Kiawa Dempsey

def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
#set up menu

def encode(word):
    string = ''
    for i in range(0, len(word)):
        if word[i] == '0':
            string += '3'
        elif word[i] == '1':
            string += '4'
        elif word[i] == '2':
            string += '5'
        elif word[i] == '3':
            string += '6'
        elif word[i] == '4':
            string += '7'
        elif word[i] == '5':
            string += '8'
        elif word[i] == '6':
            string += '9'
        elif word[i] == '7':
            string += '0'
        elif word[i] == '8':
            string += '1'
        elif word[i] == '9':
            string += '2'
    return string
# creates function to encode input by adding 3

if __name__ == '__main__':
    while True:
        menu()
        option = int(input('Please enter an option:' ))
        if option == 1:
            word = input('Please enter your password to encode:')
            word = encode(word)
            print('Your password has been encoded and stored!')
            pass
        elif option == 2:
            code = word
            o_word = decode(code) #o_word stands for original password
            print(f'The encoded password is', code, 'and the original password is', o_word, end=".")
            pass
        elif option == 3:
            break
# completes all the menu options