from typing import List, Dict, Literal, TypedDict
from .trader import _RawTrader

LangType = Literal['en', 'ru', 'de', 'fr', 'es', 'cn']


class Item(_RawTrader):
    uid: str
    bsgId: str
    name: str
    shortName: str
    price: int
    basePrice: int
    avg24hPrice: int
    avg7daysPrice: int
    updated: str
    slots: int
    diff24h: int
    diff7days: int
    icon: str
    link: str
    wikiLink: str
    img: str
    imgBig: str
    reference: str


class Point3D(TypedDict, total=False):
    x: int
    y: int
    z: int


class BSGPrefab(TypedDict, total=False):
    path: str
    rcid: str


class Filter(TypedDict, total=False):
    Shift: int
    Filter: List[str]


class Filters(TypedDict, total=False):
    filters: Filter


class _BaseItem(TypedDict):
    _id: str
    _name: str
    _parent: str
    _proto: str


class StackSlots(_BaseItem, total=False):
    _props: Filters
    _max_count: int


ThrowType = Literal['frag_grenade', 'smoke_grenade', 'flash_grenade']
FragmentType = Literal['5996f6d686f77467977ba6cc', '5996f6fc86f7745e585b4de3']
ammoType = Literal['bullet', 'grenade', 'buckshot']


class BSGProps(TypedDict, total=False):

    # Basic Data
    Name: str
    ShortName: str
    Description: str
    Weight: int
    BackgroundColor: str
    Width: int
    Height: int
    StackMaxSize: int
    Rarity: str
    SpawnChance: int
    CreditsPrice: int
    ItemSound: str
    Prefab: BSGPrefab
    UsePrefab: BSGPrefab
    StackObjectsCount: int
    NotShownInSlot: bool
    ExaminedByDefault: bool
    ExamineTime: int

    IsUndiscardable: bool
    IsUnsaleable: bool
    IsUnbuyable: bool
    IsUngivable: bool
    IsLockedafterEquip: bool

    QuestItem: bool
    LootExperience: int
    ExamineExperience: int
    HideEntrails: bool
    RepairCost: int
    RepairSpeed: int
    ExtraSizeLeft: int
    ExtraSizeRight: int
    ExtraSizeUp: int
    ExtraSizeDown: int
    ExtraSizeForceAdd: bool
    MergesWithChildren: bool
    CanSellOnRagfair: bool
    CanRequireOnRagfair: bool
    ConflictingItems: list
    FixedPrice: bool
    Unlootable: bool
    UnlootableFromSlot: str
    UnlootableFromSide: list
    ChangePriceCoef: int
    AllowSpawnOnLocations: list
    SendToClient: bool
    AnimationVariantsNumber: int
    DiscardingBlock: bool
    RagFairCommissionModifier: int
    IsAlwaysAvailableForInsurance: bool

    StackSlots: StackSlots
    IsAnimated: bool

    # Ammo Data
    ammoType: ammoType
    ammoCaliber: str
    Damage: int
    ammoAccr: int
    ammoRec: int
    ammoDist: int
    buckshotBullets: int

    PenetrationPower: int
    PenetrationPowerDiviation: int

    ammoHear: int
    ammoSfx: str

    MisfireChance: int

    # Grenade Data
    ThrowType: ThrowType
    throwDamMax: int
    Strength: int
    EmitTime: int

    MinExplosionDistance: int
    MaxExplosionDistance: int

    ExplDelay: int
    explDelay: int

    throwDamMax: int

    CanBeHiddenDuringThrow: bool

    # Fragment Data
    FragmentsCount: int
    FragmentType: FragmentType

    ContusionDistance: int

    Blindness: Point3D
    Contusion: Point3D
    ArmorDistanceDistanceDamage: Point3D

    # Weapon Data
    Foldable: bool


class BSGItem(_BaseItem, total=False):
    _type: str
    _props: BSGProps
