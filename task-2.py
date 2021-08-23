def user(name: str, surname: str, birth: str, city: str, mail: str, phone: str) -> None:
    print(f'ФИО: {name} {surname}, Дата рождения: {birth}, Город проживания: {city}, Почта: {mail}, Телефон: {phone}')

user(name='Иван', surname='Иванов', birth='01.01.1970', city='Default city', mail='ivanov@mail.ru', phone='8 800 555-35-35')