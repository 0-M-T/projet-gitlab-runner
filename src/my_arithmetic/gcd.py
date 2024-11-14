def gcd(a, b):
    """Calcule le plus grand commun diviseur (PGCD) de deux entiers a et b."""
    while b:
        a, b = b, a % b
    return a
