from item_types import (
    Asteroid,
    Bacteria,
    Belt,
    Crafter,
    ElectricPole,
    Fluid,
    FluidTank,
    Fuel,
    Inserter as InserterType,
    Item,
    ItemContainer,
    Miner,
    Module,
    Robot,
)

# Logistics

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
BulkInserter = InserterType(name="Bulk inserter", stack_size=50, rocket_capacity=50, rotation_speed=864, hand_size=2)
StackInserter = InserterType(name="Stack inserter", stack_size=50, rocket_capacity=50, rotation_speed=864, hand_size=6)

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

LogisticRobot = Robot(
    name="Logistic robot", stack_size=50, rocket_capacity=50, capacity=1, speed=10.8, max_power_consumption=29_250
)
ConstructionRobot = Robot(
    name="Construction robot", stack_size=50, rocket_capacity=50, capacity=1, speed=13, max_power_consumption=34_500
)
ActiveProviderChest = ItemContainer(name="Active provider chest", stack_size=50, rocket_capacity=50, capacity=48)
PassiveProviderChest = ItemContainer(name="Passive provider chest", stack_size=50, rocket_capacity=50, capacity=48)
StorageChest = ItemContainer(name="Storage chest", stack_size=50, rocket_capacity=50, capacity=48)
BufferChest = ItemContainer(name="Buffer chest", stack_size=50, rocket_capacity=50, capacity=48)
RequesterChest = ItemContainer(name="Requester chest", stack_size=50, rocket_capacity=50, capacity=48)
Roboport = Item(name="Roboport", stack_size=10, rocket_capacity=10)

Lamp = Item(name="Lamp", stack_size=50, rocket_capacity=50)
ArithmeticCombinator = Item(name="Arithmetic combinator", stack_size=50, rocket_capacity=50)
DeciderCombinator = Item(name="Decider combinator", stack_size=50, rocket_capacity=50)
SelectorCombinator = Item(name="Selector combinator", stack_size=50, rocket_capacity=50)
ConstantCombinator = Item(name="Constant combinator", stack_size=50, rocket_capacity=50)
PowerSwitch = Item(name="Power switch", stack_size=10, rocket_capacity=10)
ProgrammableSpeaker = Item(name="Programmable speaker", stack_size=10, rocket_capacity=10)
DisplayPanel = Item(name="DisplayPanel", stack_size=10, rocket_capacity=10)

StoneBrick = Item(name="Stone brick", stack_size=100, rocket_capacity=500)
Concrete = Item(name="Concrete", stack_size=100, rocket_capacity=100)
HazardConcrete = Item(name="Hazard concrete", stack_size=100, rocket_capacity=100)
RefinedConcrete = Item(name="Refined concrete", stack_size=100, rocket_capacity=100)
RefinedHazardConcrete = Item(name="Refined hazard concrete", stack_size=100, rocket_capacity=100)
Landfill = Item(name="Landfill", stack_size=100, rocket_capacity=20)
ArtificialYumakoSoil = Item(name="Artificial yumako soil", stack_size=100, rocket_capacity=67)
OvergrowthYumakoSoil = Item(name="Overgrowth yumako soil", stack_size=100, rocket_capacity=14)
ArtificialJellynutSoil = Item(name="Artificial jellynut soil", stack_size=100, rocket_capacity=67)
OvergrowthJellynutSoil = Item(name="Overgrowth jellynut soil", stack_size=100, rocket_capacity=14)
IcePlatform = Item(name="Ice platform", stack_size=100, rocket_capacity=100)
Foundation = Item(name="Foundation", stack_size=50, rocket_capacity=50)
CliffExplosives = Item(name="Cliff explosives", stack_size=20, rocket_capacity=20)

# Production

RepairPack = Item(name="Repair pack", stack_size=100, rocket_capacity=100)

