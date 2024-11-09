from dataclasses import dataclass
from item_types import Entity
from items import (
    Accumulator,
    AdvancedCircuit,
    Ammonia,
    ArtificialJellynutSoil,
    ArtificialYumakoSoil,
    AssemblingMachine1,
    AssemblingMachine2,
    Barrel,
    Battery,
    BiterEgg,
    Boiler,
    BulkInserter,
    Calcite,
    CaptureBotRocket,
    CarbonFiber,
    Concrete,
    CopperCable,
    CopperPlate,
    DeciderCombinator,
    ElectricEngineUnit,
    ElectricMiningDrill,
    Electrolyte,
    ElectronicCircuit,
    EngineUnit,
    Exoskeleton,
    Explosives,
    ExpressSplitter,
    ExpressTransportBelt,
    ExpressUndergroundBelt,
    FastInserter,
    FastSplitter,
    FastTransportBelt,
    FastUndergroundBelt,
    FluoroketoneCold,
    FlyingRobotFrame,
    Grenade,
    HeatPipe,
    HolmiumPlate,
    Ice,
    Inserter,
    IronGearWheel,
    IronOre,
    IronPlate,
    IronStick,
    Jelly,
    JellynutSeed,
    Lab,
    Landfill,
    LightningRod,
    LithiumPlate,
    Lubricant,
    MoltenIron,
    Nutrients,
    PentapodEgg,
    Pipe,
    PortableFissionReactor,
    ProcessingUnit,
    QuantumProcessor,
    Radar,
    Rail,
    RawFish,
    RefinedConcrete,
    RocketTurret,
    SpeedModule1,
    Splitter,
    Spoilage,
    SteelChest,
    SteelPlate,
    Stone,
    StoneBrick,
    StoneFurnace,
    StorageTank,
    Supercapacitor,
    Superconductor,
    TransportBelt,
    TungstenCarbide,
    TungstenPlate,
    UndergroundBelt,
    Uranium235,
    Water,
    Wood,
    YumakoSeed,
)


@dataclass
class Recipe:
    requirements: dict[Entity, int]
    """Required items/fluids"""
    crafting_time: float = 0.5
    """Crafting time, in seconds"""
    items_produced: int = 1
    """Items produced per crafting time"""


# Logistics

WoodenChestRecipe = Recipe(requirements={Wood: 2})
IronChestRecipe = Recipe(requirements={IronPlate: 8})
SteelChestRecipe = Recipe(requirements={SteelPlate: 8})
StorageTankRecipe = Recipe(requirements={IronPlate: 20, SteelPlate: 5}, crafting_time=3)

TransportBeltRecipe = Recipe(requirements={IronPlate: 1, IronGearWheel: 1}, items_produced=2)
FastTransportBeltRecipe = Recipe(requirements={IronGearWheel: 5, TransportBelt: 1})
ExpressTransportBeltRecipe = Recipe(requirements={IronGearWheel: 10, FastTransportBelt: 1, Lubricant: 20})
TurboTransportBeltRecipe = Recipe(requirements={TungstenPlate: 5, ExpressTransportBelt: 1, Lubricant: 20})

UndergroundBeltRecipe = Recipe(requirements={IronPlate: 10, TransportBelt: 5}, crafting_time=1, items_produced=2)
FastUndergroundBeltRecipe = Recipe(
    requirements={IronGearWheel: 40, UndergroundBelt: 2}, crafting_time=2, items_produced=2
)
ExpressUndergroundBeltRecipe = Recipe(
    requirements={IronGearWheel: 80, FastUndergroundBelt: 2, Lubricant: 40}, crafting_time=2, items_produced=2
)
TurboUndergroundBeltRecipe = Recipe(
    requirements={TungstenPlate: 40, ExpressUndergroundBelt: 2, Lubricant: 40}, crafting_time=2, items_produced=2
)

SplitterRecipe = Recipe(requirements={IronPlate: 5, ElectronicCircuit: 5, TransportBelt: 4}, crafting_time=1)
FastSplitterRecipe = Recipe(requirements={IronGearWheel: 10, ElectronicCircuit: 10, Splitter: 1}, crafting_time=2)
ExpressSplitterRecipe = Recipe(
    requirements={IronGearWheel: 10, AdvancedCircuit: 10, FastSplitter: 1, Lubricant: 80}, crafting_time=2
)
TurboSplitterRecipe = Recipe(
    requirements={ProcessingUnit: 2, TungstenPlate: 15, ExpressSplitter: 1, Lubricant: 80}, crafting_time=2
)

