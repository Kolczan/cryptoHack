__all__ = ["leg", "is_qres"]


def leg(a: int, modp: int) -> int:
    return pow(a, (modp - 1) // 2, modp)


def is_qres(a: int, modp: int) -> bool:
    return leg(a, modp) == 1


def leg_sqrt(x: int, modp: int) -> tuple[int, int]:
    xa = pow(x, (modp + 1) // 4, modp)
    xb = -xa % modp
    return xa, xb
