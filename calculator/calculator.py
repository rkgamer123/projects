#!/usr/bin/env python3

import sys
import math
from tkinter import *


def combine_constants(values):

    vals_list = values.split(",")

    if len(vals_list) > 2:
        return ""

    for i in range(len(vals_list)):
        temp_exp = vals_list[i]

        j = 0
        sign = 1
        exp = ""

        while j != len(temp_exp):
            if temp_exp[j] != "-":
                break
            sign *= -1
            j += 1

        if sign == 1:
            exp = temp_exp[j:len(temp_exp)]
        elif sign == -1:
            exp = "-" + temp_exp[j:len(temp_exp)]

        temp_exp = exp

        try:
            val = float(exp)
        except ValueError:
            pass
        else:
            if exp[0] == "+":
                return ""

        temp_exp = temp_exp.split("pi")
        count = temp_exp.count("")
        for j in range(count):
            temp_exp.remove("")

        j = 0
        while j != len(temp_exp):
            temp = len(temp_exp[j].split("e"))
            temp_exp[j:j + 1] = temp_exp[j].split("e")
            j += temp

        count = temp_exp.count("")
        for j in range(count):
            temp_exp.remove("")

        j = 0
        while j != len(temp_exp):
            temp = len(temp_exp[j].split("π"))
            temp_exp[j:j + 1] = temp_exp[j].split("π")
            j += temp

        count = temp_exp.count("")
        for j in range(count):
            temp_exp.remove("")

        val = 1
        for j in range(len(temp_exp)):
            num = temp_exp[j]
            try:
                x = float(num)
            except ValueError:
                val = ""
                return val
            else:
                if ("+" in num) or ("-" in num and j != 0):
                    val = ""
                    return val
                else:
                    val *= float(num)

        pi_count = exp.count("pi") + exp.count("π")
        e_count = exp.count("e")

        if pi_count == 0 and e_count == 0 and temp_exp == []:
            val = ""
        else:
            val *= math.pi**pi_count
            val *= math.e**e_count

        vals_list[i] = str(val)

        if val == "":
            return val
    if len(vals_list) == 1:
        return vals_list[0]
    else:
        return ",".join(vals_list)


#Supported operators: +,-,*,x,/,//,^, **, %, !, sqrt(), root(),abs(),sin(),cos(),tan(),asin(),acos(),atan(),log(),ln(),floor(),ceil()

#Supported constants: pi, π, e
    
#module: argparse
    
# -i - interactive
# -e expression
# -v (default) - visual


