matches = {'zero': 'ноль',
           'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять'}

try:
    with open('lesson5_task4_in.txt', 'r') as f1:
        with open('lesson5_task4_out.txt', 'w') as f2:
            lines = f1.readlines()
            output = [matches[i.split()[0].lower()] + i[i.find(' '):] for i in lines]
            f2.writelines(output)
except Exception as e:
    print(e)
