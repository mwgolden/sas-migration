from dataclasses import dataclass, field
from typing import List

@dataclass
class DataSource:
    name: str
    type: str

@dataclass
class DataTarget:
    name: str
    type: str

@dataclass
class Filter:
    expression: str

@dataclass
class Assignment:
    target: str
    expression: str

@dataclass
class DataFlow:
    source: DataSource
    target: DataTarget

@dataclass
class MigrationDocument:
    inputs: List[DataSource] = field(default_factory=list)
    targets: List[DataTarget] = field(default_factory=list)
    data_flows: List[DataFlow] = field(default_factory=list)
    filters: List[Filter] = field(default_factory=list)
    assignments: List[Assignment] = field(default_factory=list)
    libraries: dict = field(default_factory=dict)