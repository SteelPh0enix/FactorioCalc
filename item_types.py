from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Entity:
    name: str

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

@dataclass(frozen=True)
class Item(Entity):
    stack_size: int
    rocket_capacity: int

@dataclass(frozen=True)
class Fuel(Item):
    fuel_value: int
    "Energy possible to acquired from single unit of fuel, in jules"


@dataclass(frozen=True)
class ItemContainer(Item):
    capacity: int
    """Capacity, in stacks"""


@dataclass(frozen=True)
class FluidTank(Item):
    volume: float
    """Volume, in fluid units"""


@dataclass(frozen=True)
class Belt(Item):
    speed: int
    """Belt speed, in moved items per second"""


@dataclass(frozen=True)
class Inserter(Item):
    rotation_speed: int
    """Rotation speed, in degrees per second"""
    hand_size: int
    """How many items an inserter can pick up at once"""


@dataclass(frozen=True)
class ElectricPole(Item):
    wire_reach: float
    """How long can a wire reach this pole"""
    supply_area: tuple[int, int]
    """Size of supply area in (width, height) format"""

@dataclass(frozen=True)
class Robot(Item):
    capacity: int
    """Cargo capacity of a robot, in items"""
    speed: float
    """Base speed of a robot"""
    max_power_consumption: float
    """Maximum power consumption, in watts"""

@dataclass(frozen=True)
class Miner(Item):
    mining_speed: float
    """Mining speed, in items/sec"""
    mining_area: tuple[int, int]
    """Mining area in (width, height) format"""
    resource_drain: float = 1
    """Resource drain multiplier, 100% == 1"""

@dataclass(frozen=True)
class Crafter(Item):
    crafting_speed: float = 1
    """Crafting speed multiplier"""
    base_productivity: float = 1
    """Base productivity of a crafter"""

@dataclass(frozen=True)
class Module(Item):
    energy_consumption: float = 0
    """Energy consumption multiplier"""
    speed: float = 0
    """Speed multiplier"""
    quality: float = 0
    """Quality multiplier"""
    productivity: float = 0
    """Productivity multiplier"""

@dataclass(frozen=True)
class Bacteria(Item):
    spoil_time: int
    """Spoil time, in seconds"""

@dataclass(frozen=True)
class Fluid(Entity):
    pass
