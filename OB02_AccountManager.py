#Разработай систему управления учетными записями пользователей для небольшой
# компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.list_user = {}

    def add_user(self, id, name):
        self.list_user[id] = name
        print(f'Приветствуем, {name}! Ваш уникальный номер: {id}')

class Admin(User):
    def __init__(self, id, name, admin):
        super().__init__(id, name)
        self.admin = admin

    def info_status(self):
        self.admin = 'Администратор'
        print(f'Ваш статус: {self.admin}. Вы можете добавлять и удалять пользователей')

    def __add_user(self, id, name):
        self.list_user[id] = name
        print(f'Вы добавили нового пользователя {name}, id: {id}')

    def __del_user(self, id):
        if id in self.list_user:
            del self.list_user[id]
            print(f'Пользователь {id} удален')
        else:
            print(f'Пользователь {id} не найден')

    def get_add_user(self):
        return self.__add_user

    def get_del_user(self):
        return self.__del_user

u = User('222', 'Дмитрий')
u.add_user('222', 'Дмитрий')

a = Admin('01', 'Михаил', 'admin')
a.add_user('01', 'Михаил')
a.info_status()
add_a = a.get_add_user()
add_a('02', 'Марина')

add_a('03', 'Петр')
del_a = a.get_del_user()
del_a('03')