Boiler = Item(name="Boiler", stack_size=50, rocket_capacity=50)
SteamEngine = Item(name="Steam engine", stack_size=10, rocket_capacity=10)
SolarPanel = Item(name="Solar panel", stack_size=50, rocket_capacity=50)
Accumulator = Item(name="Accumulator", stack_size=50, rocket_capacity=50)
NuclearReactor = Item(name="Nuclear reactor", stack_size=10, rocket_capacity=1)
HeatPipe = Item(name="Heat pipe", stack_size=50, rocket_capacity=50)
HeatExchanger = Item(name="Heat exchanger", stack_size=50, rocket_capacity=25)
SteamTurbine = Item(name="Steam turbine", stack_size=10, rocket_capacity=10)
FusionReactor = Item(name="Fusion reactor", stack_size=1, rocket_capacity=1)
FusionGenerator = Item(name="Fusion generator", stack_size=5, rocket_capacity=5)

BurnerMiningDrill = Miner(
    name="Burner mining drill",
    stack_size=50,
    rocket_capacity=50,
    mining_speed=0.25,
    mining_area=(2, 2),
)
ElectricMiningDrill = Miner(
    name="Electric mining drill",
    stack_size=50,
    rocket_capacity=50,
    mining_speed=0.5,
    mining_area=(5, 5),
)
BigMiningDrill = Miner(
    name="Big mining drill",
    stack_size=20,
    rocket_capacity=20,
    mining_speed=2.5,
    mining_area=(13, 13),
    resource_drain=0.5,
)
OffshorePump = Item(name="Offshore pump", stack_size=20, rocket_capacity=20)
Pumpjack = Miner(
    name="Pumpjack", stack_size=20, rocket_capacity=20, mining_speed=1, mining_area=(1, 1), resource_drain=1
)

StoneFurnace = Crafter(name="Stone furnace", stack_size=50, rocket_capacity=50)
SteelFurnace = Crafter(name="Steel furnace", stack_size=50, rocket_capacity=50, crafting_speed=2)
ElectricFurnace = Crafter(name="Electric furnace", stack_size=50, rocket_capacity=50, crafting_speed=2)
Foundry = Crafter(name="Foundry", stack_size=20, rocket_capacity=5, crafting_speed=4, base_productivity=0.5)
Recycler = Crafter(name="Recycler", stack_size=20, rocket_capacity=10, crafting_speed=0.5)

AgriculturalTower = Item(name="Agricultural tower", stack_size=20, rocket_capacity=20)
Biochamber = Crafter(name="Biochamber", stack_size=20, rocket_capacity=20, crafting_speed=2, base_productivity=0.5)
CaptiveBiterSpawner = Crafter(name="Captive biter spawner", stack_size=1, rocket_capacity=1)

AssemblingMachine1 = Crafter(name="Assembling machine 1", stack_size=50, rocket_capacity=50, crafting_speed=0.5)
AssemblingMachine2 = Crafter(name="Assembling machine 2", stack_size=50, rocket_capacity=50, crafting_speed=0.75)
AssemblingMachine3 = Crafter(name="Assembling machine 3", stack_size=50, rocket_capacity=25, crafting_speed=1.25)
OilRefinery = Crafter(name="Oil refinery", stack_size=10, rocket_capacity=10, crafting_speed=1)
ChemicalPlant = Crafter(name="Chemical plant", stack_size=10, rocket_capacity=10, crafting_speed=1)
Centrifuge = Crafter(name="Centrifuge", stack_size=50, rocket_capacity=1, crafting_speed=1)
ElectromagneticPlant = Crafter(name="Electromagnetic plant", stack_size=20, rocket_capacity=5, crafting_speed=2)
CryogenicPlant = Crafter(name="Cryogenic plant", stack_size=20, rocket_capacity=5, crafting_speed=2)
Lab = Item(name="Lab", stack_size=10, rocket_capacity=10)
Biolab = Item(name="Biolab", stack_size=5, rocket_capacity=1)

