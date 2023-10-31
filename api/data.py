from faker import Faker

'''
Здесь используется библиотека Faker для генерации тестовых данных (для логина пользователя) 
'''
fake = Faker()
test_name = fake.name().replace(" ", "").casefold()
data = [(f"{test_name}@example.com", "1234567890Test")]
login_data = data[0][0]
password_data = data[0][1]

'''
Здесь используются данные уже зарегистрированного пользователя
'''
old_user = ["test28102023-1@test.com", "1234567890Test"]
old_user_login = old_user[0]
old_user_password = old_user[1]