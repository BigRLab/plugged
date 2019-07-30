import plugged


def test_points():
    points = list(plugged.points('examples/plugins/*.py'))
    assert len(points) != 0
    for (name, point) in points:
        assert isinstance(point, plugged.entry.Point)
    return None
