import plugged


@plugged.point
def greeting(name):
    return f'Greetings {name}'


@plugged.point
class Greeter:

    @plugged.point
    def yell(self):
        return self.name.upper()
