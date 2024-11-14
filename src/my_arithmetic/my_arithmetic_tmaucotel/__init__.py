# SPDX-FileCopyrightText: 2024-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT
def pgcd(a, b):
    """Calcule le plus grand commun diviseur (PGCD) de deux entiers a et b."""
    while b:
        a, b = b, a % b
    return a