LightningRod = Item(name="Lightning rod", stack_size=50, rocket_capacity=50)
LightningCollector = Item(name="Lightning collector", stack_size=20, rocket_capacity=20)
HeatingTower = Item(name="Heating tower", stack_size=20, rocket_capacity=10)

Beacon = Item(name="Beacon", stack_size=20, rocket_capacity=20)

SpeedModule1 = Module(
    name="Speed module 1",
    stack_size=50,
    rocket_capacity=50,
    energy_consumption=0.5,
    speed=0.2,
    quality=-0.01,
)
SpeedModule2 = Module(
    name="Speed module 2",
    stack_size=50,
    rocket_capacity=50,
    energy_consumption=0.6,
    speed=0.3,
    quality=-0.015,
)
SpeedModule3 = Module(
    name="Speed module 3",
    stack_size=50,
    rocket_capacity=50,
    energy_consumption=0.7,
    speed=0.5,
    quality=-0.025,
)

EfficiencyModule1 = Module(
    name="Efficiency module 1",
    stack_size=50,
    rocket_capacity=50,
    energy_consumption=-0.3,
)
EfficiencyModule2 = Module(
    name="Efficiency module 2",
    stack_size=50,
    rocket_capacity=50,
    energy_consumption=-0.4,
)
EfficiencyModule3 = Module(
    name="Efficiency module 3",
    stack_size=50,
    rocket_capacity=50,
    energy_consumption=-0.5,
)

ProductivityModule1 = Module(
    name="Productivity module 1",
    stack_size=50,
    rocket_capacity=50,
    energy_consumption=0.4,
    speed=-0.05,
    productivity=0.04,
)
ProductivityModule2 = Module(
    name="Productivity module 2",
    stack_size=50,
    rocket_capacity=50,
    energy_consumption=0.6,
    speed=-0.1,
    productivity=0.06,
)
ProductivityModule3 = Module(
    name="Productivity module 3",
    stack_size=50,
    rocket_capacity=50,
    energy_consumption=0.8,
    speed=-0.15,
    productivity=0.1,
)

QualityModule1 = Module(
    name="Quality module 1",
    stack_size=50,
    rocket_capacity=50,
    speed=-0.05,
    quality=0.01,
)
QualityModule2 = Module(
    name="Quality module 2",
    stack_size=50,
    rocket_capacity=50,
    speed=-0.05,
    quality=0.02,
)
QualityModule3 = Module(
    name="Quality module 3",
    stack_size=50,
    rocket_capacity=50,
    speed=-0.05,
    quality=0.025,
)

# Intermediate products

Wood = Fuel(name="Wood", stack_size=100, rocket_capacity=500, fuel_value=2_000_000)
Coal = Fuel(name="Coal", stack_size=50, rocket_capacity=500, fuel_value=4_000_000)
Stone = Item(name="Stone", stack_size=50, rocket_capacity=500)
IronOre = Item(name="Iron ore", stack_size=50, rocket_capacity=500)
CopperOre = Item(name="Copper ore", stack_size=50, rocket_capacity=500)
UraniumOre = Item(name="Uranium ore", stack_size=50, rocket_capacity=200)
RawFish = Item(name="Raw fish", stack_size=100, rocket_capacity=300)
Ice = Item(name="Ice", stack_size=50, rocket_capacity=1000)

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
ProcessingUnit = Item(name="Processing unit", stack_size=100, rocket_capacity=300)

EngineUnit = Item(name="Engine unit", stack_size=50, rocket_capacity=400)
ElectricEngineUnit = Item(name="Electric engine unit", stack_size=50, rocket_capacity=400)
FlyingRobotFrame = Item(name="Flying robot frame", stack_size=50, rocket_capacity=150)
LowDensityStructure = Item(name="Low density structure", stack_size=50, rocket_capacity=200)
RocketFuel = Fuel(name="Rocket fuel", stack_size=20, rocket_capacity=100, fuel_value=100_000_000)
RocketPart = Item(name="Rocket part", stack_size=5, rocket_capacity=105)

