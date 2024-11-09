from dataclasses import dataclass
from item_types import Entity
from items import (
    Accumulator,
    ActiveProviderChest,
    AdvancedCircuit,
    AgriculturalSciencePack,
    AgriculturalTower,
    Ammonia,
    AmmoniacalSolution,
    ArithmeticCombinator,
    ArtificialJellynutSoil,
    ArtificialYumakoSoil,
    ArtilleryShell,
    ArtilleryWagon,
    AssemblingMachine1,
    AssemblingMachine2,
    AssemblingMachine3,
    AsteroidCollector,
    AtomicBomb,
    AutomationSciencePack,
    Barrel,
    Battery,
    Beacon,
    BigElectricPole,
    BigMiningDrill,
    Biochamber,
    Bioflux,
    Biolab,
    BiterEgg,
    Boiler,
    BufferChest,
    BulkInserter,
    BurnerInserter,
    BurnerMiningDrill,
    Calcite,
    CannonShell,
    CaptiveBiterSpawner,
    CaptureBotRocket,
    Car,
    Carbon,
    CarbonFiber,
    CarbonicAsteroidChunk,
    CargoBay,
    CargoLandingPad,
    CargoWagon,
    Centrifuge,
    ChemicalPlant,
    ChemicalSciencePack,
    CliffExplosives,
    ClusterGrenade,
    Coal,
    CombatShotgun,
    Concrete,
    ConstantCombinator,
    ConstructionRobot,
    CopperCable,
    CopperOre,
    CopperPlate,
    CrudeOil,
    Crusher,
    CryogenicPlant,
    CryogenicSciencePack,
    DeciderCombinator,
    DefenderCapsule,
    DepletedUraniumFuelCell,
    DestroyerCapsule,
    DisplayPanel,
    DistractorCapsule,
    ElectricEngineUnit,
    ElectricFurnace,
    ElectricMiningDrill,
    Electrolyte,
    ElectromagneticPlant,
    ElectromagneticSciencePack,
    ElectronicCircuit,
    EngineUnit,
    Exoskeleton,
    ExplosiveCannonShell,
    ExplosiveRocket,
    ExplosiveUraniumCannonShell,
    Explosives,
    ExpressSplitter,
    ExpressTransportBelt,
    ExpressUndergroundBelt,
    FastInserter,
    FastSplitter,
    FastTransportBelt,
    FastUndergroundBelt,
    FirearmMagazine,
    Flamethrower,
    FlamethrowerAmmo,
    FluidWagon,
    Fluorine,
    FluoroketoneCold,
    FluoroketoneHot,
    FlyingRobotFrame,
    Foundation,
    Foundry,
    FusionGenerator,
    FusionPowerCell,
    FusionReactor,
    Grenade,
    HazardConcrete,
    HeatExchanger,
    HeatPipe,
    HeatingTower,
    HeavyArmor,
    HeavyOil,
    HolmiumOre,
    HolmiumPlate,
    HolmiumSolution,
    Ice,
    Inserter,
    IronChest,
    IronGearWheel,
    IronOre,
    IronPlate,
    IronStick,
    Jelly,
    Jellynut,
    JellynutSeed,
    Lab,
    Lamp,
    Landfill,
    Lava,
    LightArmor,
    LightOil,
    LightningCollector,
    LightningRod,
    Lithium,
    LithiumBrine,
    LithiumPlate,
    Locomotive,
    LogisticRobot,
    LogisticsSciencePack,
    LongHandedInserter,
    LowDensityStructure,
    Lubricant,
    MediumElectricPole,
    MetallicAsteroidChunk,
    MetallurgicSciencePack,
    MilitarySciencePack,
    ModularArmor,
    MoltenCopper,
    MoltenIron,
    NuclearFuel,
    NuclearReactor,
    Nutrients,
    OffshorePump,
    OilRefinery,
    OvergrowthJellynutSoil,
    OvergrowthYumakoSoil,
    OxideAsteroidChunk,
    PassiveProviderChest,
    PentapodEgg,
    PetroleumGas,
    PiercingRoundsMagazine,
    PiercingShotgunShells,
    Pipe,
    PipeToGround,
    PlasticBar,
    PoisonCapsule,
    PortableFissionReactor,
    PowerSwitch,
    ProcessingUnit,
    ProductionSciencePack,
    ProductivityModule1,
    ProgrammableSpeaker,
    PromethiumAsteroidChunk,
    PromethiumSciencePack,
    Pump,
    Pumpjack,
    QuantumProcessor,
    Radar,
    Rail,
    RailChainSignal,
    RailRamp,
    RailSignal,
    RailSupport,
    Railgun,
    RailgunAmmo,
    RawFish,
    Recycler,
    RefinedConcrete,
    RefinedHazardConcrete,
    RepairPack,
    RequesterChest,
    Roboport,
    Rocket,
    RocketFuel,
    RocketLauncher,
    RocketPart,
    RocketSilo,
    RocketTurret,
    Scrap,
    SelectorCombinator,
    Shotgun,
    ShotgunShells,
    SlowdownCapsule,
    SmallElectricPole,
    SolarPanel,
    SolidFuel,
    SpacePlatformFoundation,
    SpacePlatformStarterPack,
    SpaceSciencePack,
    SpeedModule1,
    SpeedModule2,
    SpeedModule3,
    Spidertron,
    Splitter,
    Spoilage,
    StackInserter,
    Steam,
    SteamEngine,
    SteamTurbine,
    SteelChest,
    SteelFurnace,
    SteelPlate,
    Stone,
    StoneBrick,
    StoneFurnace,
    StorageChest,
    StorageTank,
    SubmachineGun,
    Substation,
    Sulfur,
    SulfuricAcid,
    Supercapacitor,
    Superconductor,
    Tank,
    TeslaAmmo,
    TeslaGun,
    Thruster,
    ThrusterFuel,
    ThrusterOxidizer,
    TrainStop,
    TransportBelt,
    TreeSeed,
    TungstenCarbide,
    TungstenOre,
    TungstenPlate,
    TurboSplitter,
    TurboTransportBelt,
    TurboUndergroundBelt,
    UndergroundBelt,
    Uranium235,
    Uranium238,
    UraniumCannonShell,
    UraniumFuelCell,
    UraniumOre,
    UraniumRoundsMagazine,
    UtilitySciencePack,
    Wall,
    Water,
    Wood,
    WoodenChest,
    Yumako,
    YumakoMash,
    YumakoSeed,
)


@dataclass
class Recipe:
    inputs: dict[Entity, int]
    """Required items/fluids"""
    outputs: dict[Entity, int] = {}
    """Items/fluids produced by recipe"""
    output_probabilities: dict[Entity, float] = {}
    """Probability of each output, in (0, 1) range"""
    crafting_time: float = 0.5
    """Crafting time, in seconds"""


# Logistics

WoodenChestRecipe = Recipe(
    inputs={Wood: 2},
    outputs={WoodenChest: 1},
)
IronChestRecipe = Recipe(
    inputs={IronPlate: 8},
    outputs={IronChest: 1},
)
SteelChestRecipe = Recipe(
    inputs={SteelPlate: 8},
    outputs={SteelChest: 1},
)
StorageTankRecipe = Recipe(
    inputs={IronPlate: 20, SteelPlate: 5},
    outputs={StorageTank: 1},
    crafting_time=3,
)

