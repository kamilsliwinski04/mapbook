# name: str = input('Enter your name: ')
# print(f'WITAJ {name}')
data_of_users: list = [
    {'name': 'Julia', 'surname': 'Szklarzewska', 'posts': 5, 'location': 'Hajnówka'},
    {'name': 'Norbert', 'surname': 'Szeliga', 'posts': 15, 'location': 'Rzeszów'},
    {'name': 'Kacper', 'surname': 'Wójcik', 'posts': 20, 'location': 'Legnica'},
    {'name': 'Sebastian', 'surname': 'Dudek', 'posts': 100, 'location': 'Siedlce'},
]
print(f'Witaj {data_of_users[0]["name"]}')
def read(users:list)->None:
    """
    this is a function to show users from a list
    :param users: a list of users
    :return: None
    """
    for user in users[1:]:
        print(f'twój znajomy:  {user['name']}, opublikował: {user['posts']} postów')

read(data_of_users)
