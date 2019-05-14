def minion_game(string):
    vowels = "AEIOU"
    vowels_split = list(vowels)
    string_split = list(string.upper())
    index = 0
    kevin_count = 0
    stuart_count = 0
    length = string.__len__()
    for char in string_split:
        if char in vowels_split:
            combo_num1 = length - index
            kevin_count += combo_num1

        else:
            combo_num2 = length - index
            stuart_count += combo_num2
        index += 1

    if stuart_count > kevin_count:
        print("Stuart %i" % stuart_count)
    elif kevin_count > stuart_count:
        print("Kevin %i" % kevin_count)
    else:
        print('Draw')


print(minion_game('BAANANAS'))
