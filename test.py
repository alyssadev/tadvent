from tadvent import Game, Room, Object, Player
from tadvent import Direction as d
import unittest

class TestZork(unittest.TestCase):
    def test_init_game(self):
        room = Room(name="West of House")
        room.description = "This is an open field west of a white house, with a boarded front door."

        door = Object(name="door", descriptors=["boarded", "front"], locked=True, destination=None)
        room.add_exit(d.East, door)

        leaflet = Object(name="leaflet", descriptors=["small"], readable=True)
        leaflet.contents = """WELCOME TO ZORK, or a poor facsimile at least"""
        mailbox = Object(name="mailbox", descriptors=["small"], closed=True, contains=[leaflet], takeable=False)
        room.add_object(mailbox)

        mat = Object(name="mat", descriptors=["rubber"])
        mat.description = "Welcome to Zork!"
        mat.position_desc = f"A rubber mat saying '{mat.description}' lies by the door."
        room.add_object(mat)

        player = Player(name=None)
        room.add_player(player)

        game = Game(name="ZORK")
        game.set_starting_room(room)
        game.add_player(player)
        look = "\n".join(game.player.look())
        self.assertEqual(look.strip(),
"""This is an open field west of a white house, with a boarded front door.
There is a small mailbox here.
A rubber mat saying 'Welcome to Zork!' lies by the door.""")

if __name__ == "__main__":
    unittest.main()
