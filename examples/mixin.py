import plugged


class Main(plugged.mixin.PointExtend):

    name = 'someone'

    def do_main_things(self):
        print(self.yell())
        print(self.greeting())


@plugged.point
def yell():
    print('AWWWW YEEEE')


@plugged.point
class Other:

    @plugged.point
    def greeting(self):
        return f'Hello {self.name}'


if __name__ == '__main__':
    m = Main(locals().items())
    m.do_main_things()