TransportBeltRecipe = Recipe(
    inputs={IronPlate: 1, IronGearWheel: 1},
    outputs={TransportBelt: 1},
)
FastTransportBeltRecipe = Recipe(
    inputs={IronGearWheel: 5, TransportBelt: 1},
    outputs={FastTransportBelt: 1},
)
ExpressTransportBeltRecipe = Recipe(
    inputs={IronGearWheel: 10, FastTransportBelt: 1, Lubricant: 20},
    outputs={ExpressTransportBelt: 1},
)
TurboTransportBeltRecipe = Recipe(
    inputs={TungstenPlate: 5, ExpressTransportBelt: 1, Lubricant: 20},
    outputs={TurboTransportBelt: 1},
)

UndergroundBeltRecipe = Recipe(
    inputs={IronPlate: 10, TransportBelt: 5},
    outputs={UndergroundBelt: 2},
    crafting_time=1,
)
FastUndergroundBeltRecipe = Recipe(
    inputs={IronGearWheel: 40, UndergroundBelt: 2},
    outputs={FastUndergroundBelt: 2},
    crafting_time=2,
)
ExpressUndergroundBeltRecipe = Recipe(
    inputs={IronGearWheel: 80, FastUndergroundBelt: 2, Lubricant: 40},
    outputs={ExpressUndergroundBelt: 2},
    crafting_time=2,
)
TurboUndergroundBeltRecipe = Recipe(
    inputs={TungstenPlate: 40, ExpressUndergroundBelt: 2, Lubricant: 40},
    outputs={TurboUndergroundBelt: 2},
    crafting_time=2,
)

SplitterRecipe = Recipe(
    inputs={IronPlate: 5, ElectronicCircuit: 5, TransportBelt: 4},
    outputs={Splitter: 1},
    crafting_time=1,
)
FastSplitterRecipe = Recipe(
    inputs={IronGearWheel: 10, ElectronicCircuit: 10, Splitter: 1},
    outputs={FastSplitter: 1},
    crafting_time=2,
)
ExpressSplitterRecipe = Recipe(
    inputs={IronGearWheel: 10, AdvancedCircuit: 10, FastSplitter: 1, Lubricant: 80},
    outputs={ExpressSplitter: 1},
    crafting_time=2,
)
TurboSplitterRecipe = Recipe(
    inputs={ProcessingUnit: 2, TungstenPlate: 15, ExpressSplitter: 1, Lubricant: 80},
    outputs={TurboSplitter: 1},
    crafting_time=2,
)

BurnerInserterRecipe = Recipe(
    inputs={IronPlate: 1, IronGearWheel: 1},
    outputs={BurnerInserter: 1},
)
InserterRecipe = Recipe(
    inputs={IronPlate: 1, IronGearWheel: 1, ElectronicCircuit: 1},
    outputs={Inserter: 1},
)
LongHandedInserterRecipe = Recipe(
    inputs={IronPlate: 1, IronGearWheel: 1, Inserter: 1},
    outputs={LongHandedInserter: 1},
)
FastInserterRecipe = Recipe(
    inputs={IronPlate: 2, ElectronicCircuit: 2, Inserter: 1},
    outputs={FastInserter: 1},
)
BulkInserterRecipe = Recipe(
    inputs={IronGearWheel: 15, ElectronicCircuit: 15, AdvancedCircuit: 1, FastInserter: 1},
    outputs={BulkInserter: 1},
)
StackInserterRecipe = Recipe(
    inputs={ProcessingUnit: 1, Jelly: 10, CarbonFiber: 2, BulkInserter: 1},
    outputs={StackInserter: 1},
)

SmallElectricPoleRecipe = Recipe(
    inputs={Wood: 1, CopperCable: 2},
    outputs={SmallElectricPole: 2},
)
MediumElectricPoleRecipe = Recipe(
    inputs={SteelPlate: 2, IronStick: 4, CopperCable: 2},
    outputs={MediumElectricPole: 1},
)
BigElectricPoleRecipe = Recipe(
    inputs={SteelPlate: 5, IronStick: 8, CopperCable: 4},
    outputs={BigElectricPole: 1},
)
SubstationRecipe = Recipe(
    inputs={SteelPlate: 10, CopperCable: 6, AdvancedCircuit: 5},
    outputs={Substation: 1},
)

PipeRecipe = Recipe(
    inputs={IronPlate: 1},
    outputs={Pipe: 1},
)
PipeToGroundRecipe = Recipe(
    inputs={IronPlate: 5, Pipe: 10},
    outputs={PipeToGround: 2},
)
PumpRecipe = Recipe(
    inputs={SteelPlate: 1, EngineUnit: 1, Pipe: 1},
    outputs={Pump: 1},
    crafting_time=2,
)
CastingPipeRecipe = Recipe(
    inputs={MoltenIron: 10},
    outputs={Pipe: 1},
    crafting_time=1,
)
CastingPipeToGroundRecipe = Recipe(
    inputs={Pipe: 10, MoltenIron: 50},
    outputs={PipeToGround: 2},
    crafting_time=1,
)

RailRecipe = Recipe(
    inputs={Stone: 1, SteelPlate: 1, IronStick: 1},
    outputs={Rail: 2},
)
RailRampRecipe = Recipe(
    inputs={SteelPlate: 10, Rail: 8, RefinedConcrete: 100},
    outputs={RailRamp: 1},
)
RailSupportRecipe = Recipe(
    inputs={SteelPlate: 10, RefinedConcrete: 20},
    outputs={RailSupport: 1},
)
TrainStopRecipe = Recipe(
    inputs={IronPlate: 6, SteelPlate: 3, IronStick: 6, ElectronicCircuit: 5},
    outputs={TrainStop: 1},
)
RailSignalRecipe = Recipe(
    inputs={IronPlate: 5, ElectronicCircuit: 1},
    outputs={RailSignal: 1},
)
RailChainSignalRecipe = Recipe(
    inputs={IronPlate: 5, ElectronicCircuit: 1},
    outputs={RailChainSignal: 1},
)
LocomotiveRecipe = Recipe(
    inputs={SteelPlate: 30, ElectronicCircuit: 10, EngineUnit: 20},
    outputs={Locomotive: 1},
    crafting_time=4,
)
CargoWagonRecipe = Recipe(
    inputs={IronPlate: 20, SteelPlate: 20, IronGearWheel: 10},
    outputs={CargoWagon: 1},
    crafting_time=1,
)
FluidWagonRecipe = Recipe(
    inputs={SteelPlate: 16, IronGearWheel: 10, StorageTank: 1, Pipe: 8},
    outputs={FluidWagon: 1},
    crafting_time=1.5,
)
ArtilleryWagonRecipe = Recipe(
    inputs={IronGearWheel: 40, ProcessingUnit: 10, EngineUnit: 60, TungstenPlate: 60, RefinedConcrete: 60},
    outputs={ArtilleryWagon: 1},
    crafting_time=4,
)

CarRecipe = Recipe(
    inputs={IronPlate: 20, SteelPlate: 5, EngineUnit: 8},
    outputs={Car: 1},
    crafting_time=2,
)
TankRecipe = Recipe(
    inputs={SteelPlate: 50, IronGearWheel: 15, AdvancedCircuit: 10, EngineUnit: 32},
    outputs={Tank: 1},
    crafting_time=5,
)
SpidertronRecipe = Recipe(
    inputs={RawFish: 1, PortableFissionReactor: 2, Exoskeleton: 4, Radar: 2, RocketTurret: 1},
    outputs={Spidertron: 1},
    crafting_time=10,
)

