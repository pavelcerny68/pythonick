from collections import OrderedDict


# převod pouze Integer to Roman
# do souboru arab.in  zadáš číslo "5" a v roman.out přibyde "V"

def get_int_roman_dictord():
    """Create OrderedDict for roman numeral conversion."""
    d_int_roman = OrderedDict()

    d_int_roman[1000] = "M"
    d_int_roman[900] = "CM"
    d_int_roman[500] = "D"
    d_int_roman[400] = "CD"
    d_int_roman[100] = "C"
    d_int_roman[90] = "XC"
    d_int_roman[50] = "L"
    d_int_roman[40] = "XL"
    d_int_roman[10] = "X"
    d_int_roman[9] = "IX"
    d_int_roman[5] = "V"
    d_int_roman[4] = "IV"
    d_int_roman[1] = "I"

    return d_int_roman


def int_to_roman(int_roman_dictord, integer):
    """Convert Integer to Roman numeral."""
    roman_list = []

    # Handle conversion rules detailed in specification
    # while iterating over conversion ordered dictionary
    for key in int_roman_dictord:
        if key > integer:
            continue  # Restart loop until input int <= key
        q = integer // key  # // instead of divmod, remainder unused
        if not q:
            continue
        roman_list.append(int_roman_dictord[key] * q)
        integer -= (key * q)
        if not integer:
            break

    return ''.join(roman_list)


def main():
    """Write OUT file line by line, stop at first error in input as per spec."""
    int_roman_dictord = get_int_roman_dictord()  # Init conversion dictionary

    with open('ARAB.IN', 'r') as in_f:
        with open('ROMAN.OUT', 'w') as out_f:
            for line in in_f:
                try:
                    num = int(line)  # Try converting input line to integer
                except ValueError:
                    exit('{} is not a number.'.format(line))
                if 0 <= num <= 4000:
                    out_f.write(int_to_roman(
                        int_roman_dictord, int(line)) + '\n')
                    print("v souboru arab-in je zapsáno běžné číslo: ", num, "\n",
                          " do souboru roman-out je zapsáno romanske číslo: ", int_to_roman(int_roman_dictord, int(line)))
                    print("==================================================")
                else:
                    exit('{} is not between 0 and 4000.'.format(num))
                    Print("Nezadal jsi číslo mezi roky 0  až  4000")
                    

if __name__ == '__main__':
    main()
