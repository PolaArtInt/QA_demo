def hello(username):
    return f'Hello {username}!'


print(hello('Pola'))


def new_func():
    print('new_func')


new_func()


class Employee:
    def __init__(self, username):
        self.username = username


emp_1 = Employee('Pola')
