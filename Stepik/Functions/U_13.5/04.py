# is_password_good(password)
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.


# password = input('Ввелите пароль: ')
#
# if len(password) >= 8 and password.isupper() == True:
#     print('Yes')
# else:
#     print('NO')

password = '1234'

for i in password:
    if i.isdigit() == True:
        print('Y')
    else:
        print('N')



