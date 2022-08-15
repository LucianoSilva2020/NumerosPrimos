numero = int(input('Digite um número:'))
total = 0
verde = '\033[1;36;42m'
for var in range (1, numero + 1):
    if numero % var == 0:
         print(f'{verde}', end='')
         total += 1
    else:
        print(f'{verde}', end='')   
        print(f'{var}', end='')
print(f'O número {numero} foi divisível {total} vezes.')
if total == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')             