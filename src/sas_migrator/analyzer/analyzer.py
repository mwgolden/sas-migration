import re

from . import symbol_classes as s
from sas_migrator.parser.program_nodes import SASProgram


def analyze(sas_program: SASProgram) -> s.MigrationDocument:

    doc = s.MigrationDocument()

    for statement in sas_program.statements:
        node_name = statement.__class__.__name__.lower()
        fn = PROGRAM_ANALYZERS.get(node_name)

        if fn:
            fn(statement, doc)
    
    return doc


def visit_libname(node, doc: s.MigrationDocument):
    doc.libraries[node.libref] = {
        "path": node.path,
        "engine": node.engine or "BASE"
    }

def visit_data_step(node, doc: s.MigrationDocument):
    for input in node.inputs:
        source = s.DataSource(
            name=input,
            type="dataset"
        )
        doc.inputs.append(source)

    for output in node.outputs:
        output = s.DataTarget(
            name=output,
            type="dataset"
        )
        doc.targets.append(output)

    for source in doc.inputs:
        for target in doc.targets:
            doc.data_flows.append(
                s.DataFlow(
                    source=source,
                    target=target
                )
            )

    analyze_transformations(node.transformations, doc)

def analyze_transformations(transformations: list[str], doc: s.MigrationDocument):
    for t in transformations:
        if t.startswith("WHERE("):
            expression = t[6:-1]
            doc.filters.append(
                s.Filter(expression=expression)
            )
        elif t.startswith("Assign("):
            expression = t[7:-1]
            doc.assignments.append(
                s.Assignment(expression=expression)
            )


PROGRAM_ANALYZERS = {
    "libname": visit_libname,
    "datastep": visit_data_step
}
