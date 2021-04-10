import attr
import typing
from .object import Object
from .player import Player
from .room import Room

@attr.s
class Game:
    name = attr.ib()
    starting_room: Room = attr.ib(default=None)
    player: Player = attr.ib(default=None)
    def add_player(self, player):
        self.player = player
        player.game = self
    def set_starting_room(self, room):
        self.starting_room = room
        room.parent = self
