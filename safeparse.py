from typing import Optional, Any, Union
from ast import parse, literal_eval, Assign, expr, Name, Tuple

__all__ = ["extract_values"]


def extract_values(file: str) -> Optional[dict]:
    with open(file, "rt") as f:
        pcode = f.read()

    try:
        past = parse(pcode, filename=file)

    except:
        return None

    if past is None:
        return None

    pvars = {}
    for body in past.body:
        if not isinstance(body, Assign):
            continue

        if len(body.targets) != 1:
            continue

        if isinstance(body.targets[0], Name):
            vname = body.targets[0].id

        elif isinstance(body.targets[0], Tuple):
            vname = "_".join(x.id for x in body.targets[0].elts)

        vval = parse_value(body.value)
        pvars[vname] = vval

    return pvars


def parse_value(val: Union[str, expr]) -> Any:
    return literal_eval(val)


def _parse_contents(contents: str, filename: str):
    try:
        past = parse(contents, filename=filename)

    except:
        return None

    if past is None:
        return None

    for body in past.body:
        if not isinstance(body, Assign):
            continue

        if len(body.targets) != 1:
            continue

        if isinstance(body.targets[0], Name):
            vname = body.targets[0].id

        elif isinstance(body.targets[0], Tuple):
            vname = "_".join(x.id for x in body.targets[0].elts)

        vval = parse_value(body.value)
        yield vname, vval


def extract_named_tuples(file: str) -> Optional[list[dict]]:
    with open(file, "rt") as f:
        pcode = f.read()

    current_tuple = {}
    tuples = []
    for name, value in _parse_contents(pcode, file):
        if name in current_tuple:
            tuples.append(current_tuple)
            current_tuple = {}

        current_tuple[name] = value

    tuples.append(current_tuple)
    return tuples



def extract_line(line: str) -> Any:
    sepidx = line.index(":")
    sepidx += 2
    line = line[sepidx:]
    return parse_value(line)


def extract_lines(file: str) -> list[Any]:
    with open(file, "rt") as f:
        return [
            extract_line(line)
            for line
            in f
        ]
