from dotenv import dotenv_values
def get_square(min1):
    
    for i in range (0, 500):
        min1+=(i)
    return min1
config = dotenv_values('.env')
string_min1 = config['min1']
min1 = int(string_min1)
square = get_square(min1)

print(f'число{min1} равна {square}')
