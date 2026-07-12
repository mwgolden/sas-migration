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
    path: Optional[Path] = None

@dataclass
class DataStep(Node):
    inputs: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)
    transformations: List[str] = field(default_factory=list)

@dataclass
class ProcSort(Node):
    inputs: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)
    by: List[str] = field(default_factory=list)

@dataclass
class ProcSql(Node):
    tables: List[str] = field(default_factory=list)
    joins: List[str] = field(default_factory=list)
    group_by: List[str] = field(default_factory=list)


@dataclass
class Macro(Node):
    name: str
    parameters: List[str] = field(default_factory=list)


@dataclass
class SASProgram:
    statements: List[Node] = field(default_factory=list)