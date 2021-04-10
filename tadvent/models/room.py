import attr
import typing
from .object import Object
from ..enums import Direction

@attr.s
class Room(Object):
    exits: typing.Dict[Direction, Object] = attr.ib(default=attr.Factory(dict))
    objects: typing.List[Object] = attr.ib(default=attr.Factory(list))
    player: Object = attr.ib(default=None)
    def add_exit(self, direction: Direction, obj: Object):
        self.exits[direction] = obj
        obj.parent = self
    def add_object(self, obj):
        self.objects.append(obj)
        obj.parent = self
    def add_player(self, player):
        self.player = player
        self.player.parent = self
