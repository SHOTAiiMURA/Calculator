import re
def sequence(equ_string, first_term, no_of_terms):
    sum = 0
    num = re.findall('\d+', equ_string)
    #print(type(num))
    #conv = int(num)
    #print(type(conv))
    #need equation_solver function

    return sum

sum = sequence("x+2", 3, 3)
print("sum :" + str(sum))