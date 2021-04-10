import attr
import typing

@attr.s
class BaseObject:
    pass

@attr.s
class Object(BaseObject):
    name: str = attr.ib()
    description: str = attr.ib(default=None)
    descriptors: typing.List[str] = attr.ib(default=attr.Factory(list))

    # General object attributes
    visible: bool = attr.ib(default=True)
    parent: BaseObject = attr.ib(default=None)
    takeable: bool = attr.ib(default=True)
    readable: bool = attr.ib(default=True)
    position_desc: str = attr.ib(default=None)

    # Exit attributes
    locked: bool = attr.ib(default=None)
    destination: BaseObject = attr.ib(default=None)

    # Container attributes
    closed: bool = attr.ib(default=None)
    contains: typing.List[BaseObject] = attr.ib(default=attr.Factory(list))
