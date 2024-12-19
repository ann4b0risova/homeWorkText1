with open('1.txt', encoding='utf-8') as f1:
    read_1 = f1.readlines()
    line_1text = len(read_1)
    #print(line_1text)

with open('2.txt', encoding='utf-8') as f2:
    read_2 = f2.readlines()
    line_2text = len(read_2)
    #print(line_2text)

with open('3.txt', encoding='utf-8') as f3:
    read_3 = f3.readlines()
    line_3text = len(read_3)
    #print(line_3text)

with open('total.txt', 'w', encoding='utf-8' ) as f_total:
    if line_1text < line_2text and line_1text < line_3text:
        f_total.write('1.txt' + '\n')
        f_total.write(str(line_1text) + '\n')
        f_total.writelines(read_1)
        f_total.write('\n')
    elif line_2text < line_1text and line_2text < line_3text:
        f_total.write('2.txt' + '\n')
        f_total.write(str(line_2text) + '\n')
        f_total.writelines(read_2)
        f_total.write('\n')
    elif line_3text < line_1text and line_3text < line_2text:
        f_total.write('3.txt' + '\n')
        f_total.write(str(line_3text) + '\n')
        f_total.writelines(read_3)
        f_total.write('\n')

    if line_2text < line_1text and line_3text > line_1text:
        f_total.write('1.txt' + '\n')
        f_total.write(str(line_1text) + '\n')
        f_total.writelines(read_1)
        f_total.write('\n')
    elif line_1text < line_2text and line_2text > line_3text:
        f_total.write('2.txt' + '\n')
        f_total.write(str(line_2text) + '\n')
        f_total.writelines(read_2)
        f_total.write('\n')
    elif line_1text < line_3text and line_2text > line_3text:
        f_total.write('3.txt' + '\n')
        f_total.write(str(line_3text) + '\n')
        f_total.writelines(read_3)
        f_total.write('\n')

    if line_1text > line_2text and line_1text > line_3text:
        f_total.write('1.txt' + '\n')
        f_total.write(str(line_1text) + '\n')
        f_total.writelines(read_1)
        f_total.write('\n')
    elif line_2text > line_1text and line_2text > line_3text:
        f_total.write('2.txt' + '\n')
        f_total.write(str(line_2text) + '\n')
        f_total.writelines(read_2)
        f_total.write('\n')
    elif line_3text > line_1text and line_3text > line_2text:
        f_total.write('3.txt' + '\n')
        f_total.write(str(line_3text) + '\n')
        f_total.writelines(read_3)
        f_total.write('\n')



