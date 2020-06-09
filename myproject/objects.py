# OOP


def run():
    print('run')
    return 'done'


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name  # attributes
            self.age = age
        if age < 18:
            print('Player not old enough')

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Tom', 10)

print(player1.shout())