LogisticRobotRecipe = Recipe(
    inputs={AdvancedCircuit: 2, FlyingRobotFrame: 1},
    outputs={LogisticRobot: 1},
)
ConstructionRobotRecipe = Recipe(
    inputs={ElectronicCircuit: 2, FlyingRobotFrame: 1},
    outputs={ConstructionRobot: 1},
)
ActiveProviderChestRecipe = Recipe(
    inputs={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1},
    outputs={ActiveProviderChest: 1},
)
PassiveProviderChestRecipe = Recipe(
    inputs={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1},
    outputs={PassiveProviderChest: 1},
)
StorageChestRecipe = Recipe(
    inputs={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1},
    outputs={StorageChest: 1},
)
BufferChestRecipe = Recipe(
    inputs={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1},
    outputs={BufferChest: 1},
)
RequesterChestRecipe = Recipe(
    inputs={ElectronicCircuit: 3, AdvancedCircuit: 1, SteelChest: 1},
    outputs={RequesterChest: 1},
)
RoboportRecipe = Recipe(
    inputs={SteelPlate: 45, IronGearWheel: 45, AdvancedCircuit: 45},
    outputs={Roboport: 1},
    crafting_time=5,
)

LampRecipe = Recipe(
    inputs={IronPlate: 1, CopperCable: 3, ElectronicCircuit: 1},
    outputs={Lamp: 1},
)
ArithmeticCombinatorRecipe = Recipe(
    inputs={CopperCable: 5, ElectronicCircuit: 5},
    outputs={ArithmeticCombinator: 1},
)
DeciderCombinatorRecipe = Recipe(
    inputs={CopperCable: 5, ElectronicCircuit: 5},
    outputs={DeciderCombinator: 1},
)
SelectorCombinatorRecipe = Recipe(
    inputs={AdvancedCircuit: 2, DeciderCombinator: 5},
    outputs={SelectorCombinator: 1},
)
ConstantCombinatorRecipe = Recipe(
    inputs={CopperCable: 5, ElectronicCircuit: 5},
    outputs={ConstantCombinator: 1},
)
PowerSwitchRecipe = Recipe(
    inputs={IronPlate: 5, CopperCable: 5, ElectronicCircuit: 2},
    outputs={PowerSwitch: 1},
    crafting_time=2,
)
ProgrammableSpeakerRecipe = Recipe(
    inputs={IronPlate: 3, IronStick: 4, CopperCable: 5, ElectronicCircuit: 4},
    outputs={ProgrammableSpeaker: 1},
    crafting_time=2,
)
DisplayPanelRecipe = Recipe(
    inputs={IronPlate: 1, ElectronicCircuit: 1},
    outputs={DisplayPanel: 1},
)

StoneBrickRecipe = Recipe(
    inputs={Stone: 2},
    outputs={StoneBrick: 1},
    crafting_time=3.2,
)
ConcreteRecipe = Recipe(
    inputs={IronOre: 1, StoneBrick: 5, Water: 100},
    outputs={Concrete: 10},
    crafting_time=10,
)
HazardConcreteRecipe = Recipe(
    inputs={Concrete: 10},
    outputs={HazardConcrete: 10},
    crafting_time=0.25,
)
RefinedConcreteRecipe = Recipe(
    inputs={SteelPlate: 1, IronStick: 8, Concrete: 20, Water: 100},
    outputs={RefinedConcrete: 10},
    crafting_time=15,
)
RefinedHazardConcreteRecipe = Recipe(
    inputs={RefinedConcrete: 10},
    outputs={RefinedHazardConcrete: 10},
    crafting_time=0.25,
)
LandfillRecipe = Recipe(
    inputs={Stone: 50},
    outputs={Landfill: 1},
)
ArtificialYumakoSoilRecipe = Recipe(
    inputs={YumakoSeed: 2, Nutrients: 50, Landfill: 5},
    outputs={ArtificialYumakoSoil: 10},
    crafting_time=2,
)
OvergrowthYumakoSoilRecipe = Recipe(
    inputs={YumakoSeed: 5, Spoilage: 50, BiterEgg: 10, ArtificialYumakoSoil: 2, Water: 100},
    outputs={OvergrowthYumakoSoil: 1},
    crafting_time=10,
)
ArtificialJellynutSoilRecipe = Recipe(
    inputs={JellynutSeed: 2, Nutrients: 50, Landfill: 5},
    outputs={ArtificialJellynutSoil: 10},
    crafting_time=2,
)
OvergrowthJellynutSoilRecipe = Recipe(
    inputs={JellynutSeed: 5, Spoilage: 50, BiterEgg: 10, ArtificialJellynutSoil: 2, Water: 100},
    outputs={OvergrowthJellynutSoil: 1},
    crafting_time=10,
)
IcePlatformRecipe = Recipe(
    inputs={Ice: 50, Ammonia: 400},
    outputs={Ice: 1},
    crafting_time=30,
)
FoundationRecipe = Recipe(
    inputs={Stone: 20, TungstenPlate: 4, CarbonFiber: 4, LithiumPlate: 4, FluoroketoneCold: 20},
    outputs={Foundation: 1},
    crafting_time=30,
)
CliffExplosivesRecipe = Recipe(
    inputs={Explosives: 10, Barrel: 1, Calcite: 10, Grenade: 1},
    outputs={CliffExplosives: 1},
    crafting_time=8,
)

# Production

RepairPackRecipe = Recipe(
    inputs={IronGearWheel: 2, ElectronicCircuit: 2},
    outputs={RepairPack: 1},
)

BoilerRecipe = Recipe(
    inputs={Pipe: 4, StoneFurnace: 1},
    outputs={Boiler: 1},
)
SteamEngineRecipe = Recipe(
    inputs={IronPlate: 10, IronGearWheel: 8, Pipe: 5},
    outputs={SteamEngine: 1},
)
SolarPanelRecipe = Recipe(
    inputs={CopperPlate: 5, SteelPlate: 5, ElectronicCircuit: 15},
    outputs={SolarPanel: 1},
    crafting_time=10,
)
AccumulatorRecipe = Recipe(
    inputs={IronPlate: 2, Battery: 5},
    outputs={Accumulator: 1},
    crafting_time=10,
)
NuclearReactorRecipe = Recipe(
    inputs={CopperPlate: 500, SteelPlate: 500, AdvancedCircuit: 500, Concrete: 500},
    outputs={NuclearReactor: 1},
    crafting_time=8,
)
HeatPipeRecipe = Recipe(
    inputs={CopperPlate: 20, SteelPlate: 10},
    outputs={HeatPipe: 1},
    crafting_time=1,
)
HeatExchangerRecipe = Recipe(
    inputs={CopperPlate: 100, SteelPlate: 10, Pipe: 10},
    outputs={HeatExchanger: 1},
    crafting_time=3,
)
SteamTurbineRecipe = Recipe(
    inputs={CopperPlate: 50, IronGearWheel: 50, Pipe: 20},
    outputs={SteamTurbine: 1},
    crafting_time=3,
)
FusionReactorRecipe = Recipe(
    inputs={TungstenPlate: 200, Superconductor: 200, QuantumProcessor: 250},
    outputs={FusionReactor: 1},
    crafting_time=60,
)
FusionGeneratorRecipe = Recipe(
    inputs={TungstenPlate: 100, Superconductor: 100, QuantumProcessor: 50},
    outputs={FusionGenerator: 1},
    crafting_time=30,
)

