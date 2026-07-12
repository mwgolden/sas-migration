from splitter import ProgramUnit
from program_nodes import SASProgram
import program_parsers as p

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
            parse_unknown = lambda x: x
        )

        node = parser(unit.unit)
        sas_program.statements.append(node)

    return sas_program
