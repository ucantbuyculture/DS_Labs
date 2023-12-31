from tkinter import *
from decimal import Decimal, getcontext
 
def format_decimal(number, decimal_places):
    return f'{number:.{decimal_places}f}'

getcontext().prec = 100

def replace_dots(num1, num2):
    num1_res = Decimal(num1.get().replace(',', '.'))
    num2_res = Decimal(num2.get().replace(',', '.'))
    return num1_res, num2_res

def click_sum():
    try:
        if 'e' in numA_start.get() or 'e' in numB_start.get():
            raise ValueError
        numA, numB = replace_dots(numA_start, numB_start)
        result = numA + numB

        if abs(result) > 1000000000000:
            label_result['text'] = 'Переполнение'
        else:
            label_result['text'] = f'Результат: {format_decimal(result, 20)}'
    except ValueError:
        label_result['text'] = 'Ошибка ввода'

def click_diiferance():
    try:
        if 'e' in numA_start.get() or 'e' in numB_start.get():
            raise ValueError
        numA = Decimal(numA_start.get().replace(',', '.'))
        numB = Decimal(numB_start.get().replace(',', '.'))
        result = numA - numB

        if abs(result) > 1000000000000:
            label_result['text'] = 'Переполнение'
        else:
            label_result['text'] = f'Результат: {format_decimal(result, 20)}'
    except ValueError:
        label_result['text'] = 'Ошибка ввода'

root = Tk()
root.title('Calculator')
root.geometry('400x300')
label_name = Label(root, text='Булыга Никита, 4 группа, 4 курс, 2023')
label_name.grid(row=0, column=1, columnspan=4)
numA_start = Entry(root)
numA_start.grid(row=1, column=1)
numB_start = Entry(root)
numB_start.grid(row=1, column=2)
button_sum = Button(root, text='Сложение', command=click_sum)
button_sum.grid(row=2, column=1)
button_diff = Button(root, text='Вычитание', command=click_diiferance)
button_diff.grid(row=2, column=2)
label_result = Label(root, text='Результат:')
label_result.grid(row=3, column=1, columnspan=4)
root.mainloop()
