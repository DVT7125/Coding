def da_name(first, middle, last):
    print(first, middle, last)
    print()

def apos(message):
    print(message)
    print()

def codm(language, what_is_a_comment):
    print("In", language, "a comment begins with a", what_is_a_comment)
    print()

def xof(base, exponent):
    result = base**exponent
    # print(result)
    print(base, "to the power of", exponent, "=", result)

def mult(num1, num2):
    result = num1*num2
    print(num1, "Times", num2, "=", result)

def Divd(num1, num2):
    if num2 == 0:
        print("Please do not put 0 in my secend number for me to divide!")
    else:
        result = num1/num2
        print(num1, "Divied By", num2, "=", result)

def Divm(Number1, Number2, Number3):
    if Number2 == 0:
        print("Please do not put a 0 for me to divide!")
    else:
        result = Number1/Number2*Number3
        print(Number1, "Divided by", Number2,
              "and times by", Number3, "=", result)
Divd(5, 0)
codm("Python", "#")
xof(-5, -2)
mult(5, -8)
Divm(5, 2, 67)
da_name("D", "V", "T")
apos("Now is the time for all good men to come to the aid of their country!")