BurnerMiningDrillRecipe = Recipe(
    inputs={IronPlate: 3, IronGearWheel: 3, StoneFurnace: 1},
    outputs={BurnerMiningDrill: 1},
    crafting_time=2,
)
ElectricMiningDrillRecipe = Recipe(
    inputs={IronPlate: 10, IronGearWheel: 5, ElectronicCircuit: 3},
    outputs={ElectricMiningDrill: 1},
    crafting_time=2,
)
BigMiningDrillRecipe = Recipe(
    inputs={
        AdvancedCircuit: 10,
        ElectricEngineUnit: 10,
        TungstenPlate: 20,
        ElectricMiningDrill: 1,
        MoltenIron: 200,
    },
    outputs={BigMiningDrill: 1},
    crafting_time=30,
)
OffshorePumpRecipe = Recipe(
    inputs={IronGearWheel: 3, Pipe: 3},
    outputs={OffshorePump: 1},
)
PumpjackRecipe = Recipe(
    inputs={SteelPlate: 5, IronGearWheel: 10, ElectronicCircuit: 5, Pipe: 10},
    outputs={Pumpjack: 1},
    crafting_time=5,
)

StoneFurnaceRecipe = Recipe(
    inputs={Stone: 5},
    outputs={StoneFurnace: 1},
)
SteelFurnaceRecipe = Recipe(
    inputs={SteelPlate: 6, StoneBrick: 10},
    outputs={SteelFurnace: 1},
    crafting_time=3,
)
ElectricFurnaceRecipe = Recipe(
    inputs={SteelPlate: 10, AdvancedCircuit: 5, StoneBrick: 10},
    outputs={ElectricFurnace: 1},
    crafting_time=5,
)
FoundryRecipe = Recipe(
    inputs={SteelPlate: 50, ElectronicCircuit: 30, TungstenCarbide: 50, RefinedConcrete: 20, Lubricant: 20},
    outputs={Foundry: 1},
    crafting_time=10,
)
RecyclerRecipe = Recipe(
    inputs={SteelPlate: 20, IronGearWheel: 40, ProcessingUnit: 6, Concrete: 20},
    outputs={Recycler: 1},
    crafting_time=3,
)

AgriculturalTowerRecipe = Recipe(
    inputs={SteelPlate: 10, ElectronicCircuit: 3, Spoilage: 20, Landfill: 1},
    outputs={AgriculturalTower: 1},
    crafting_time=10,
)
BiochamberRecipe = Recipe(
    inputs={IronPlate: 20, ElectronicCircuit: 5, Nutrients: 5, PentapodEgg: 1, Landfill: 1},
    outputs={Biochamber: 1},
    crafting_time=20,
)
CaptiveBiterSpawnerRecipe = Recipe(
    inputs={Uranium235: 15, BiterEgg: 10, CaptureBotRocket: 1, FluoroketoneCold: 100},
    outputs={CaptiveBiterSpawner: 1},
    crafting_time=10,
)

AssemblingMachine1Recipe = Recipe(
    inputs={IronPlate: 9, IronGearWheel: 5, ElectronicCircuit: 3},
    outputs={AssemblingMachine1: 1},
)
AssemblingMachine2Recipe = Recipe(
    inputs={SteelPlate: 2, IronGearWheel: 5, ElectronicCircuit: 3, AssemblingMachine1: 1},
    outputs={AssemblingMachine2: 1},
)
AssemblingMachine3Recipe = Recipe(
    inputs={AssemblingMachine2: 2, SpeedModule1: 4},
    outputs={AssemblingMachine3: 1},
)
OilRefineryRecipe = Recipe(
    inputs={SteelPlate: 15, IronGearWheel: 10, ElectronicCircuit: 10, Pipe: 10, StoneBrick: 10},
    outputs={OilRefinery: 1},
    crafting_time=8,
)
ChemicalPlantRecipe = Recipe(
    inputs={SteelPlate: 5, IronGearWheel: 5, ElectronicCircuit: 5, Pipe: 5},
    outputs={ChemicalPlant: 1},
    crafting_time=5,
)
CentrifugeRecipe = Recipe(
    inputs={SteelPlate: 50, IronGearWheel: 100, AdvancedCircuit: 100, Concrete: 100},
    outputs={Centrifuge: 1},
    crafting_time=4,
)
ElectromagneticPlantRecipe = Recipe(
    inputs={SteelPlate: 50, ProcessingUnit: 50, HolmiumPlate: 150, RefinedConcrete: 50},
    outputs={ElectromagneticPlant: 1},
    crafting_time=10,
)
CryogenicPlantRecipe = Recipe(
    inputs={ProcessingUnit: 20, Superconductor: 20, LithiumPlate: 20, RefinedConcrete: 40},
    outputs={CryogenicPlant: 1},
    crafting_time=10,
)
LabRecipe = Recipe(
    inputs={IronGearWheel: 10, ElectronicCircuit: 10, TransportBelt: 4},
    outputs={Lab: 1},
    crafting_time=2,
)
BiolabRecipe = Recipe(
    inputs={Uranium235: 3, BiterEgg: 10, RefinedConcrete: 25, Lab: 1, CaptureBotRocket: 2},
    outputs={Biolab: 1},
    crafting_time=10,
)

LightningRodRecipe = Recipe(
    inputs={SteelPlate: 8, CopperCable: 12, StoneBrick: 4},
    outputs={LightningRod: 1},
    crafting_time=5,
)
LightningCollectorRecipe = Recipe(
    inputs={Supercapacitor: 8, Accumulator: 1, LightningRod: 1, Electrolyte: 80},
    outputs={LightningCollector: 1},
    crafting_time=5,
)
HeatingTowerRecipe = Recipe(
    inputs={Concrete: 20, Boiler: 2, HeatPipe: 5},
    outputs={HeatingTower: 1},
    crafting_time=10,
)

BeaconRecipe = Recipe(
    inputs={SteelPlate: 10, CopperCable: 10, ElectronicCircuit: 20, AdvancedCircuit: 20},
    outputs={Beacon: 1},
    crafting_time=15,
)

SpeedModule1Recipe = Recipe(
    inputs={ElectronicCircuit: 5, AdvancedCircuit: 5},
    outputs={SpeedModule1: 1},
    crafting_time=15,
)

SpeedModule2Recipe = Recipe(
    inputs={AdvancedCircuit: 5, ProcessingUnit: 5, SpeedModule1: 4},
    outputs={SpeedModule2: 1},
    crafting_time=30,
)

SpeedModule3Recipe = Recipe(
    inputs={AdvancedCircuit: 5, ProcessingUnit: 5, TungstenCarbide: 1, SpeedModule2: 4},
    outputs={SpeedModule3: 1},
    crafting_time=60,
)

# TODO: remaining module recipes

# Intermediate products

BasicOilProcessingRecipe = Recipe(
    inputs={CrudeOil: 100},
    outputs={PetroleumGas: 45},
    crafting_time=5,
)

AdvancedOilProcessingRecipe = Recipe(
    inputs={Water: 50, CrudeOil: 100},
    outputs={HeavyOil: 25, LightOil: 45, PetroleumGas: 55},
    crafting_time=5,
)

