from tkinter import *
from decimal import Decimal, getcontext

def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

def is_valid_input(s):
    if 'e' in s:
        return False
    if s[0] == '+' or s[0] == '-':
        s = s[1:]
    a = s.replace(',', '.').split('.')
    if len(a) > 1:
        if ' ' in a[1]:
            return False
    b = a[0].split(' ')
    if len(b) > 1:
        if len(b[0]) > 3:
            return False
        for bs in b[1:]:
            if len(bs) != 3:
                return False
    return True

def parse_input(input_str):
    try:
        return Decimal(input_str.replace(' ', '').replace(',', '.'))
    except:
        raise ValueError

def format_decimal(number, decimal_places): #формируем результат с пробелами между разрядами, для этого разобьем число на целую и нецелую часть
    result = f'{number:.{decimal_places}f}'
    integer_part, non_integer_part = result.split('.')
    integer_part = '{:,}'.format(int(integer_part)).replace(',', ' ') 
    return f'{integer_part}.{non_integer_part}'

def click_sum():
    try:
        if is_valid_input(entry_num1.get()) and is_valid_input(entry_num2.get()):
            num1 = parse_input(entry_num1.get())
            num2 = parse_input(entry_num2.get())
            result = num1 + num2

            if abs(result) > 1000000000000:
                label_result['text'] = 'Слишком много'
            else:
                label_result['text'] = f'Результат: {format_decimal(result, 6)}'
        else:
            raise ValueError
    except ValueError:
        label_result['text'] = 'Неправильный ввод'

def click_differance():
    try:
        if is_valid_input(entry_num1.get()) and is_valid_input(entry_num2.get()):
            num1 = parse_input(entry_num1.get())
            num2 = parse_input(entry_num2.get())
            result = num1 - num2

            if abs(result) > 1000000000000:
                label_result['text'] = 'слишком много'
            else:
                label_result['text'] = f'Результат: {format_decimal(result, 6)}'
        else:
            raise ValueError
    except ValueError:
        label_result['text'] = 'Неправильный ввод'

def click_multiply():
    try:
        if is_valid_input(entry_num1.get()) and is_valid_input(entry_num2.get()):
            num1 = parse_input(entry_num1.get())
            num2 = parse_input(entry_num2.get())
            result = num1 * num2

            if abs(result) > 1000000000000:
                label_result['text'] = 'слишком много'
            else:
                label_result['text'] = f'Результат: {format_decimal(result, 6)}'
        else:
            raise ValueError
    except ValueError:
        label_result['text'] = 'Неправильный ввод'

def click_division():
    try:
        if is_valid_input(entry_num1.get()) and is_valid_input(entry_num2.get()):
            num1 = parse_input(entry_num1.get())
            num2 = parse_input(entry_num2.get())
            if num2 == 0:
                raise ZeroDivisionError
            else:
                result = num1 / num2

            if abs(result) > 1000000000000:
                label_result['text'] = 'слишком много'
            else:
                label_result['text'] = f'Результат: {format_decimal(result, 6)}'
        else:
            raise ValueError
    except ZeroDivisionError:
        label_result['text'] = 'нельзя на 0'
    except ValueError:
        label_result['text'] = 'Неправильный ввод'

getcontext().prec = 100 

root = Tk()
root.title('Calculator')
root.geometry('400x300')
root.bind_all("<Key>", _onKeyRelease, "+")
root.resizable(False,False)
root.config(bg='#ebe6d1')
label_name = Label(root, text='Булыга Никита 4 гр 4 к 2023')
label_name.place(relx=0.35, rely=0.1)
entry_num1 = Entry(root)
entry_num1.place(relx=0.1, rely=0.25)
entry_num2 = Entry(root)
entry_num2.place(relx=0.6, rely=0.25)
sum_but = Button(root, text='Сложение', command=click_sum)
sum_but.place(relx=0.15, rely=0.4)
diff_but = Button(root, text='Вычитание', command=click_differance)
diff_but.place(relx=0.35, rely=0.4)
division_but = Button(root, text='Деление', command=click_division)
division_but.place(relx=0.57, rely=0.4)
multiply_but = Button(root, text='Умножение', command=click_multiply)
multiply_but.place(relx=0.75, rely=0.4)
label_result = Label(root, text='Результат:')
label_result.place(relx=0.4, rely=0.6)
root.mainloop()