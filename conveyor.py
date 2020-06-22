#cумма
def summ(a):
    b = 0
    for _ in a.split(','):
        if _.isalnum():
            b += int(_)
    return b


#вывод конвейера
def final(st_f1, pluss, numss):
    return (st_f1+pluss)*numss


#подсчет тактов с учетом конфликтов
def conf_numss(st_f, pluss, numss):
    for i in st_f:
        if int(i) > st_f1 + pluss:
            if i % (st_f1 + pluss) != 0:
                numss += i // (st_f1 + pluss)
            else:
                numss += (i // (st_f1 + pluss)) - 1
    return numss

file = open('result.txt', 'a')
print('Данные записываются в файл result.txt')
nums = int(input('Введите кол-во команд >>> '))
pluss = int(input('Накладные расходы по организации конвейерной обработки >>> '))
fin = 0
st_f = []
for i in range(nums):
    st = input('Введите строку >>> ').replace(' ','')
    fin += summ(st)
    st_f.append(max(st.split(',')))
st_f1 = int(max(st_f))
numss = nums+6-1

file.write(f'Безконвейерный - {fin} (cр.знач - {fin / nums})\n')
# print('Безконвейерный', fin)
file.write(f'такты - {numss}\n')
# print('такты', numss)
file.write(f'Конвейер БЕЗ КОНФЛИКТОВ - {final(st_f1, pluss, numss)}\n')
# print('Конвейер', final(st_f1, pluss, numss))
print('Конфликты(3 шт)')

for i in range(3):
    inp = input('Введите через запятую номер программы, стадию(число) и нс конфликта (пример: 1,60,32) >>> ').replace(' ','').split(',')
    st_f[int(inp[0])-1] = int(inp[1])+int(inp[2])

numss = conf_numss(st_f, pluss, numss)
file.write(f'такты (с учетом конфликтов){numss}\n')
# print('такты', numss)
file.write(f'Конвейер (с учетом конфликтов) {final(st_f1, pluss, numss)}\n')
# print('Конвейер (с учетом конфликтов)', final(st_f1, pluss, numss))
print('Данные записаны!')
