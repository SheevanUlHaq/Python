def frequency():
    sentence = input("Enter a sentence : ")
    dict = {}
    for i in sentence:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)


frequency()
