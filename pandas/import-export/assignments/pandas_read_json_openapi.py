"""
* Assignment: Pandas Read JSON OpenAPI
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define `resp` with result of `requests.get()` for `DATA`
    3. Define `data` with conversion of `resp` from JSON to Python dict by calling `.json()` on `resp`
    5. Define `result: pd.DataFrame` from value for key `paths` in `data` dict

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `resp` z resultatem `requests.get()` dla `DATA`
    3. Zdefiniuj `data` z przekształceniem `resp` z JSON do Python dict wywołując `.json()` na `resp`
    4. Zdefiniuj `result: pd.DataFrame` dla wartości z klucza `paths` w słowniku `data`

Hints:
    * `pd.DataFrame(data)`

Tests:
    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> list(result.index)
    ['put', 'post', 'get', 'delete']
    >>> list(result.columns)  # doctest: +NORMALIZE_WHITESPACE
    ['/pet', '/pet/findByStatus', '/pet/findByTags', '/pet/{petId}', '/pet/{petId}/uploadImage',
     '/store/inventory', '/store/order', '/store/order/{orderId}',
     '/user', '/user/createWithList', '/user/login', '/user/logout', '/user/{username}']
"""


# Given
import pandas as pd
import requests

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/openapi.json'


resp = ...
data = ...
result = ...

# Solution
resp = requests.get(DATA)
data = resp.json()['paths']
result = pd.DataFrame(data)
