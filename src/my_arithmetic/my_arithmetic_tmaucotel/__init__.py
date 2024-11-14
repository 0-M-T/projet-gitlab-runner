# SPDX-FileCopyrightText: 2024-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT
def pgcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
