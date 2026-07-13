from sas_migrator.parser.parser import parse
from sas_migrator.parser.program_nodes import SASProgram
from sas_migrator.analyzer.analyzer import analyze
from pathlib import Path
from pprint import pprint



def main():
    path_str = "./SASPrograms/texas_customers.sas"
    path = Path(path_str)
    sas_program = parse(path=path)
    migration = analyze(sas_program=sas_program)

    pprint(migration)


if __name__ == "__main__":
    main()