BurnerInserterRecipe = Recipe(requirements={IronPlate: 1, IronGearWheel: 1})
InserterRecipe = Recipe(requirements={IronPlate: 1, IronGearWheel: 1, ElectronicCircuit: 1})
LongHandedInserterRecipe = Recipe(requirements={IronPlate: 1, IronGearWheel: 1, Inserter: 1})
FastInserterRecipe = Recipe(requirements={IronPlate: 2, ElectronicCircuit: 2, Inserter: 1})
BulkInserterRecipe = Recipe(
    requirements={IronGearWheel: 15, ElectronicCircuit: 15, AdvancedCircuit: 1, FastInserter: 1}
)
StackInserterRecipe = Recipe(requirements={ProcessingUnit: 1, Jelly: 10, CarbonFiber: 2, BulkInserter: 1})

SmallElectricPoleRecipe = Recipe(requirements={Wood: 1, CopperCable: 2}, items_produced=2)
MediumElectricPoleRecipe = Recipe(requirements={SteelPlate: 2, IronStick: 4, CopperCable: 2})
BigElectricPoleRecipe = Recipe(requirements={SteelPlate: 5, IronStick: 8, CopperCable: 4})
SubstationRecipe = Recipe(requirements={SteelPlate: 10, CopperCable: 6, AdvancedCircuit: 5})

PipeRecipe = Recipe(requirements={IronPlate: 1})
PipeToGroundRecipe = Recipe(requirements={IronPlate: 5, Pipe: 10}, items_produced=2)
PumpRecipe = Recipe(requirements={SteelPlate: 1, EngineUnit: 1, Pipe: 1}, crafting_time=2)
CastingPipeRecipe = Recipe(requirements={MoltenIron: 10}, crafting_time=1)
CastingPipeToGroundRecipe = Recipe(requirements={Pipe: 10, MoltenIron: 50}, crafting_time=1, items_produced=2)

RailRecipe = Recipe(requirements={Stone: 1, SteelPlate: 1, IronStick: 1}, items_produced=2)
RailRampRecipe = Recipe(requirements={SteelPlate: 10, Rail: 8, RefinedConcrete: 100})
RailSupportRecipe = Recipe(requirements={SteelPlate: 10, RefinedConcrete: 20})
TrainStopRecipe = Recipe(requirements={IronPlate: 6, SteelPlate: 3, IronStick: 6, ElectronicCircuit: 5})
RailSignalRecipe = Recipe(requirements={IronPlate: 5, ElectronicCircuit: 1})
RailChainSignalRecipe = Recipe(requirements={IronPlate: 5, ElectronicCircuit: 1})
LocomotiveRecipe = Recipe(requirements={SteelPlate: 30, ElectronicCircuit: 10, EngineUnit: 20}, crafting_time=4)
CargoWagonRecipe = Recipe(requirements={IronPlate: 20, SteelPlate: 20, IronGearWheel: 10}, crafting_time=1)
FluidWagonRecipe = Recipe(requirements={SteelPlate: 16, IronGearWheel: 10, StorageTank: 1, Pipe: 8}, crafting_time=1.5)
ArtilleryWagonRecipe = Recipe(
    requirements={IronGearWheel: 40, ProcessingUnit: 10, EngineUnit: 60, TungstenPlate: 60, RefinedConcrete: 60},
    crafting_time=4,
)

CarRecipe = Recipe(requirements={IronPlate: 20, SteelPlate: 5, EngineUnit: 8}, crafting_time=2)
TankRecipe = Recipe(
    requirements={SteelPlate: 50, IronGearWheel: 15, AdvancedCircuit: 10, EngineUnit: 32}, crafting_time=5
)
SpidertronRecipe = Recipe(
    requirements={RawFish: 1, PortableFissionReactor: 2, Exoskeleton: 4, Radar: 2, RocketTurret: 1}, crafting_time=10
)

LogisticRobotRecipe = Recipe(requirements={AdvancedCircuit: 2, FlyingRobotFrame: 1})
ConstructionRobotRecipe = Recipe(requirements={ElectronicCircuit: 2, FlyingRobotFrame: 1})
ActiveProviderChestRecipe = Recipe(requirements={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1})
PassiveProviderChestRecipe = Recipe(requirements={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1})
StorageChestRecipe = Recipe(requirements={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1})
BufferChestRecipe = Recipe(requirements={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1})
RequesterChestRecipe = Recipe(requirements={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1})
RoboportRecipe = Recipe(requirements={SteelPlate: 45, IronGearWheel: 45, AdvancedCircuit: 45}, crafting_time=5)

