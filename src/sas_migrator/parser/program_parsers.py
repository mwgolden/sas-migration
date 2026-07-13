import re
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

def parse_data_step(unit: ProgramUnit) -> n.DataStep: 

    data_step = n.DataStep(source=unit.unit)
    
    lines = [
        line.strip() 
        for line in unit.unit.splitlines()
        if line.strip()
    ]

    for line in lines:
        lower = line.lower()
        if lower.startswith("data "):
            m = re.match(r"data\s+([a-zA-z_][\w.]*)", line, re.I)
            if m:
                data_step.outputs.append(m.group(1))
            continue
        if lower.startswith("set "):
            m = re.match(r"set\s+([a-zA-z_][\w.]*)", line, re.I)
            if m:
                data_step.inputs.append(m.group(1))
            continue
        if lower.startswith("where "):
            expression = line[6:].rstrip(";").strip()
            data_step.transformations.append(f"WHERE({expression})")
            continue
        if "=" in line:
            lhs, rhs = line.rstrip(";").split("=", 1)
            lhs = lhs.strip()
            rhs = rhs.strip()
            data_step.transformations.append(f"ASSIGN({lhs} = {rhs})")
            continue

    return data_step


def parse_proc_sql(unit: ProgramUnit): pass

def parse_proc_sort(unit: ProgramUnit): pass