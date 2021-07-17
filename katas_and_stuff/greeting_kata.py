def greet_two(names):
    return " and ".join([names[0], names[1]])


def greet_more_than_two(names):
    return greet_two([", ".join(names[:-1]), names[-1]])


def greet_shouted(name):
    return f"HELLO {name}!"


def is_shouted(name):
    return name.upper() == name


def split_name(name):
    names = []
    for n in name:
        if '"' not in name:
            for splitted in n.split(", "):
                names.append(splitted)
    return names


def greet(name):
    if name is None:
        return "Hello, my friend."
    if isinstance(name, list):
        name = split_name(name)
        if len(name) > 2:
            shouted = [na for na in name if is_shouted(na)]
            not_shouted = [na for na in name if not is_shouted(na)]
            if len(shouted) == 0:
                return f"Hello, {greet_more_than_two(not_shouted)}."
            else:
                return (
                    "Hello, "
                    + greet_two(not_shouted)
                    + ". AND "
                    + greet_shouted(shouted[0])
                )
        else:
            return f"Hello, {greet_two(name)}."

    if name.isnumeric():
        return "Hello, robot."
    if is_shouted(name):
        return greet_shouted(name)

    return f"Hello, {name}."
