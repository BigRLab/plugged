import plugged


class MyClass(plugged.mixin.PointExtend):

    name = 'Testing!'


def test_pointextend():
    t = MyClass(plugged.points('examples/plugins/*.py'))
    assert t.greeting('sj1k') == 'Greetings sj1k'
    assert t.yell() == 'TESTING!'
