from dataclasses import dataclass
from typing import List
from enum import Enum, auto

from pprint import pprint


@dataclass
class ProgramUnit:
    classification: str
    unit: str
    

def is_unit_start(token: str) -> bool:
    unit_start = [
        "data", "proc", "%macro", "libname", "filename", "options", "%let" , "%include" 
    ]

    return token.lower() in unit_start

def classify_unit(line: List[str]) -> str:
    t1, t2  = line[0].lower().rstrip(";"), line[1].lower().rstrip(";")
    if t1 =="proc":
        return f"proc_{t2}"
    else: 
        return t1

def splitter(source_lines: List[str]) -> List[ProgramUnit]:
    # TODO: Need to split macro based on %macro ... %mend
    program_units = []
    classification = "unknown"
    unit = ""
    for line in source_lines:
        tokens = line.split()
        if tokens and is_unit_start(tokens[0]):
            if unit: 
                program_units.append(
                    ProgramUnit(classification=classification, unit=unit)
                )
            classification = classify_unit(tokens)
            unit = ""
        unit += line
    # capture final unit
    if unit:
        program_units.append(
                    ProgramUnit(classification=classification, unit=unit)
                )
        
    return program_units






if __name__ == "__main__":
    with open("./SASPrograms/etl.sas", 'r') as f:
        lines = f.readlines()
        units = splitter(lines)
        pprint(units)