Uranium235 = Item(name="Uranium-235", stack_size=100, rocket_capacity=20)
Uranium238 = Item(name="Uranium-238", stack_size=100, rocket_capacity=20)
UraniumFuelCell = Fuel(name="Uranium fuel cell", stack_size=50, rocket_capacity=10, fuel_value=8_000_000_000)
DepletedUraniumFuelCell = Item(name="Depleted uranium fuel cell", stack_size=50, rocket_capacity=10)
NuclearFuel = Fuel(name="Nuclear fuel", stack_size=1, rocket_capacity=10, fuel_value=1_210_000_000)

Calcite = Item(name="Calcite", stack_size=50, rocket_capacity=500)
TungstenOre = Item(name="Tungsten ore", stack_size=50, rocket_capacity=100)
TungstenCarbide = Item(name="Tungsten carbide", stack_size=50, rocket_capacity=500)
TungstenPlate = Item(name="Tungsten plate", stack_size=50, rocket_capacity=250)
Scrap = Item(name="Scrap", stack_size=50, rocket_capacity=500)
HolmiumOre = Item(name="Holmium ore", stack_size=50, rocket_capacity=500)
HolmiumPlate = Item(name="Holmium plate", stack_size=100, rocket_capacity=1000)
Superconductor = Item(name="Superconductor", stack_size=200, rocket_capacity=1000)
Supercapacitor = Item(name="Supercapacitor", stack_size=100, rocket_capacity=500)

YumakoSeed = Item(name="Yumako seed", stack_size=10, rocket_capacity=100)
JellynutSeed = Item(name="Jellynut seed", stack_size=10, rocket_capacity=100)
TreeSeed = Item(name="Tree seed", stack_size=10, rocket_capacity=100)
Yumako = Item(name="Yumako", stack_size=50, rocket_capacity=1000)
Jellynut = Item(name="Jellynut", stack_size=50, rocket_capacity=1000)
IronBacteria = Bacteria(name="Iron bacteria", stack_size=50, rocket_capacity=1000, spoil_time=60)
CopperBacteria = Bacteria(name="Copper bacteria", stack_size=50, rocket_capacity=1000, spoil_time=60)
Spoilage = Fuel(name="Spoilage", stack_size=200, rocket_capacity=2000, fuel_value=250_000)
Nutrients = Item(name="Nutrients", stack_size=100, rocket_capacity=2000)

Bioflux = Item(name="Bioflux", stack_size=100, rocket_capacity=1000)
YumakoMash = Fuel(name="Yumako mash", stack_size=100, rocket_capacity=2000, fuel_value=1_000_000)
Jelly = Fuel(name="Jelly", stack_size=100, rocket_capacity=2000, fuel_value=1_000_000)
CarbonFiber = Item(name="Carbon fiber", stack_size=100, rocket_capacity=500)
BiterEgg = Item(name="Biter egg", stack_size=100, rocket_capacity=500)
PentapodEgg = Item(name="Pentapod egg", stack_size=20, rocket_capacity=200)

Lithium = Item(name="Lithium", stack_size=50, rocket_capacity=250)
LithiumPlate = Item(name="Lithium plate", stack_size=100, rocket_capacity=500)
QuantumProcessor = Item(name="Quantum processor", stack_size=100, rocket_capacity=200)
FusionPowerCell = Fuel(name="Fusion power cell", stack_size=50, rocket_capacity=50, fuel_value=40_000_000_000)

