"""
* Assignment name: Type Int Add
* Suggested filename: type_int_add.py
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min

English:
    1. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    2. Zero Celsius degrees is equal to 273.15 Kelvins
    3. For calculation use round number 273 (0°K = -273K)
    4. How many Kelvins has average temperatures at surface [MSLREMS]_:
        a. Mars highest: 20 °C
        b. Mars lowest: -153 °C
        c. Mars average: −63 °C
    5. Compare result with "Tests" section (see below)

Polish:
    1. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    2. Zero stopni Celsiusza to 273.15 Kelwiny
    3. W zadaniu przyjmij równe 273°C (0°K = -273K)
    4. Ile Kelwinów wynoszą średnie temperatury powierzchni [MSLREMS]_:
        a. Mars najwyższa: 20 °C
        b. Mars najniższa: -153 °C
        c. Mars średnia: −63 °C
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> mars_max
    293
    >>> mars_min
    120
    >>> mars_avg
    210
"""

# Given
K = 273

# Solution
mars_max = 20 + K
mars_min = -153 + K
mars_avg = -63 + K
