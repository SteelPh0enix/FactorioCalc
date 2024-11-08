from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    stack_size: int
    rocket_capacity: int

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)


@dataclass
class Fuel(Item):
    fuel_value: int
    "Energy possible to acquired from single unit of fuel, in jules"


@dataclass
class ItemContainer(Item):
    capacity: int
    """Capacity, in stacks"""


@dataclass
class FluidTank(Item):
    volume: float
    """Volume, in fluid units"""


@dataclass
class Belt(Item):
    speed: int
    """Belt speed, in moved items per second"""


@dataclass
class Inserter(Item):
    rotation_speed: int
    """Rotation speed, in degrees per second"""
    hand_size: int
    """How many items an inserter can pick up at once"""


@dataclass
class ElectricPole(Item):
    wire_reach: float
    """How long can a wire reach this pole"""
    supply_area: tuple[int, int]
    """Size of supply area in (width, height) format"""