SimpleCoalLiquefactionRecipeCoalLiquefactionRecipe = Recipe(
    inputs={Coal: 10, Calcite: 2, SulfuricAcid: 25},
    outputs={HeavyOil: 50},
    crafting_time=5,
)

CoalLiquefactionRecipe = Recipe(
    inputs={Coal: 10, HeavyOil: 25, Steam: 50},
    outputs={HeavyOil: 90, LightOil: 20, PetroleumGas: 10},
    crafting_time=5,
)

HeavyOilCrackingToLightOilRecipe = Recipe(
    inputs={Water: 30, HeavyOil: 40},
    outputs={LightOil: 30},
    crafting_time=2,
)

LightOilCrackingToPetroleumGasRecipe = Recipe(
    inputs={Water: 30, LightOil: 30},
    outputs={PetroleumGas: 20},
    crafting_time=2,
)

SolidFuelFromPetroleumGasRecipe = Recipe(
    inputs={PetroleumGas: 20},
    outputs={SolidFuel: 1},
    crafting_time=1,
)

SolidFuelFromLightOilRecipe = Recipe(
    inputs={LightOil: 10},
    outputs={SolidFuel: 1},
    crafting_time=1,
)

SolidFuelFromHeavyOilRecipe = Recipe(
    inputs={HeavyOil: 20},
    outputs={SolidFuel: 1},
    crafting_time=1,
)

AcidNeutralisationRecipe = Recipe(
    inputs={Calcite: 1, SulfuricAcid: 1000},
    outputs={Steam: 10000},
    crafting_time=5,
)

SteamCondensationRecipe = Recipe(
    inputs={Steam: 1000},
    outputs={Water: 90},
    crafting_time=1,
)

IceMeltingRecipe = Recipe(
    inputs={Ice: 1},
    outputs={Water: 20},
    crafting_time=1,
)

IronPlateRecipe = Recipe(
    inputs={IronOre: 1},
    outputs={IronPlate: 1},
    crafting_time=3.2,
)

CopperPlateRecipe = Recipe(
    inputs={CopperOre: 1},
    outputs={CopperPlate: 1},
    crafting_time=3.2,
)

SteelPlateRecipe = Recipe(
    inputs={IronPlate: 5},
    outputs={SteelPlate: 1},
    crafting_time=16,
)

PlasticBarRecipe = Recipe(
    inputs={Coal: 1, PetroleumGas: 20},
    outputs={PlasticBar: 2},
    crafting_time=1,
)

SulfurRecipe = Recipe(
    inputs={Water: 30, PetroleumGas: 30},
    outputs={Sulfur: 2},
    crafting_time=1,
)

BatteryRecipe = Recipe(
    inputs={IronPlate: 1, CopperPlate: 1, SulfuricAcid: 20},
    outputs={Battery: 1},
    crafting_time=4,
)

ExplosivesRecipe = Recipe(
    inputs={Coal: 1, Sulfur: 1, Water: 10},
    outputs={Explosives: 2},
    crafting_time=4,
)

CarbonRecipe = Recipe(
    inputs={Coal: 2, SulfuricAcid: 20},
    outputs={Carbon: 1},
    crafting_time=1,
)

CoalSynthesisRecipe = Recipe(
    inputs={Sulfur: 1, Carbon: 5, Water: 10},
    outputs={Coal: 1},
    crafting_time=2,
)

IronGearWheelRecipe = Recipe(
    inputs={IronPlate: 2},
    outputs={IronGearWheel: 1},
)

IronStickRecipe = Recipe(
    inputs={IronPlate: 1},
    outputs={IronStick: 1},
)

CopperCableRecipe = Recipe(
    inputs={CopperPlate: 1},
    outputs={CopperCable: 2},
)

BarrelRecipe = Recipe(
    inputs={SteelPlate: 1},
    outputs={Barrel: 1},
    crafting_time=1,
)

ElectronicCircuitRecipe = Recipe(
    inputs={IronPlate: 1, CopperCable: 3},
    outputs={ElectronicCircuit: 1},
)

AdvancedCircuitRecipe = Recipe(
    inputs={PlasticBar: 2, CopperCable: 4, ElectronicCircuit: 2},
    outputs={AdvancedCircuit: 1},
    crafting_time=6,
)

ProcessingUnitRecipe = Recipe(
    inputs={ElectronicCircuit: 20, AdvancedCircuit: 2, SulfuricAcid: 5},
    outputs={ProcessingUnit: 1},
    crafting_time=10,
)

EngineUnitRecipe = Recipe(
    inputs={SteelPlate: 1, IronGearWheel: 1, Pipe: 2},
    outputs={EngineUnit: 1},
    crafting_time=10,
)

ElectricEngineUnitRecipe = Recipe(
    inputs={ElectronicCircuit: 2, EngineUnit: 1, Lubricant: 15},
    outputs={ElectricEngineUnit: 1},
    crafting_time=10,
)

FlyingRobotFrameRecipe = Recipe(
    inputs={SteelPlate: 1, Battery: 2, ElectronicCircuit: 3, ElectricEngineUnit: 1},
    outputs={FlyingRobotFrame: 1},
    crafting_time=20,
)

LowDensityStructureRecipe = Recipe(
    inputs={CopperPlate: 20, SteelPlate: 2, PlasticBar: 5},
    outputs={LowDensityStructure: 1},
    crafting_time=15,
)

RocketFuelRecipe = Recipe(
    inputs={SolidFuel: 10, LightOil: 10},
    outputs={RocketFuel: 1},
    crafting_time=15,
)

RocketPartRecipe = Recipe(
    inputs={ProcessingUnit: 1, LowDensityStructure: 1, RocketFuel: 1},
    outputs={RocketPart: 1},
    crafting_time=3,
)

UraniumFuelCellRecipe = Recipe(
    inputs={IronPlate: 10, Uranium235: 1, Uranium238: 19},
    outputs={UraniumFuelCell: 10},
    crafting_time=10,
)

NuclearFuelRecipe = Recipe(
    inputs={RocketFuel: 1, Uranium235: 1},
    outputs={NuclearFuel: 1},
    crafting_time=90,
)

UraniumProcessingRecipe = Recipe(
    inputs={UraniumOre: 10},
    output_probabilities={Uranium235: 0.007, Uranium238: 0.993},
    crafting_time=12,
)

NuclearFuelReprocessingRecipe = Recipe(
    inputs={DepletedUraniumFuelCell: 5},
    outputs={Uranium238: 3},
    crafting_time=60,
)

KovarexEnrichmentProcessRecipe = Recipe(
    inputs={Uranium235: 40, Uranium238: 5},
    outputs={Uranium235: 41, Uranium238: 2},
    crafting_time=60,
)

TungstenCarbideRecipe = Recipe(
    inputs={Carbon: 1, TungstenOre: 2, SulfuricAcid: 10},
    outputs={TungstenCarbide: 1},
    crafting_time=1,
)

TungstenPlateRecipe = Recipe(
    inputs={TungstenOre: 4, MoltenIron: 10},
    outputs={TungstenPlate: 1},
    crafting_time=10,
)

MoltenIronFromLavaRecipe = Recipe(
    inputs={Calcite: 1, Lava: 500},
    outputs={Stone: 10, MoltenIron: 250},
    crafting_time=16,
)

