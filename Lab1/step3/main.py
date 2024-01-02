from tkinter import *
from tkinter.ttk import *
from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_DOWN 

def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

def check_input(s):
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

def format_decimal(number, decimal_places=10):
    rounded_number = number.quantize(Decimal('1e-%d' % decimal_places))
    str_number = f'{rounded_number:f}' 
    parts = str_number.split('.')      
    int_part = '{:,}'.format(int(parts[0])).replace(',', ' ')  
    return int_part + '.' + parts[1] if len(parts) > 1 else int_part


def round_result(value, method):
    if method == "mathematical":
        return value.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    elif method == "bankers":
        return value.quantize(Decimal('1'), rounding=ROUND_HALF_EVEN)
    elif method == "truncation":
        return value.quantize(Decimal('1'), rounding=ROUND_DOWN)
    return value  

def calculate():
    try:
        if check_input(entry_num1.get()):
            num1 = parse_input(entry_num1.get())
        else:
            raise ValueError
        if check_input(entry_num2.get()):
            num2 = parse_input(entry_num2.get())
        else:
            raise ValueError
        if check_input(entry_num3.get()):
            num3 = parse_input(entry_num3.get())
        else:
            raise ValueError
        if check_input(entry_num4.get()):
            num4 = parse_input(entry_num4.get())
        else:
            raise ValueError

        # операции с num2 и num3
        if operation2_var.get() == '+':
            inner_result = num2 + num3
        elif operation2_var.get() == '-':
            inner_result = num2 - num3
        elif operation2_var.get() == '*':
            inner_result = num2 * num3
        elif operation2_var.get() == '/':
            if num3 == 0:
                raise ZeroDivisionError
            inner_result = num2 / num3

        if abs(inner_result) > Decimal('1000000000000.0000000000'):
            raise OverflowError
        inner_result = inner_result.quantize(Decimal('1.0000000000'))

        if operation1_var.get() == '+':
            result = num1 + inner_result
        elif operation1_var.get() == '-':
            result = num1 - inner_result
        elif operation1_var.get() == '*':
            result = num1 * inner_result
        elif operation1_var.get() == '/':
            if inner_result == 0:
                raise ZeroDivisionError
            result = num1 / inner_result

        if abs(result) > Decimal('1000000000000.0000000000'):
            raise OverflowError
        result = result.quantize(Decimal('1.0000000000'))

        if operation3_var.get() == '+':
            result += num4
        elif operation3_var.get() == '-':
            result -= num4
        elif operation3_var.get() == '*':
            result *= num4
        elif operation3_var.get() == '/':
            if num4 == 0:
                raise ZeroDivisionError
            result /= num4

        if abs(result) > Decimal('1000000000000.0000000000'):
            raise OverflowError
        result = result.quantize(Decimal('1.0000000000'))

        result_str = f"{result:f}".rstrip('0').rstrip('.') if '.' in f"{result}" else f"{result}"
        label_result.config(text=f'Результат: {result_str}')
        rounding_method = var_rounding.get()
        result = round_result(result, rounding_method)
        label_rounded.config(text=f'Округлено: {int(result)}')

    except ValueError:
        label_result.config(text='Ошибка ввода')
    except ZeroDivisionError:
        label_result.config(text='Деление на ноль')
    except OverflowError:
        label_result.config(text='Переполнение')

getcontext().prec = 100

root = Tk()
root.title('4 operands calculator')
root.config(bg='#ebe6d1')
root.geometry('800x300')
root.bind_all("<Key>", _onKeyRelease)
label_name = Label(root, text='Булыга Никита 4 гр 4 к 2023')

entry_num1 = Entry(root)
entry_num1.grid(row=1, column=0)
entry_num1.insert(0, '0')

operation1_var = StringVar(value='+')
operation1_menu = Combobox(root, textvariable=operation1_var, values=['+', '-', '*', '/'], state='readonly', width=3)
operation1_menu.grid(row=1, column=1)

label_open_bracket = Label(root, text='(')
label_open_bracket.grid(row=1, column=2)

entry_num2 = Entry(root)
entry_num2.grid(row=1, column=3)
entry_num2.insert(0, '0')

operation2_var = StringVar(value='+')
operation2_menu = Combobox(root, textvariable=operation2_var, values=['+', '-', '*', '/'], state='readonly', width=3)
operation2_menu.grid(row=1, column=4)

entry_num3 = Entry(root)
entry_num3.grid(row=1, column=5)
entry_num3.insert(0, '0')

label_close_bracket = Label(root, text=')')
label_close_bracket.grid(row=1, column=6)

operation3_var = StringVar(value='+')
operation3_menu = Combobox(root, textvariable=operation3_var, values=['+', '-', '*', '/'], state='readonly', width=3)
operation3_menu.grid(row=1, column=7)

entry_num4 = Entry(root)
entry_num4.grid(row=1, column=8)
entry_num4.insert(0, '0')

button_calc = Button(root, text='=', command=calculate)
button_calc.grid(row=1, column=9)

label_result = Label(root, text='Результат:')
label_result.grid(row=2, column=0, columnspan=10)

label_rounded = Label(root, text='Округлено:')
label_rounded.grid(row=3, column=0, columnspan=10)

var_rounding = StringVar(value="mathematical")  # Значение по умолчанию для округления

rounding_frame = Frame(root)
rounding_frame.grid(row=4, column=0, columnspan=10)

rounding_methods = [("Математическое", "mathematical"), ("Бухгалтерское", "bankers"), ("Усечение", "truncation")]
for text, method in rounding_methods:
    Radiobutton(rounding_frame, text=text, variable=var_rounding, value=method).pack(side=LEFT)

root.mainloop()