def evaluate(text, start, show_work):

    if start:
        l3.configure(text="Steps Taken (0):")
        temp = 0
        for i in range(len(text)):
            if text[i] == '(':
                temp += 1
            elif text[i] == ')':
                temp -= 1
        if temp > 0:
            return ("Error: unmatched '('")
        elif temp < 0:
            return ("Error: unmatched ')'")

        mylist.delete(0, END)
        return evaluate(text, False, show_work)
    else:

        #solving code

        operators = [["!"], ["**", "^"], ["*", "x", "/", "//", "%"],
                     ["+", "-"]]
        all_functions = [
            "sqrt", "abs", "floor", "ceil", "sin", "cos", "tan", "asin",
            "acos", "atan", "log", "ln", "root"
        ]
        trig_functions = ["sin", "cos", "tan", "asin", "acos", "atan"]
        digits = "0123456789.pieπ"
        chars = "qwertyuiopasdfghjklzxcvbnm"
        exp = text.replace(" ", "")
        main_left = ""
        main_right = ""
        main_exp = ""
        trig_unit = ""
        steps_taken = 0

        if show_work:
            mylist.insert(END, "= " + main_left + exp + main_right)
            steps_taken += 1
            l3.configure(text="Steps Taken (" + str(steps_taken) + "):")

        solving_exp = True
        while solving_exp:
            main_exp = main_left + exp + main_right
            solving_section = True
            while solving_section:
                end = len(main_exp) - 1
                factorial = False
                i = 0
                while i != len(main_exp):
                    if main_exp[i] == ')':
                        end = i - 1
                        if main_exp[i + 1:i + 2] == "!":
                            factorial = True
                        break
                    i += 1
                if i == len(main_exp):
                    i -= 1

                start = i
                bracket = False
                while i != -1:
                    if main_exp[i] == '(':
                        bracket = True
                        break
                    i -= 1
                start = i + 1

                if i > 0:
                    i -= 1
                else:
                    i = 0

                main_left = main_exp[0:start]
                main_right = main_exp[end + 1:len(main_exp)]
                exp = main_exp[start:end + 1]

                function_left = False
                solve_function = False
                function = ""

                stamp = i
                if main_exp == "":
                    return ("Error: invalid input")

                if (main_exp[i] in chars or main_exp[i] in digits) and bracket:
                    function_left = True
                    while i != -1:
                        if (main_exp[i] not in chars
                                and main_exp[i] not in digits):
                            break
                        i -= 1
                    if i == -1:
                        i = 0

                    while i < stamp:
                        if main_exp[i:stamp +
                                    1] in all_functions or combine_constants(
                                        main_exp[i:stamp + 1]) != "":
                            break
                        i += 1

                    function = main_exp[i:stamp + 1]
                    i = i - 1

                    temp_function = combine_constants(function)
                    multiplier = False

                    if temp_function != "":
                        multiplier = True
                    elif function not in all_functions:
                        function = ""

                    if temp_function == "" and function not in all_functions:
                        return ("Error: invalid function")

                    if combine_constants(exp) != "":
                        solve_function = True

                if function_left and solve_function:
                    main_left = main_exp[0:i + 1]
                    main_right = main_right[1:len(main_right)]

                i2 = 0
                if exp != "":
                    while exp[i2] == "-" and i2 != len(exp) - 1:
                        i2 += 1
                minus_streak = i2
                sym_index = 0
                sym = ''
                for i in range(len(operators)):
                    temp_exp = exp[minus_streak:len(exp)]
                    temp_syms = [x for x in operators[i] if x in temp_exp
                                 ]  #Finds which operators are in the text

                    if temp_syms != []:
                        sym_dict = {x: temp_exp.index(x) for x in temp_syms}
                        keys = list(sym_dict.keys())  #syms in text
                        values = list(
                            sym_dict.values())  #index of syms in text
                        sym_index = sorted(values)[0] + minus_streak
                        sym = keys[values.index(sym_index - minus_streak)]
                        if sym == "/" and temp_exp[sym_index + 1:sym_index +
                                                   2] == "/":
                            sym = "//"
                        break

                i2 = sym_index - 1
                a = ""
                while i2 != -1:
                    if exp[i2] not in digits:
                        break
                    a = exp[i2] + a
                    i2 -= 1

                a = combine_constants(a)

                a_sign = 1
                while i2 != -1:
                    if exp[i2] != "-":
                        break
                    a_sign *= -1
                    i2 -= 1
                if i2 == -1:
                    i2 = 0

                if i2 == 0:
                    left_side = ''
                else:
                    left_side = exp[0:i2 + 1]

                i2 = sym_index + len(sym)

                b_sign = 1

                while i2 != len(exp):
                    if exp[i2] != "-":
                        break
                    b_sign *= -1
                    i2 += 1

                b = ""
                if combine_constants(exp) != "":
                    solved = True
                else:
                    solved = False

                while i2 != len(exp):
                    if (exp[i2]
                            not in digits) and not (exp[i2] == "," and solved):
                        break
                    b = b + exp[i2]
                    i2 += 1
                if i2 == len(exp):
                    i2 == len(exp) - 1

                b = combine_constants(b)

                right_side = exp[i2:len(exp)]

                two_ops = True

                try:
                    a = float(a)
                    if sym != "!":
                        b = float(b)
                except ValueError:
                    two_ops = False
                else:
                    if sym != "!":
                        a *= a_sign
                    if int(a) == a:
                        a = int(a)
                    if sym != "!":
                        b *= b_sign
                        if int(b) == b:
                            b = int(b)

                val = 0
                if two_ops:
                    if sym == "!":
                        if math.floor(a) != a:
                            return (
                                "Error: factorial not defined for decimal values"
                            )
                        elif a > 1000:
                            return ("Error: factorial overflow")
                        val = math.factorial(a) * a_sign
                    elif sym == "**" or sym == "^":
                        val = a**b
                        if isinstance(val, complex):
                            return ("Error: value is a complex number")
                    elif sym == "*" or sym == "x":
                        val = a * b
                    elif sym == "+":
                        val = a + b
                    elif sym == "-":
                        val = a - b
                    try:
                        if sym == "/":
                            val = a / b
                        elif sym == "//":
                            val = a // b
                        elif sym == "%":
                            val = a % b
                    except ZeroDivisionError:
                        return ("Error: division by zero")
                    exp = left_side + str(val) + right_side
                    main_exp = main_left + exp + main_right
                else:
                    if function == "log" or function == "root" and solve_function:
                        args = exp.split(",")
                        args[0] = combine_constants(args[0])
                        if len(args) == 2:
                            args[1] = combine_constants(args[1])
                        if function == "log" and len(args) > 2:
                            return (
                                "Error: log requires 1 to 2 arguments, got " +
                                str(len(args)))
                        elif function == "root" and len(args) != 2:
                            return ("Error: root requires 2 arguments, got " +
                                    str(len(args)))
                        if len(args) == 1:
                            args.append("")
                        if args[0] != "":
                            args[0] = float(args[0])
                        if args[1] != "":
                            args[1] = float(args[1])

                exp = combine_constants(str(exp))
                if exp != "" and "," not in str(exp):
                    exp = float(exp)

                if exp == "" and not two_ops:
                    return ("Error: invalid input")
                if exp != "":
                    if factorial and abs(exp) != exp:
                        return (
                            "Error: factorial is not defined for negative numbers"
                        )

                if combine_constants(str(exp)) != "" and "," not in str(exp):
                    val = float(exp)
                    if int(val) == val:
                        val = int(val)

                if function_left and solve_function:
                    if multiplier:
                        function = float(combine_constants(function))
                        exp = float(exp)
                        if int(function) == function:
                            function = int(function)
                        if int(exp) == exp:
                            exp = int(exp)
                        val = function * exp
                    else:
                        radians = 0
                        if function in ["sin", "cos", "tan"]:
                            if b2["text"] == "Radians":
                                radians = float(exp)
                            elif b2["text"] == "Degrees":
                                radians = math.radians(float(exp))

                        if function == "sqrt":
                            if abs(exp) == exp:
                                val = math.sqrt(exp)
                            else:
                                return (
                                    "Error: can't take square root of negative number"
                                )
                        elif function == "abs":
                            val = abs(exp)
                        elif function == "floor":
                            val = math.floor(exp)
                        elif function == "ceil":
                            val = math.ceil(exp)
                        elif function == "sin":
                            val = math.sin(radians)
                        elif function == "cos":
                            val = math.cos(radians)
                        elif function == "tan":
                            val = math.tan(radians)
                        elif function == "asin":
                            val = math.asin(exp)
                        elif function == "acos":
                            val = math.acos(exp)
                        elif function == "atan":
                            val = math.atan(exp)
                        elif function == "log":
                            try:
                                if args[1] == "":
                                    val = math.log10(args[0])
                                else:
                                    val = math.log(args[0], args[1])
                            except ValueError:
                                return ("Error: logarithim domain error")
                            if isinstance(val, complex):
                                return ("Error: value is a complex number")
                        elif function == "ln":
                            try:
                                val = math.log(exp)
                            except ValueError:
                                return ("Error: logarithim domain error")
                            if isinstance(val, complex):
                                return ("Error: value is a complex number")
                        elif function == "root":
                            try:
                                val = args[0]**(1 / args[1])
                            except ValueError:
                                return ("Error: root domain error")
                            if isinstance(val, complex):
                                return ("Error: value is a complex number")

                        if function in ["asin", "acos", "atan"
                                        ] and b2["text"] == "Degrees":
                            val = math.degrees(val)

                if val != "":
                    val = round(val, 11)
                    if int(val) == val:
                        val = int(val)

                if function != "log" or two_ops:
                    args = [val, ""]

                char = main_left[len(main_left) - 1:len(main_left)]

                if function_left and solve_function and char in digits and char != "":
                    main_left = main_left + "("
                    main_right = ")" + main_right

                exp = left_side + str(val) + right_side

                try:
                    x = float(args[0])
                    if args[1] != "":
                        x = float(args[1])
                except ValueError:
                    if (a == "" or b == "") and two_ops and sym != "!":
                        return ("Error: invalid input")
                else:
                    solving_section = False

                if not solving_section and not function_left:
                    main_left = main_left[0:len(main_left) - 1]
                    main_right = main_right[1:len(main_right)]

                main_exp = main_left + exp + main_right

                try:
                    x = float(main_exp)
                except ValueError:
                    pass
                else:
                    solving_exp = False

                if (show_work and not solving_section):
                    mylist.insert(END, "= " + main_exp)
                    steps_taken += 1
                    l3.configure(text="Steps Taken (" + str(steps_taken) +
                                 "):")
        return main_exp


def calculate():
    result = evaluate(t1.get(), True, True)
    t2.delete(0, END)
    t2.insert(END, str(result))


def change_unit():
    if b2["text"] == "Radians":
        b2.configure(text="Degrees")
    elif b2["text"] == "Degrees":
        b2.configure(text="Radians")


root = Tk()
root.title("Calculator")
root.geometry("600x400")

l1 = Label(root, text="Enter an expression:")
l1.place(x=60, y=20)

l2 = Label(root, text="Result:")
l2.place(x=135, y=260)

l3 = Label(root, text="Steps Taken: ")
l3.place(x=200, y=100)

l4 = Label(root, text="Angle Unit:")
l4.place(x=110, y=305)

t1 = Entry()
t1.place(x=200, y=20, width=310)

t2 = Entry()
t2.place(x=200, y=260, width=310)

scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scroll_bar.set, width=38, height=6)

scroll_bar.config(command=mylist.yview)

mylist.place(x=200, y=130)

b1 = Button(root, text='Calculate expression', command=calculate)
b1.place(x=200, y=55)

b2 = Button(root, text='Radians', command=change_unit)
b2.place(x=200, y=300)

root.mainloop()