MoltenCopperFromLavaRecipe = Recipe(
    inputs={Calcite: 1, Lava: 500},
    outputs={Stone: 15, MoltenCopper: 250},
    crafting_time=16,
)

CastingIronRecipe = Recipe(
    inputs={MoltenIron: 20},
    outputs={IronPlate: 2},
    crafting_time=3.2,
)

CastingCopperRecipe = Recipe(
    inputs={MoltenCopper: 20},
    outputs={CopperPlate: 2},
    crafting_time=3.2,
)

CastingSteelRecipe = Recipe(
    inputs={MoltenIron: 30},
    outputs={SteelPlate: 1},
    crafting_time=3.2,
)

CastingIronGearWheelRecipe = Recipe(
    inputs={MoltenIron: 10},
    outputs={IronGearWheel: 1},
    crafting_time=1,
)

CastingIronStickRecipe = Recipe(
    inputs={MoltenIron: 20},
    outputs={IronStick: 4},
    crafting_time=1,
)

CastingLowDensityStructureRecipe = Recipe(
    inputs={PlasticBar: 5, MoltenIron: 80, MoltenCopper: 250},
    outputs={LowDensityStructure: 1},
    crafting_time=15,
)

ConcreteFromMoltenIronRecipe = Recipe(
    inputs={StoneBrick: 5, MoltenIron: 20, Water: 100},
    outputs={Concrete: 10},
    crafting_time=10,
)

CastingCopperCableRecipe = Recipe(
    inputs={MoltenCopper: 5},
    outputs={CopperCable: 2},
    crafting_time=1,
)

HolmiumPlateRecipe = Recipe(
    inputs={HolmiumSolution: 20},
    outputs={HolmiumPlate: 1},
    crafting_time=1,
)

SuperconductorRecipe = Recipe(
    inputs={CopperPlate: 1, PlasticBar: 1, HolmiumPlate: 1, LightOil: 5},
    outputs={Superconductor: 2},
    crafting_time=5,
)

SupercapacitorRecipe = Recipe(
    inputs={Battery: 1, ElectronicCircuit: 4, HolmiumPlate: 2, Superconductor: 2, Electrolyte: 10},
    outputs={Supercapacitor: 1},
    crafting_time=10,
)

ScrapRecyclingRecipe = Recipe(
    inputs={Scrap: 1},
    output_probabilities={
        ProcessingUnit: 0.02,
        AdvancedCircuit: 0.03,
        LowDensityStructure: 0.01,
        SolidFuel: 0.07,
        SteelPlate: 0.04,
        Concrete: 0.06,
        Battery: 0.04,
        Ice: 0.05,
        Stone: 0.04,
        HolmiumOre: 0.01,
        IronGearWheel: 0.2,
        CopperCable: 0.03,
    },
    crafting_time=0.2,
)

YumakoProcessingRecipe = Recipe(
    inputs={Yumako: 1},
    outputs={YumakoMash: 2},
    output_probabilities={YumakoSeed: 0.02},
    crafting_time=1,
)

JellynutProcessingRecipe = Recipe(
    inputs={Jellynut: 1},
    outputs={Jelly: 4},
    output_probabilities={JellynutSeed: 0.02},
    crafting_time=1,
)

NutrientsFromSpoilageRecipe = Recipe(
    inputs={Spoilage: 10},
    output_probabilities={Nutrients: 0.5, Spoilage: 0.5},
    crafting_time=2,
)

NutrientsFromYumakoMashRecipe = Recipe(
    inputs={YumakoMash: 4},
    outputs={Nutrients: 6},
    crafting_time=4,
)

NutrientsFromBiofluxRecipe = Recipe(
    inputs={Bioflux: 5},
    outputs={Nutrients: 40},
    crafting_time=2,
)

BiofluxRecipe = Recipe(
    inputs={YumakoMash: 15, Jelly: 12},
    outputs={Bioflux: 4},
    crafting_time=6,
)

CarbonFiberRecipe = Recipe(
    inputs={Carbon: 1, YumakoMash: 10},
    outputs={CarbonFiber: 1},
    crafting_time=5,
)

BiterEggRecipe = Recipe(
    inputs={},
    outputs={BiterEgg: 5},
    crafting_time=10,
)

PentapodEggRecipe = Recipe(
    inputs={Nutrients: 30, PentapodEgg: 1, Water: 60},
    outputs={PentapodEgg: 2},
    crafting_time=15,
)

RocketFuelFromJellyRecipe = Recipe(
    inputs={Bioflux: 2, Jelly: 30, Water: 30},
    outputs={RocketFuel: 1},
    crafting_time=10,
)

BiolubricantRecipe = Recipe(
    inputs={Jelly: 60},
    outputs={Lubricant: 20},
    crafting_time=3,
)

BioplasticRecipe = Recipe(
    inputs={Bioflux: 1, YumakoMash: 4},
    outputs={PlasticBar: 3},
    crafting_time=2,
)

BiosulfurRecipe = Recipe(
    inputs={Spoilage: 5, Bioflux: 1},
    outputs={Sulfur: 2},
    crafting_time=2,
)

BurntSpoilageRecipe = Recipe(
    inputs={Spoilage: 6},
    outputs={Carbon: 1},
    crafting_time=12,
)

WoodProcessingRecipe = Recipe(
    inputs={Wood: 2},
    outputs={TreeSeed: 1},
    crafting_time=2,
)

FishBreedingRecipe = Recipe(
    inputs={RawFish: 2, Nutrients: 100, Water: 100},
    outputs={RawFish: 3},
    crafting_time=6,
)

NutrientsFromFishRecipe = Recipe(
    inputs={RawFish: 1},
    outputs={Nutrients: 20},
    crafting_time=2,
)

NutrientsFromBiterEggRecipe = Recipe(
    inputs={BiterEgg: 1},
    outputs={Nutrients: 20},
    crafting_time=2,
)

LithiumRecipe = Recipe(
    inputs={HolmiumPlate: 1, LithiumBrine: 50, Ammonia: 50},
    outputs={Lithium: 5},
    crafting_time=20,
)

LithiumPlateRecipe = Recipe(
    inputs={Lithium: 1},
    outputs={LithiumPlate: 1},
    crafting_time=6.4,
)

QuantumProcessorRecipe = Recipe(
    inputs={
        ProcessingUnit: 1,
        TungstenCarbide: 1,
        Superconductor: 1,
        CarbonFiber: 1,
        LithiumPlate: 2,
        FluoroketoneCold: 10,
    },
    outputs={QuantumProcessor: 1, FluoroketoneHot: 5},
    crafting_time=30,
)

FusionPowerCellRecipe = Recipe(
    inputs={HolmiumPlate: 1, LithiumPlate: 5, Ammonia: 100},
    outputs={FusionPowerCell: 1},
    crafting_time=10,
)

AmmoniacalSolutionSeparationRecipe = Recipe(
    inputs={AmmoniacalSolution: 50},
    outputs={Ice: 5, Ammonia: 50},
    crafting_time=1,
)

SolidFuelFromAmmoniaRecipe = Recipe(
    inputs={Ammonia: 50, CrudeOil: 20},
    outputs={SolidFuel: 1},
    crafting_time=1,
)

AmmoniaRocketFuelRecipe = Recipe(
    inputs={SolidFuel: 3, Water: 50, Ammonia: 500},
    outputs={RocketFuel: 1},
    crafting_time=10,
)

