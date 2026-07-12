from .splitter import ProgramUnit
from  . import program_nodes as n 

def parse_libname(unit: ProgramUnit) -> n.Libname: 
    tokens = unit.unit.split()

    libref = tokens[1]
    engine = None
    path = None
    options = {}

    for token in tokens[2:]:
        if "=" in token:
            key, value = token.split("=")
            options[key.lower()] = value
            continue
        if token.startswith(("'", '"')):
            path = token.strip("'\"")
            continue
        if engine is None:
            engine = token.upper()

    return n.Libname(
        source=unit.unit,
        libref=libref,
        engine=engine,
        path=path,
        options=options
    )

def parse_data_step(unit: ProgramUnit): pass

def parse_proc_sql(unit: ProgramUnit): pass

def parse_proc_sort(unit: ProgramUnit): pass