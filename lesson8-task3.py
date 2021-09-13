class InputTypeError(Exception):
    def __init__(self, value, message='Неверный тип вводимого значения: '):
        self.message = message
        self.value = value
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} {self.value}'

inp = ''
integers = []
while inp != 'stop':
    try:
        inp = input()
        if not inp.isdigit():
            raise InputTypeError(inp)
        else:
            integers.append(int(inp))
    except InputTypeError as e:
        print(e)

print(integers)
