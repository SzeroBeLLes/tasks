from dotenv import dotenv_values

def get_square(storona):
    drygaystorona=''
    for i in range(0, storona):
    	drygaystorona+='*'*storona
    	drygaystorona+='\n'
    return drygaystorona
config = dotenv_values('.env')
string_storona = config['storona']
storona = int(string_storona)
square = get_square(storona)
    
print(square)