AutomationSciencePack = Item(name="Automation science pack", stack_size=200, rocket_capacity=1000)
LogisticsSciencePack = Item(name="Logistics science pack", stack_size=200, rocket_capacity=1000)
MilitarySciencePack = Item(name="Military science pack", stack_size=200, rocket_capacity=1000)
ChemicalSciencePack = Item(name="Chemical science pack", stack_size=200, rocket_capacity=1000)
ProductionSciencePack = Item(name="Production science pack", stack_size=200, rocket_capacity=1000)
UtilitySciencePack = Item(name="Utility science pack", stack_size=200, rocket_capacity=1000)
SpaceSciencePack = Item(name="Space science pack", stack_size=200, rocket_capacity=1000)
MetallurgicSciencePack = Item(name="Metallurgic science pack", stack_size=200, rocket_capacity=1000)
ElectromagneticSciencePack = Item(name="Electromagnetic science pack", stack_size=200, rocket_capacity=1000)
AgriculturalSciencePack = Item(name="Agricultural science pack", stack_size=200, rocket_capacity=1000)
CryogenicSciencePack = Item(name="Cryogenic science pack", stack_size=200, rocket_capacity=1000)
PromethiumSciencePack = Item(name="Promethium science pack", stack_size=200, rocket_capacity=1000)

# Space

RocketSilo = Item(name="Rocket silo", stack_size=1, rocket_capacity=0)
CargoLandingPad = Item(name="Cargo landing pad", stack_size=1, rocket_capacity=1)
SpacePlatformFoundation = Item(name="Space platform foundation", stack_size=100, rocket_capacity=50)
CargoBay = Item(name="Cargo bay", stack_size=10, rocket_capacity=10)
AsteroidCollector = Item(name="Asteroid collector", stack_size=10, rocket_capacity=10)
Crusher = Crafter(name="Crusher", stack_size=10, rocket_capacity=10)
Thruster = Item(name="Thruster", stack_size=10, rocket_capacity=5)
SpacePlatformStarterPack = Item(name="Space platform starter pack", stack_size=1, rocket_capacity=1)


MetallicAsteroidChunk = Item(name="Metallic asteroid chunk", stack_size=1, rocket_capacity=10)
CarbonicAsteroidChunk = Item(name="Carbonic asteroid chunk", stack_size=1, rocket_capacity=10)
OxideAsteroidChunk = Item(name="Oxide asteroid chunk", stack_size=1, rocket_capacity=10)
PromethiumAsteroidChunk = Item(name="Promethium asteroid chunk", stack_size=1, rocket_capacity=10)

SmallMetallicAsteroid = Asteroid(name="Small metallic asteroid", yields={MetallicAsteroidChunk: 2})
MediumMetallicAsteroid = Asteroid(name="Medium metallic asteroid", yields={SmallMetallicAsteroid: 3})
BigMetallicAsteroid = Asteroid(name="Big metallic asteroid", yields={MediumMetallicAsteroid: 3})
HugeMetallicAsteroid = Asteroid(name="Huge metallic asteroid", yields={BigMetallicAsteroid: 3})

SmallCarbonicAsteroid = Asteroid(name="Small carbonic asteroid", yields={CarbonicAsteroidChunk: 2})
MediumCarbonicAsteroid = Asteroid(name="Medium carbonic asteroid", yields={SmallCarbonicAsteroid: 3})
BigCarbonicAsteroid = Asteroid(name="Big carbonic asteroid", yields={MediumCarbonicAsteroid: 3})
HugeCarbonicAsteroid = Asteroid(name="Huge carbonic asteroid", yields={BigCarbonicAsteroid: 3})

SmallOxideAsteroid = Asteroid(name="Small oxide asteroid", yields={OxideAsteroidChunk: 2})
MediumOxideAsteroid = Asteroid(name="Medium oxide asteroid", yields={SmallOxideAsteroid: 3})
BigOxideAsteroid = Asteroid(name="Big oxide asteroid", yields={MediumOxideAsteroid: 3})
HugeOxideAsteroid = Asteroid(name="Huge oxide asteroid", yields={BigOxideAsteroid: 3})

SmallPromethiumAsteroid = Asteroid(name="Small promethium asteroid", yields={PromethiumAsteroidChunk: 2})
MediumPromethiumAsteroid = Asteroid(name="Medium promethium asteroid", yields={SmallPromethiumAsteroid: 3})
BigPromethiumAsteroid = Asteroid(name="Big promethium asteroid", yields={MediumPromethiumAsteroid: 3})
HugePromethiumAsteroid = Asteroid(name="Huge promethium asteroid", yields={BigPromethiumAsteroid: 3})

