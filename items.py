from item_types import Belt, ItemContainer, ElectricPole, Fuel, Inserter as InserterType, Item, FluidTank

WoodenChest = ItemContainer(name="Wooden chest", stack_size=50, rocket_capacity=50, capacity=16)
IronChest = ItemContainer(name="Iron chest", stack_size=50, rocket_capacity=50, capacity=32)
SteelChest = ItemContainer(name="Iron chest", stack_size=50, rocket_capacity=50, capacity=48)

StorageTank = FluidTank(name="Storage tank", stack_size=50, rocket_capacity=50, volume=25_000)

TransportBelt = Belt(name="Transport belt", stack_size=100, rocket_capacity=100, speed=15)
FastTransportBelt = Belt(name="Fast transport belt", stack_size=100, rocket_capacity=100, speed=30)
ExpressTransportBelt = Belt(name="Express transport belt", stack_size=100, rocket_capacity=100, speed=45)
TurboTransportBelt = Belt(name="Turbo transport belt", stack_size=100, rocket_capacity=50, speed=60)

UndergroundBelt = Belt(name="Underground belt", stack_size=50, rocket_capacity=50, speed=15)
FastUndergroundBelt = Belt(name="Fast underground belt", stack_size=50, rocket_capacity=50, speed=30)
ExpressUndergroundBelt = Belt(name="Express underground belt", stack_size=50, rocket_capacity=50, speed=45)
TurboUndergroundBelt = Belt(name="Turbo underground belt", stack_size=50, rocket_capacity=25, speed=60)

Splitter = Belt(name="Splitter", stack_size=50, rocket_capacity=50, speed=15)
FastSplitter = Belt(name="Fast splitter", stack_size=50, rocket_capacity=50, speed=30)
ExpressSplitter = Belt(name="Express splitter", stack_size=50, rocket_capacity=50, speed=45)
TurboSplitter = Belt(name="Turbo splitter", stack_size=50, rocket_capacity=25, speed=60)

BurnerInserter = InserterType(
    name="Burner inserter", stack_size=50, rocket_capacity=50, rotation_speed=281, hand_size=1
)
Inserter = InserterType(name="Inserter", stack_size=50, rocket_capacity=50, rotation_speed=302, hand_size=1)
LongHandedInserter = InserterType(
    name="Long-handed inserter", stack_size=50, rocket_capacity=50, rotation_speed=432, hand_size=1
)
FastInserter = InserterType(name="Fast inserter", stack_size=50, rocket_capacity=50, rotation_speed=864, hand_size=1)
BulkInserter = InserterType(
    name="Bulk inserter",
    stack_size=50,
    rocket_capacity=50,
    rotation_speed=864,
    hand_size=2,  # not sure about hand_size here
)
StackInserter = InserterType(
    name="Stack inserter",
    stack_size=50,
    rocket_capacity=50,
    rotation_speed=864,
    hand_size=6,  # and here either
)

SmallElectricPole = ElectricPole(
    name="Small electric pole", stack_size=50, rocket_capacity=50, wire_reach=7.5, supply_area=(5, 5)
)
MediumElectricPole = ElectricPole(
    name="Medium electric pole", stack_size=50, rocket_capacity=50, wire_reach=9, supply_area=(7, 7)
)
BigElectricPole = ElectricPole(
    name="Big electric pole", stack_size=50, rocket_capacity=50, wire_reach=32, supply_area=(4, 4)
)
Substation = ElectricPole(name="Substation", stack_size=50, rocket_capacity=50, wire_reach=18, supply_area=(18, 18))

Pipe = Item(name="Pipe", stack_size=100, rocket_capacity=200)
PipeToGround = Item(name="Pipe to ground", stack_size=50, rocket_capacity=50)
Pump = Item(name="Pump", stack_size=50, rocket_capacity=50)

Rail = Item(name="Rail", stack_size=100, rocket_capacity=100)
RailRamp = Item(name="Rail ramp", stack_size=10, rocket_capacity=1)
RailSupport = Item(name="Rail support", stack_size=20, rocket_capacity=5)
TrainStop = Item(name="Train stop", stack_size=10, rocket_capacity=10)
RailSignal = Item(name="Rail signal", stack_size=50, rocket_capacity=50)
RailChainSignal = Item(name="Rail chain signal", stack_size=50, rocket_capacity=50)
Locomotive = Item(name="Locomotive", stack_size=5, rocket_capacity=5)
CargoWagon = ItemContainer(name="Cargo wagon", stack_size=5, rocket_capacity=5, capacity=40)
FluidWagon = FluidTank(name="Fluid wagon", stack_size=5, rocket_capacity=5, volume=50_000)
ArtilleryWagon = Item(name="Artillery wagon", stack_size=5, rocket_capacity=1)

Car = ItemContainer(name="Car", stack_size=1, rocket_capacity=1, capacity=80)
Tank = ItemContainer(name="Tank", stack_size=1, rocket_capacity=1, capacity=80)
Spidertron = ItemContainer(name="Spidertron", stack_size=1, rocket_capacity=1, capacity=80)

Wood = Fuel(name="Wood", stack_size=100, rocket_capacity=500, fuel_value=2_000_000)
Coal = Fuel(name="Coal", stack_size=50, rocket_capacity=500, fuel_value=4_000_000)
Stone = Item(name="Stone", stack_size=50, rocket_capacity=500)
IronOre = Item(name="Iron ore", stack_size=50, rocket_capacity=500)
CopperOre = Item(name="Copper ore", stack_size=50, rocket_capacity=500)
UraniumOre = Item(name="Uranium ore", stack_size=50, rocket_capacity=200)

IronPlate = Item(name="Iron plate", stack_size=100, rocket_capacity=1000)
CopperPlate = Item(name="Copper plate", stack_size=100, rocket_capacity=1000)
SteelPlate = Item(name="Steel plate", stack_size=100, rocket_capacity=400)
SolidFuel = Fuel(name="Solid fuel", stack_size=50, rocket_capacity=1000, fuel_value=12_000_000)
PlasticBar = Item(name="Plastic bar", stack_size=100, rocket_capacity=2000)
Sulfur = Item(name="Sulfur", stack_size=50, rocket_capacity=1000)
Battery = Item(name="Battery", stack_size=200, rocket_capacity=400)
Explosives = Item(name="Explosives", stack_size=50, rocket_capacity=500)
Carbon = Fuel(name="Carbon", stack_size=50, rocket_capacity=1000, fuel_value=2_000_000)

IronGearWheel = Item(name="Iron gear wheel", stack_size=100, rocket_capacity=1000)
IronStick = Item(name="Iron stick", stack_size=100, rocket_capacity=2000)
CopperCable = Item(name="Copper cable", stack_size=200, rocket_capacity=4000)
Barrel = Item(name="Barrel", stack_size=10, rocket_capacity=200)

ElectronicCircuit = Item(name="Electronic circuit", stack_size=200, rocket_capacity=2000)
AdvancedCircuit = Item(name="Advanced circuit", stack_size=200, rocket_capacity=1000)
ProcessingCircuit = Item(name="Processing circuit", stack_size=100, rocket_capacity=300)
