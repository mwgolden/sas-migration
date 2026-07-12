from dataclasses import dataclass, field
from typing import List, Optional
from pathlib import Path


@dataclass
class Node:
    source: str

@dataclass
class Libname(Node):
    libref: str
    engine: str = "BASE"
    path: Optional[Path]

@dataclass
class DataStep(Node):
    inputs: List[str] = field(default_factory=List)
    outputs: List[str] = field(default_factory=List)
    transformations: List[str] = field(default_factory=List)

@dataclass
class ProcSort(Node):
    inputs: List[str] = field(default_factory=List)
    outputs: List[str] = field(default_factory=List)
    by: List[str] = field(default_factory=List)

@dataclass
class ProcSql(Node):
    tables: List[str] = field(default_factory=List)
    joins: List[str] = field(default_factory=List)
    group_by: List[str] = field(default_factory=List)


@dataclass
class Macro(Node):
    name: str
    parameters: List[str] = field(default_factory=List)


@dataclass
class SASProgram:
    statements: List[Node] = field(default_factory=List)