# Combat

SubmachineGun = Item(name="Submachine gun", stack_size=5, rocket_capacity=5)
Railgun = Item(name="Railgun", stack_size=1, rocket_capacity=1)
TeslaGun = Item(name="Tesla gun", stack_size=5, rocket_capacity=5)
Shotgun = Item(name="Shotgun", stack_size=5, rocket_capacity=5)
CombatShotgun = Item(name="Combat shotgun", stack_size=5, rocket_capacity=5)
RocketLauncher = Item(name="Rocket launcher", stack_size=5, rocket_capacity=5)
Flamethrower = Item(name="Flamethrower", stack_size=5, rocket_capacity=5)

FirearmMagazine = Item(name="Firearm magazine", stack_size=100, rocket_capacity=100)
PiercingRoundsMagazine = Item(name="Piercing rounds magazine", stack_size=100, rocket_capacity=50)
UraniumRoundsMagazine = Item(name="Uranium rounds magazine", stack_size=100, rocket_capacity=25)
ShotgunShells = Item(name="Shotgun shells", stack_size=100, rocket_capacity=100)
PiercingShotgunShells = Item(name="Piercing shotgun shells", stack_size=100, rocket_capacity=50)
CannonShell = Item(name="Cannon shell", stack_size=100, rocket_capacity=50)
ExplosiveCannonShell = Item(name="Explosive cannon shell", stack_size=100, rocket_capacity=50)
UraniumCannonShell = Item(name="Uranium cannon shell", stack_size=100, rocket_capacity=25)
ExplosiveUraniumCannonShell = Item(name="Explosive uranium cannon shell", stack_size=100, rocket_capacity=25)
ArtilleryShell = Item(name="Artillery shell", stack_size=1, rocket_capacity=10)
Rocket = Item(name="Rocket", stack_size=100, rocket_capacity=25)
ExplosiveRocket = Item(name="Explosive rocket", stack_size=100, rocket_capacity=25)
AtomicBomb = Item(name="Atomic bomb", stack_size=10, rocket_capacity=0)
CaptureBotRocket = Item(name="Capture bot rocket", stack_size=10, rocket_capacity=10)
FlamethrowerAmmo = Item(name="Flamethrower ammo", stack_size=100, rocket_capacity=100)
RailgunAmmo = Item(name="Railgun ammo", stack_size=10, rocket_capacity=5)
TeslaAmmo = Item(name="Tesla ammo", stack_size=100, rocket_capacity=100)

Grenade = Item(name="Grenade", stack_size=100, rocket_capacity=100)
ClusterGrenade = Item(name="Cluster grenade", stack_size=100, rocket_capacity=25)
PoisonCapsule = Item(name="Poison capsule", stack_size=100, rocket_capacity=100)
SlowdownCapsule = Item(name="Slowdown capsule", stack_size=100, rocket_capacity=100)
DefenderCapsule = Item(name="Defender capsule", stack_size=100, rocket_capacity=100)
DistractorCapsule = Item(name="Distractor capsule", stack_size=100, rocket_capacity=50)
DestroyerCapsule = Item(name="Destroyer capsule", stack_size=100, rocket_capacity=25)

LightArmor = Item(name="Light armor", stack_size=1, rocket_capacity=1)
HeavyArmor = Item(name="Heavy armor", stack_size=1, rocket_capacity=1)
ModularArmor = Item(name="Modular armor", stack_size=1, rocket_capacity=1)
PowerArmor = Item(name="Power armor", stack_size=1, rocket_capacity=1)
PowerArmorMK2 = Item(name="Power armor MK2", stack_size=1, rocket_capacity=1)
MechArmor = Item(name="Mech armor", stack_size=1, rocket_capacity=1)

