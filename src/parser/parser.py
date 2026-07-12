from .splitter import splitter, ProgramUnit
from .program_nodes import SASProgram
from pathlib import Path
import parser.program_parsers as p

from typing import List

PROGRAM_PARSERS = {
    "libname": p.parse_libname,
    "data": p.parse_data_step,
    "proc_sql": p.parse_proc_sql,
    "proc_sort": p.parse_proc_sort
}

def parse_program(program_units: List[ProgramUnit]): 
    sas_program = SASProgram()

    for unit in program_units:
        parser = PROGRAM_PARSERS.get(
            unit.classification,
            lambda x: x
        )

        node = parser(unit.unit)
        sas_program.statements.append(node)

    return sas_program

def parse(path: Path) -> SASProgram:
    with open(path, 'r') as f:
        lines = f.readlines()
        units = splitter(lines)
        sas_program = parse_program(units)
        return sas_program