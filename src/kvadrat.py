from dotenv import dotenv_values


def get_square(dlina, nedlina):
    return dlina * nedlina


config = dotenv_values('.env')
string_dlina = config['dlina']
dlina = int(string_dlina)

string_nedlina = config['nedlina']
nedlina = int(string_nedlina)
square = get_square(dlina,nedlina)

print(f'Площадь квадрата длиной и шириной {dlina},{nedlina} равна {square}')
