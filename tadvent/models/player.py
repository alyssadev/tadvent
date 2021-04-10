import attr
import typing
from .object import Object

@attr.s
class Player(Object):
    def look(self, target=None):
        if target:
            return target.description
        yield self.parent.description
        for obj in self.parent.objects:
            if obj.position_desc:
                yield obj.position_desc
            else:
                yield "There is a {}{} here.".format((" ".join(obj.descriptors) + " ") if obj.descriptors else "", obj.name)

