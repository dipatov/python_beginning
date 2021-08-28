def print_information(name, surname, birth_year, birth_city, email, phone):
    print(f'Имя Фамилия: {name} {surname}', f'Год рождения: {birth_year}', f'Город рождения: {birth_city}',
          f'Email: {email}', f'Телефон: {phone}', sep='\n')


print_information(name='Иван', surname='Иванов', birth_year=2000, birth_city='Москва', email='asvd@gmail.com',
                  phone='+71234567890')
