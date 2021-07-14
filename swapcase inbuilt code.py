# In this file i define what swapecase() inbuilt function code look like

final = ''

def my_code(line):
    global final
    for i in line:
        ss = i
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            if i.isupper():
                ss = i.lower()
                final = final + ss
            else:
                ss = i.upper()
                final = final + ss

        else:
            final = final + ss
    return final


def swap_case(line):
    return line.swapcase()


if __name__ == '__main__':
    s = input("Enter String:")
    result = swap_case(s)
    print(result)
    result2 = my_code(s)
    print(result2)