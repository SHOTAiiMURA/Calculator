from Calculator import BasicArithmeticOperation0_1 as BAO
# import BasicArithmeticOperation0_1 as BAO
operators = ["+", "-", "*", "/"]


def detect_parenthesis(strF, index=0, pair_ParenCount=0):
    check = False
    while index < len(strF):
        if strF[index] == "(":
            strF[index]
            pair_ParenCount += 1
            check = True
            detect_parenthesis(strF, index + 1, pair_ParenCount)
        elif strF[index] == ")":
            if pair_ParenCount <= 0:
                return -1
            else:
                pair_ParenCount -= 1
        index += 1

    if pair_ParenCount != 0:
        return -1
    elif check == False:
        return 0
    else:
        return 1


def find_parenthesisString(strF):
    start = 0
    end = 0
    check = 0
    start = strF.index("(")
    for i in range(start, len(strF)):
        if strF[i] == "(":
            check += 1
        if strF[i] == ")":
            check -= 1
        if check == 0:
            end = i
            a = strF[start + 1:end]
            return a


def nums_around_operator(string, operator):
    string_arr = string.split(operator)
    return float(string_arr[0]), float(string_arr[1])


def any_operator(string, operators):
    for char in operators:
        if char in string:
            return True
    return False


def first_appears_pos(string, object_arr):
    for i in range(len(string)):
        if string[i] in object_arr:
            if i == 0:
                return first_appears_pos(string[1:], object_arr) + 1
            return i
    return None

def is_num2(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


def first_operator(String, Operator):
    negative_firstLetter = False
    pos_ope = String.index(Operator)
    start = 0

    if Operator in ["+", "-"] and String[0] == "-":
        pos_ope = String[1:].index(Operator)
        String = String[1:]
        negative_firstLetter = True


    end = len(String)
    negative = False

    if String[pos_ope + 1] == "-":
        negative = True
        String = String[start:pos_ope + 1] + String[pos_ope + 2:end]

    while any_operator(String[start:pos_ope], operators):
        start += 1

    while any_operator(String[pos_ope + 1: end], operators):
        end -= 1

    num1, num2 = nums_around_operator(String[start:end], Operator)

    if negative_firstLetter:
        num1 *= -1
    if negative:
        num2 *= -1

    result = BAO.operator_switch(num1, num2, Operator)
    String = String.replace(String[start:end], str(result))
    print(String)
    return String


def equation_solver_noParenthesis(equ):
    while any_operator(equ, operators):
        operator = ""
        if is_num2(equ):
            break
        if any(x in equ for x in ["*", "/"]):
            pos = first_appears_pos(equ, ["*", "/"])
        else:
            pos = first_appears_pos(equ, ["+", "-"])
            while equ[pos + 1] in ["+", "-"]:
                if equ[pos] == equ[pos + 1]:
                    equ = equ[0:pos] + "+" + equ[pos + 2:len(equ)]
                else:
                    equ = equ[0:pos] + "-" + equ[pos + 2:len(equ)]
        operator = equ[pos]
        equ = first_operator(equ, operator)
    return equ


def equation_solver(equ):
    result = ""
    parenthesis_cal = ""
    parenthesis_cal_result = ""
    print(equ)

    while detect_parenthesis(equ) == 1:
        parenthesis_cal = find_parenthesisString(equ)
        if any_operator(parenthesis_cal, operators):
            parenthesis_cal_result = equation_solver(parenthesis_cal)
        else:
            parenthesis_cal_result = parenthesis_cal
        equ = equ.replace("(" + parenthesis_cal + ")", parenthesis_cal_result)

        print(equ)
    if detect_parenthesis(equ) == -1:
        print("Error")
        return None

    # print(equ)

    parenthesis_cal_result = equation_solver_noParenthesis(equ)
    return parenthesis_cal_result

def equation_solver_x(equ, variable, var_value):
    equ_x = equ.replace(variable, str(var_value))
    result = equation_solver(equ_x)
    return result


# string_pare = "1+(2*(1+((2*(1+2))+2)))+(1+2*2+(1*3*2+1)-1*(1+2))"
string_pare = "1+(2*(1+(-2)*(1+2+6*(1+2-(2+(-2)))+2))+1*(-1+3))+(1+2*2+(1*3*2+1)-(1+2))"
"1+(-90+1*(2))+(1+2*2+(1*3*2+1)-(1+2))"
# "1-2*2*(-2)"
# string_pare = "1+(-4)*(-2*2)+1+5*(-1)+(-7*(-2))"

string = equation_solver(string_pare)
print(type(string))
print("Answer " + str(1+(2*(1+(-2)*(1+2+6*(1+2-(2+(-2)))+2))+1*(-1+3))+(1+2*2+(1*3*2+1)-(1+2))))

# string_x = "x*x+x+2"
# print(string_x)
# result = equation_solver_var(string_x, "x", 3)
# print(result)