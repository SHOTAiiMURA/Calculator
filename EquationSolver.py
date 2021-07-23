import BasicArithmeticOperation0_1 as BAO

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


def nums_around_operator(string):
    string_arr = []
    for char in operators:
        if char in string:
            string_arr = string.split(char)
            break
    return float(string_arr[0]), float(string_arr[1])


def any_operator(string, operators):
    for char in operators:
        if char in string:
            return True
    return False


def first_appears_pos(string, object_arr):
    for i in range(len(string)):
        if string[i] in object_arr:
            return i
    return None


def first_operator(String, Operator):
    pos_ope = String.index(Operator)
    start = 0
    end = len(String)
    negative = False
    if String[pos_ope + 1] == "-":
        negative = True
        String = String[start:pos_ope + 1] + String[pos_ope + 2:end]

    while any_operator(String[start:pos_ope], operators):
        start += 1
        if start >= pos_ope:
            break
    while any_operator(String[pos_ope + 1: end], operators):
        end -= 1
        if end <= pos_ope:
            break

    #important for negative single number like -1, -4, -3.0
    if is_num2(String[start:end]):
        return String[start:end]

    num1, num2 = nums_around_operator(String[start:end])

    if negative:
        num2 *= -1

    result = BAO.operator_switch(num1, num2, String[pos_ope])
    String = String.replace(String[start:end], str(result))
    return String
    # return result_string


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
                    equ = equ[0:pos] + "+" + equ[pos+2:len(equ)]
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

    print(equ)

    parenthesis_cal_result = equation_solver_noParenthesis(equ)
    return parenthesis_cal_result


def is_num2(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


# string_pare = "1+(2*(1+((2*(1+2))+2)))+(1+2*2+(1*3*2+1)-1*(1+2))"
# "1-2*2*(-2)"
string_pare = "1+1*(-2)+1"

string = equation_solver(string_pare)
print("Final " + string)
