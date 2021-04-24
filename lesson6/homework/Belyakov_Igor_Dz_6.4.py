with open('users.csv', 'r', encoding='utf-8') as users_f, open('hobby.csv', 'r', encoding='utf-8') as hobby_f:
    while True:
        user = users_f.readline()
        hobby = hobby_f.readline()
        if user:
            user_name = ' '.join(user.strip().split(','))
            hobbies = hobby.strip().split(',') if hobby else None
            print(user_name, hobbies)  # сложная обработка
        elif hobby:
            exit(1)
        else:
            break
