from parser.parser import parse
from parser.program_nodes import SASProgram
from pathlib import Path



def main():
    path_str = "./SASPrograms/etl.sas"
    path = Path(path_str)
    sas_program = parse(path=path)


if __name__ == "__main__":
    main()