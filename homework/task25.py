#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


str_ = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
letters = 'abcdefghijklmnopqrstuvwxyz'

def decoding(letter):
    global letters
    return letters[letters.index(letter) - 6] if letter in letters else letter

print(''.join(list(map(decoding, str_))))