LampRecipe = Recipe(requirements={IronPlate: 1, CopperCable: 3, ElectronicCircuit: 1})
ArithmeticCombinatorRecipe = Recipe(requirements={CopperCable: 5, ElectronicCircuit: 5})
DeciderCombinatorRecipe = Recipe(requirements={CopperCable: 5, ElectronicCircuit: 5})
SelectorCombinatorRecipe = Recipe(requirements={AdvancedCircuit: 2, DeciderCombinator: 5})
ConstantCombinatorRecipe = Recipe(requirements={CopperCable: 5, ElectronicCircuit: 5})
PowerSwitchRecipe = Recipe(requirements={IronPlate: 5, CopperCable: 5, ElectronicCircuit: 2}, crafting_time=2)
ProgrammableSpeakerRecipe = Recipe(
    requirements={IronPlate: 3, IronStick: 4, CopperCable: 5, ElectronicCircuit: 4}, crafting_time=2
)
DisplayPanelRecipe = Recipe(requirements={IronPlate: 1, ElectronicCircuit: 1})

StoneBrickRecipe = Recipe(requirements={Stone: 2}, crafting_time=3.2)
ConcreteRecipe = Recipe(requirements={IronOre: 1, StoneBrick: 5, Water: 100}, crafting_time=10, items_produced=10)
HazardConcreteRecipe = Recipe(requirements={Concrete: 10}, crafting_time=0.25, items_produced=10)
RefinedConcreteRecipe = Recipe(
    requirements={SteelPlate: 1, IronStick: 8, Concrete: 20, Water: 100}, crafting_time=15, items_produced=10
)
RefinedHazardConcreteRecipe = Recipe(requirements={RefinedConcrete: 10}, crafting_time=0.25, items_produced=10)
LandfillRecipe = Recipe(requirements={Stone: 50})
ArtificialYumakoSoilRecipe = Recipe(
    requirements={YumakoSeed: 2, Nutrients: 50, Landfill: 5}, crafting_time=2, items_produced=10
)
OvergrowthYumakoSoilRecipe = Recipe(
    requirements={YumakoSeed: 5, Spoilage: 50, BiterEgg: 10, ArtificialYumakoSoil: 2, Water: 100}, crafting_time=10
)
ArtificialJellynutSoilRecipe = Recipe(
    requirements={JellynutSeed: 2, Nutrients: 50, Landfill: 5}, crafting_time=2, items_produced=10
)
OvergrowthJellynutSoilRecipe = Recipe(
    requirements={JellynutSeed: 5, Spoilage: 50, BiterEgg: 10, ArtificialJellynutSoil: 2, Water: 100}, crafting_time=10
)
IcePlatformRecipe = Recipe(requirements={Ice: 50, Ammonia: 400}, crafting_time=30)
FoundationRecipe = Recipe(
    requirements={Stone: 20, TungstenPlate: 4, CarbonFiber: 4, LithiumPlate: 4, FluoroketoneCold: 20}, crafting_time=30
)
CliffExplosivesRecipe = Recipe(requirements={Explosives: 10, Barrel: 1, Calcite: 10, Grenade: 1}, crafting_time=8)

# Production

RepairPackRecipe = Recipe(requirements={IronGearWheel: 2, ElectronicCircuit: 2})

BoilerRecipe = Recipe(requirements={Pipe: 4, StoneFurnace: 1})
SteamEngineRecipe = Recipe(requirements={IronPlate: 10, IronGearWheel: 8, Pipe: 5})
SolarPanelRecipe = Recipe(requirements={CopperPlate: 5, SteelPlate: 5, ElectronicCircuit: 15}, crafting_time=10)
AccumulatorRecipe = Recipe(requirements={IronPlate: 2, Battery: 5}, crafting_time=10)
NuclearReactorRecipe = Recipe(
    requirements={CopperPlate: 500, SteelPlate: 500, AdvancedCircuit: 500, Concrete: 500}, crafting_time=8
)
HeatPipeRecipe = Recipe(requirements={CopperPlate: 20, SteelPlate: 10}, crafting_time=1)
HeatExchangerRecipe = Recipe(requirements={CopperPlate: 100, SteelPlate: 10, Pipe: 10}, crafting_time=3)
SteamTurbineRecipe = Recipe(requirements={CopperPlate: 50, IronGearWheel: 50, Pipe: 20}, crafting_time=3)
FusionReactorRecipe = Recipe(
    requirements={TungstenPlate: 200, Superconductor: 200, QuantumProcessor: 250}, crafting_time=60
)
FusionGeneratorRecipe = Recipe(
    requirements={TungstenPlate: 100, Superconductor: 100, QuantumProcessor: 50}, crafting_time=30
)

