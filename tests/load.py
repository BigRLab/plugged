import plugged

def test_load():
    plugins = list(plugged.load('examples/plugins/*.py'))
    for item in plugins:
        assert isinstance(item, tuple)
        assert len(item) == 2
    return None