FluoroketoneRecipe = Recipe(
    inputs={SolidFuel: 1, Lithium: 1, Fluorine: 50, Ammonia: 50},
    outputs={FluoroketoneHot: 50},
    crafting_time=10,
)

CoolingHotFluoroketoneRecipe = Recipe(
    inputs={FluoroketoneHot: 10},
    outputs={FluoroketoneCold: 10},
    crafting_time=5,
)

AutomationSciencePackRecipe = Recipe(
    inputs={CopperPlate: 1, IronGearWheel: 1},
    outputs={AutomationSciencePack: 1},
    crafting_time=5,
)

LogisticsSciencePackRecipe = Recipe(
    inputs={TransportBelt: 1, Inserter: 1},
    outputs={LogisticsSciencePack: 1},
    crafting_time=6,
)

MilitarySciencePackRecipe = Recipe(
    inputs={PiercingRoundsMagazine: 1, Grenade: 1, Wall: 2},
    outputs={MilitarySciencePack: 2},
    crafting_time=10,
)

ChemicalSciencePackRecipe = Recipe(
    inputs={Sulfur: 1, AdvancedCircuit: 3, EngineUnit: 2},
    outputs={ChemicalSciencePack: 2},
    crafting_time=24,
)

ProductionSciencePackRecipe = Recipe(
    inputs={Rail: 30, ElectricFurnace: 1, ProductivityModule1: 1},
    outputs={ProductionSciencePack: 3},
    crafting_time=21,
)

UtilitySciencePackRecipe = Recipe(
    inputs={ProcessingUnit: 2, FlyingRobotFrame: 1, LowDensityStructure: 3},
    outputs={UtilitySciencePack: 3},
    crafting_time=21,
)

SpaceSciencePackRecipe = Recipe(
    inputs={Ice: 1, IronPlate: 2, Carbon: 1},
    outputs={SpaceSciencePack: 5},
    crafting_time=15,
)

MetallurgicSciencePackRecipe = Recipe(
    inputs={TungstenCarbide: 3, TungstenPlate: 2, MoltenCopper: 200},
    outputs={MetallurgicSciencePack: 1},
    crafting_time=10,
)

ElectromagneticSciencePackRecipe = Recipe(
    inputs={Supercapacitor: 1, Accumulator: 1, Electrolyte: 25, HolmiumSolution: 25},
    outputs={ElectromagneticSciencePack: 1},
    crafting_time=10,
)

AgriculturalSciencePackRecipe = Recipe(
    inputs={Bioflux: 1, PentapodEgg: 1},
    outputs={AgriculturalSciencePack: 1},
    crafting_time=4,
)

CryogenicSciencePackRecipe = Recipe(
    inputs={Ice: 3, LithiumPlate: 1, FluoroketoneCold: 6},
    outputs={CryogenicSciencePack: 1, FluoroketoneHot: 3},
    crafting_time=20,
)

PromethiumSciencePackRecipe = Recipe(
    inputs={BiterEgg: 10, QuantumProcessor: 1, PromethiumAsteroidChunk: 25},
    outputs={PromethiumSciencePack: 10},
    crafting_time=5,
)

# Space

RocketSiloRecipe = Recipe(
    inputs={SteelPlate: 1000, ProcessingUnit: 200, ElectricEngineUnit: 200, Pipe: 100, Concrete: 1000},
    outputs={RocketSilo: 1},
    crafting_time=30,
)

CargoLandingPadRecipe = Recipe(
    inputs={SteelPlate: 25, ProcessingUnit: 10, Concrete: 200},
    outputs={CargoLandingPad: 1},
    crafting_time=30,
)

SpacePlatformFoundationRecipe = Recipe(
    inputs={SteelPlate: 20, CopperCable: 20},
    outputs={SpacePlatformFoundation: 1},
    crafting_time=10,
)

CargoBayRecipe = Recipe(
    inputs={SteelPlate: 20, ProcessingUnit: 5, LowDensityStructure: 20},
    outputs={CargoBay: 1},
    crafting_time=10,
)

AsteroidCollectorRecipe = Recipe(
    inputs={ProcessingUnit: 5, ElectricEngineUnit: 8, LowDensityStructure: 20},
    outputs={AsteroidCollector: 1},
    crafting_time=10,
)

CrusherRecipe = Recipe(
    inputs={SteelPlate: 10, ElectricEngineUnit: 10, LowDensityStructure: 20},
    outputs={Crusher: 1},
    crafting_time=10,
)

ThrusterRecipe = Recipe(
    inputs={SteelPlate: 10, ProcessingUnit: 10, ElectricEngineUnit: 5},
    outputs={Thruster: 1},
    crafting_time=10,
)

SpacePlatformStarterPackRecipe = Recipe(
    inputs={SteelPlate: 20, ProcessingUnit: 20, SpacePlatformFoundation: 60},
    outputs={SpacePlatformStarterPack: 1},
    crafting_time=60,
)

MetallicAsteroidCrushingRecipe = Recipe(
    inputs={MetallicAsteroidChunk: 1},
    outputs={IronOre: 20},
    output_probabilities={MetallicAsteroidChunk: 0.2},
    crafting_time=2,
)

CarbonicAsteroidCrushingRecipe = Recipe(
    inputs={CarbonicAsteroidChunk: 1},
    outputs={Carbon: 10},
    output_probabilities={CarbonicAsteroidChunk: 0.2},
    crafting_time=2,
)

OxideAsteroidCrushingRecipe = Recipe(
    inputs={OxideAsteroidChunk: 1},
    outputs={Ice: 5},
    output_probabilities={OxideAsteroidChunk: 0.2},
    crafting_time=2,
)

MetallicAsteroidReprocessingRecipe = Recipe(
    inputs={MetallicAsteroidChunk: 1},
    output_probabilities={MetallicAsteroidChunk: 0.4, CarbonicAsteroidChunk: 0.2, OxideAsteroidChunk: 0.2},
    crafting_time=2,
)

CarbonicAsteroidReprocessingRecipe = Recipe(
    inputs={CarbonicAsteroidChunk: 1},
    output_probabilities={MetallicAsteroidChunk: 0.2, CarbonicAsteroidChunk: 0.4, OxideAsteroidChunk: 0.2},
    crafting_time=2,
)

OxideAsteroidReprocessingRecipe = Recipe(
    inputs={OxideAsteroidChunk: 1},
    output_probabilities={MetallicAsteroidChunk: 0.2, CarbonicAsteroidChunk: 0.2, OxideAsteroidChunk: 0.4},
    crafting_time=1,
)

AdvancedMetalAsteroidCrushingRecipe = Recipe(
    inputs={MetallicAsteroidChunk: 1},
    outputs={IronOre: 10, CopperOre: 4},
    output_probabilities={MetallicAsteroidChunk: 0.05},
    crafting_time=5,
)

AdvancedCarbonicAsteroidCrushingRecipe = Recipe(
    inputs={CarbonicAsteroidChunk: 1},
    outputs={Carbon: 5, Sulfur: 2},
    output_probabilities={CarbonicAsteroidChunk: 0.05},
    crafting_time=5,
)

AdvancedOxideAsteroidCrushingRecipe = Recipe(
    inputs={OxideAsteroidChunk: 1},
    outputs={Ice: 3, Calcite: 2},
    output_probabilities={OxideAsteroidChunk: 0.05},
    crafting_time=5,
)