BurnerMiningDrillRecipe = Recipe(requirements={IronPlate: 3, IronGearWheel: 3, StoneFurnace: 1}, crafting_time=2)
ElectricMiningDrillRecipe = Recipe(
    requirements={IronPlate: 10, IronGearWheel: 5, ElectronicCircuit: 3}, crafting_time=2
)
BigMiningDrillRecipe = Recipe(
    requirements={
        AdvancedCircuit: 10,
        ElectricEngineUnit: 10,
        TungstenPlate: 20,
        ElectricMiningDrill: 1,
        MoltenIron: 200,
    },
    crafting_time=30,
)
OffshorePumpRecipe = Recipe(requirements={IronGearWheel: 3, Pipe: 3})
PumpjackRecipe = Recipe(
    requirements={SteelPlate: 5, IronGearWheel: 10, ElectronicCircuit: 5, Pipe: 10}, crafting_time=5
)

StoneFurnaceRecipe = Recipe(requirements={Stone: 5})
SteelFurnaceRecipe = Recipe(requirements={SteelPlate: 6, StoneBrick: 10}, crafting_time=3)
ElectricFurnaceRecipe = Recipe(requirements={SteelPlate: 10, AdvancedCircuit: 5, StoneBrick: 10}, crafting_time=5)
FoundryRecipe = Recipe(
    requirements={SteelPlate: 50, ElectronicCircuit: 30, TungstenCarbide: 50, RefinedConcrete: 20, Lubricant: 20},
    crafting_time=10,
)
RecyclerRecipe = Recipe(
    requirements={SteelPlate: 20, IronGearWheel: 40, ProcessingUnit: 6, Concrete: 20}, crafting_time=3
)

AgriculturalTowerRecipe = Recipe(
    requirements={SteelPlate: 10, ElectronicCircuit: 3, Spoilage: 20, Landfill: 1}, crafting_time=10
)
BiochamberRecipe = Recipe(
    requirements={IronPlate: 20, ElectronicCircuit: 5, Nutrients: 5, PentapodEgg: 1, Landfill: 1}, crafting_time=20
)
CaptiveBiterSpawnerRecipe = Recipe(
    requirements={Uranium235: 15, BiterEgg: 10, CaptureBotRocket: 1, FluoroketoneCold: 100}, crafting_time=10
)

AssemblingMachine1Recipe = Recipe(requirements={IronPlate: 9, IronGearWheel: 5, ElectronicCircuit: 3})
AssemblingMachine2Recipe = Recipe(
    requirements={SteelPlate: 2, IronGearWheel: 5, ElectronicCircuit: 3, AssemblingMachine1: 1}
)
AssemblingMachine3Recipe = Recipe(requirements={AssemblingMachine2: 2, SpeedModule1: 4})
OilRefineryRecipe = Recipe(
    requirements={SteelPlate: 15, IronGearWheel: 10, ElectronicCircuit: 10, Pipe: 10, StoneBrick: 10}, crafting_time=8
)
ChemicalPlantRecipe = Recipe(
    requirements={SteelPlate: 5, IronGearWheel: 5, ElectronicCircuit: 5, Pipe: 5}, crafting_time=5
)
CentrifugeRecipe = Recipe(
    requirements={SteelPlate: 50, IronGearWheel: 100, AdvancedCircuit: 100, Concrete: 100}, crafting_time=4
)
ElectromagneticPlantRecipe = Recipe(
    requirements={SteelPlate: 50, ProcessingUnit: 50, HolmiumPlate: 150, RefinedConcrete: 50}, crafting_time=10
)
CryogenicPlantRecipe = Recipe(
    requirements={ProcessingUnit: 20, Superconductor: 20, LithiumPlate: 20, RefinedConcrete: 40}, crafting_time=10
)
LabRecipe = Recipe(requirements={IronGearWheel: 10, ElectronicCircuit: 10, TransportBelt: 4}, crafting_time=2)
BiolabRecipe = Recipe(
    requirements={Uranium235: 3, BiterEgg: 10, RefinedConcrete: 25, Lab: 1, CaptureBotRocket: 2}, crafting_time=10
)

LightningRodRecipe = Recipe(requirements={SteelPlate: 8, CopperCable: 12, StoneBrick: 4}, crafting_time=5)
LightningCollectorRecipe = Recipe(
    requirements={Supercapacitor: 8, Accumulator: 1, LightningRod: 1, Electrolyte: 80}, crafting_time=5
)
HeatingTowerRecipe = Recipe(requirements={Concrete: 20, Boiler: 2, HeatPipe: 5}, crafting_time=10)

BeaconRecipe = Recipe(
    requirements={SteelPlate: 10, CopperCable: 10, ElectronicCircuit: 20, AdvancedCircuit: 20}, crafting_time=15
)

# Intermediate products

# Space

# Combat

# Fluids
