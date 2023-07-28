from typing import Never, NoReturn


def never(_: Never) -> NoReturn:
    raise ValueError("Unreachable code")