AdvancedThrusterFuelRecipe = Recipe(
    inputs={Carbon: 2, Calcite: 1, Water: 100},
    outputs={ThrusterFuel: 1500},
    crafting_time=10,
)

AdvancedThrusterOxidizerRecipe = Recipe(
    inputs={IronOre: 2, Calcite: 1, Water: 100},
    outputs={ThrusterOxidizer: 1500},
    crafting_time=10,
)

# Combat

SubmachineGunRecipe = Recipe(
    inputs={IronPlate: 10, CopperPlate: 5, IronGearWheel: 10},
    outputs={SubmachineGun: 1},
    crafting_time=10,
)

RailgunRecipe = Recipe(
    inputs={TungstenPlate: 10, Superconductor: 10, QuantumProcessor: 20, FluoroketoneCold: 10},
    outputs={Railgun: 1},
    crafting_time=10,
)

TeslaGunRecipe = Recipe(
    inputs={PlasticBar: 30, HolmiumPlate: 10, Superconductor: 10, Electrolyte: 100},
    outputs={TeslaGun: 1},
    crafting_time=30,
)

ShotgunRecipe = Recipe(
    inputs={Wood: 5, IronPlate: 15, CopperPlate: 10, IronGearWheel: 5},
    outputs={Shotgun: 1},
    crafting_time=10,
)

CombatShotgunRecipe = Recipe(
    inputs={Wood: 10, CopperPlate: 10, SteelPlate: 15, IronGearWheel: 5},
    outputs={CombatShotgun: 1},
    crafting_time=10,
)

RocketLauncherRecipe = Recipe(
    inputs={IronPlate: 5, IronGearWheel: 5, ElectronicCircuit: 5},
    outputs={RocketLauncher: 1},
    crafting_time=10,
)

FlamethrowerRecipe = Recipe(
    inputs={SteelPlate: 5, IronGearWheel: 1},
    outputs={Flamethrower: 1},
    crafting_time=10,
)

FirearmMagazineRecipe = Recipe(
    inputs={IronPlate: 4},
    outputs={FirearmMagazine: 1},
    crafting_time=1,
)

PiercingRoundsMagazineRecipe = Recipe(
    inputs={CopperPlate: 5, SteelPlate: 1, FirearmMagazine: 1},
    outputs={PiercingRoundsMagazine: 1},
    crafting_time=3,
)

UraniumRoundsMagazineRecipe = Recipe(
    inputs={Uranium238: 1, PiercingRoundsMagazine: 1},
    outputs={UraniumRoundsMagazine: 1},
    crafting_time=10,
)

ShotgunShellsRecipe = Recipe(
    inputs={IronPlate: 2, CopperPlate: 2},
    outputs={ShotgunShells: 1},
    crafting_time=3,
)

PiercingShotgunShellsRecipe = Recipe(
    inputs={CopperPlate: 5, SteelPlate: 2, ShotgunShells: 2},
    outputs={PiercingShotgunShells: 1},
    crafting_time=8,
)

CannonShellRecipe = Recipe(
    inputs={SteelPlate: 2, PlasticBar: 2, Explosives: 1},
    outputs={CannonShell: 1},
    crafting_time=8,
)

ExplosiveCannonShellRecipe = Recipe(
    inputs={SteelPlate: 2, PlasticBar: 2, Explosives: 2},
    outputs={ExplosiveCannonShell: 1},
    crafting_time=8,
)

UraniumCannonShellRecipe = Recipe(
    inputs={Uranium238: 1, CannonShell: 1},
    outputs={UraniumCannonShell: 1},
    crafting_time=12,
)

ExplosiveUraniumCannonShellRecipe = Recipe(
    inputs={Uranium238: 1, ExplosiveCannonShell: 1},
    outputs={ExplosiveUraniumCannonShell: 1},
    crafting_time=12,
)

ArtilleryShellRecipe = Recipe(
    inputs={Explosives: 8, Calcite: 1, TungstenPlate: 4, Radar: 1},
    outputs={ArtilleryShell: 1},
    crafting_time=15,
)

RocketRecipe = Recipe(
    inputs={IronPlate: 2, Explosives: 1},
    outputs={Rocket: 1},
    crafting_time=4,
)

ExplosiveRocketRecipe = Recipe(
    inputs={Explosives: 2, Rocket: 1},
    outputs={ExplosiveRocket: 1},
    crafting_time=8,
)

AtomicBombRecipe = Recipe(
    inputs={Explosives: 10, ProcessingUnit: 10, Uranium235: 100},
    outputs={AtomicBomb: 1},
    crafting_time=50,
)

CaptureBotRocketRecipe = Recipe(
    inputs={SteelPlate: 2, ProcessingUnit: 2, FlyingRobotFrame: 1, Bioflux: 20},
    outputs={CaptureBotRocket: 1},
    crafting_time=10,
)

FlamethrowerAmmoRecipe = Recipe(
    inputs={SteelPlate: 5, CrudeOil: 100},
    outputs={FlamethrowerAmmo: 1},
    crafting_time=6,
)

RailgunAmmoRecipe = Recipe(
    inputs={SteelPlate: 5, Explosives: 2, CopperPlate: 10},
    outputs={RailgunAmmo: 1},
    crafting_time=25,
)

TeslaAmmoRecipe = Recipe(
    inputs={PlasticBar: 1, Supercapacitor: 1, Electrolyte: 10},
    outputs={TeslaAmmo: 1},
    crafting_time=30,
)

GrenadeRecipe = Recipe(
    inputs={Coal: 10, IronPlate: 5},
    outputs={Grenade: 1},
    crafting_time=8,
)

ClusterGrenadeRecipe = Recipe(
    inputs={SteelPlate: 5, Explosives: 5, Grenade: 8},
    outputs={ClusterGrenade: 1},
    crafting_time=8,
)

PoisonCapsuleRecipe = Recipe(
    inputs={Coal: 10, SteelPlate: 3, ElectronicCircuit: 3},
    outputs={PoisonCapsule: 1},
    crafting_time=8,
)

SlowdownCapsuleRecipe = Recipe(
    inputs={Coal: 5, SteelPlate: 2, ElectronicCircuit: 2},
    outputs={SlowdownCapsule: 1},
    crafting_time=8,
)

DefenderCapsuleRecipe = Recipe(
    inputs={IronGearWheel: 3, ElectronicCircuit: 3, PiercingRoundsMagazine: 3},
    outputs={DefenderCapsule: 1},
    crafting_time=8,
)

DistractorCapsuleRecipe = Recipe(
    inputs={AdvancedCircuit: 3, DefenderCapsule: 4},
    outputs={DistractorCapsule: 1},
    crafting_time=15,
)

DestroyerCapsuleRecipe = Recipe(
    inputs={SteelPlate: 4, ProcessingUnit: 1, DistractorCapsule: 4},
    outputs={DestroyerCapsule: 1},
    crafting_time=15,
)

LightArmorRecipe = Recipe(
    inputs={IronPlate: 40},
    outputs={LightArmor: 1},
    crafting_time=3,
)

HeavyArmorRecipe = Recipe(
    inputs={CopperPlate: 100, SteelPlate: 50},
    outputs={HeavyArmor: 1},
    crafting_time=8,
)

ModularArmorRecipe = Recipe(
    inputs={SteelPlate: 50, AdvancedCircuit: 30},
    outputs={ModularArmor: 1},
    crafting_time=15,
)

# TODO: remaining recipes

# Fluids
