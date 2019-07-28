import inspect
import functools

from . import entry, imp


class Extend:

    def __init__(self, path, importer):
        self.__path__ = path
        self.__importer__ = importer
        self.extend(importer(path))

    def extend(self, points):
        for (name, point) in points:
            self.__dict__[name] = point
        return None


class PointExtend(Extend):

    def __init__(self, path):
        super().__init__(path, entry.points(imp.load(path)))

    def extend(self, points):
        for (name, point) in points:
            if inspect.isclass(point.point):
                attrs = ((x, getattr(point.point, x)) for x in dir(point.point))
                for (name, point) in ((x, y) for x, y in attrs if entry.ispoint(y)):
                    self.__dict__[name] = functools.partial(point.point, self)
            else:
                self.__dict__[name] = point.point