PortableSolarPanel = Item(name="Portable solar panel", stack_size=20, rocket_capacity=20)
PortableFissionReactor = Item(name="Portable fission reactor", stack_size=20, rocket_capacity=4)
PortableFusionReactor = Item(name="Portable fusion reactor", stack_size=20, rocket_capacity=1)
PersonalBattery = Item(name="Personal battery", stack_size=20, rocket_capacity=20)
PersonalBatteryMK2 = Item(name="Personal battery MK2", stack_size=20, rocket_capacity=10)
PersonalBatteryMK3 = Item(name="Personal battery MK3", stack_size=20, rocket_capacity=5)
BeltImmunity = Item(name="Belt immunity", stack_size=20, rocket_capacity=20)
Exoskeleton = Item(name="Exoskeleton", stack_size=20, rocket_capacity=12)
PersonalRoboport = Item(name="Personal roboport", stack_size=20, rocket_capacity=9)
PersonalRoboportMK2 = Item(name="Personal roboport MK2", stack_size=20, rocket_capacity=2)
Nightvision = Item(name="Nightvision", stack_size=20, rocket_capacity=20)
ToolbeltEquipment = Item(name="Toolbelt equipment", stack_size=20, rocket_capacity=20)
EnergyShield = Item(name="Energy shield", stack_size=20, rocket_capacity=20)
EnergyShieldMK2 = Item(name="Energy shield MK2", stack_size=20, rocket_capacity=10)
PersonalLaserDefense = Item(name="Personal laser defense", stack_size=20, rocket_capacity=5)
DischargeDefense = Item(name="Discharge defense", stack_size=20, rocket_capacity=4)

Wall = Item(name="Wall", stack_size=100, rocket_capacity=100)
Gate = Item(name="Gate", stack_size=50, rocket_capacity=50)
Radar = Item(name="Radar", stack_size=50, rocket_capacity=50)
LandMine = Item(name="Land mine", stack_size=100, rocket_capacity=100)
GunTurret = Item(name="Gun turret", stack_size=50, rocket_capacity=50)
LaserTurret = Item(name="Laser turret", stack_size=50, rocket_capacity=25)
FlamethrowerTurret = Item(name="Flamethrower turret", stack_size=50, rocket_capacity=20)
ArtilleryTurret = Item(name="Artillery turret", stack_size=10, rocket_capacity=5)
RocketTurret = Item(name="Rocket turret", stack_size=10, rocket_capacity=10)
TeslaTurret = Item(name="Tesla turret", stack_size=10, rocket_capacity=10)
RailgunTurret = Item(name="Railgun turret", stack_size=10, rocket_capacity=1)

# Fluids

Water = Fluid(name="Water")
Steam = Fluid(name="Steam")
CrudeOil = Fluid(name="Crude oil")
PetroleumGas = Fluid(name="Petroleum gas")
LightOil = Fluid(name="Light oil")
HeavyOil = Fluid(name="Heavy oil")
Lubricant = Fluid(name="Lubricant")
SulfuricAcid = Fluid(name="Sulfuric acid")
ThrusterFuel = Fluid(name="Thruster fuel")
ThrusterOxidizer = Fluid(name="Thruster oxidizer")
Lava = Fluid(name="Lava")
MoltenIron = Fluid(name="Molten iron")
MoltenCopper = Fluid(name="Molten copper")
HolmiumSolution = Fluid(name="Holmium solution")
Electrolyte = Fluid(name="Electrolyte")
AmmoniacalSolution = Fluid(name="Ammoniacal solution")
Ammonia = Fluid(name="Ammonia")
Fluorine = Fluid(name="Fluorine")
FluoroketoneHot = Fluid(name="Fluoroketone (hot)")
FluoroketoneCold = Fluid(name="Fluoroketone (cold)")
LithiumBrine = Fluid(name="Lithium brine")
Plasma = Fluid(name="Plasma")
