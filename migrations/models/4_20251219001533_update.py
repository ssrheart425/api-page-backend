from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `app_user` ADD `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `app_user` DROP COLUMN `created_at`;"""


MODELS_STATE = (
    "eJztmVtv2kgUx78K8lMiZSswxiZ9MwnZsuWySki3alNZgz0GCzOm9rgBVXz3PTNm8J1Auh"
    "Si5QXZ52LP/Ob2P+anNPMs7Abv9Pm865Cp9L7yUyJohuEi67qqSGg+jx3MQNHI5bHgMVwR"
    "NQqoj0wKdhu5AQaThQPTd+bU8QhYSei6zOiZEOiQcWwKifM9xAb1xphOsA+Or9/A7BALL3"
    "AgbudTw3awa6Va61js3dxu0OWc2zqE3vFA9raRYXpuOCNx8HxJJx7ZRDuEMusYE+wjitnj"
    "qR+y5rPWrXsqehS1NA6JmpjIsbCNQpcmursjA9MjjB+0JuAdHLO3/CHXFE1p1lWlCSG8JR"
    "uLtoq6F/c9SuQE+kNpxf2IoiiCY4y58d4XkWuTcMbpdaA9iJg4R1GkvsxRUNsGUhhikvHs"
    "EShrOY4Sm3VPoWZqo6ewoTVH0j5U67KmboCym20sH3p6tyuAxgDFtE8DHOJFydwT8Rlq0L"
    "pDUSucgGzJPoXXio2fQrWOGrtx24Jn2P48ZA+ZBcF3lxn6n/T7mw/6/UVP/3zJPcu1pzvo"
    "/ynCPdgqoj2kf9MdtDJwTR8zGAaiecS34KHODBdjTmdmYFvr1Hfi4rei333tQx+sAXGX62"
    "1lG/1Or/0w1Ht/p4bgVh+2mUdO4RfWC/UyPQKbh1T+6Qw/VNht5cug3+YEvYCOff7GOG74"
    "RWJtQiH1DOI9G8hK7IDCKsCkBhZOEMxQ50a15XkuRqR4UBNZmREdQdqhBrH4FJNg3aiyDb"
    "uOIqvwa9ky/MpyFVaVqiq/vJ5ag0E3NZitTnbBPPZa7fuLGh9FCHIojvd8dlDa08SWzwwj"
    "ZE6fkW8ZOY8ne2WxeddMnmUtiKAxx8f6yXq1Vg+PAT/Gc6qC21+UFKGIOkuKNyQp2Kjx6x"
    "y9mwnyi/Elc/6bk/GVFGFZaw25CYtbrmtscVetHSXFDC0MF5MxnTCUjcYWhuJkhKjMFiwO"
    "TTnypU/DOQqCZ88vmJblYJM5x5YcgHNkwl6pNas1htYEzA1cNU8G8JsSw/JLc/eIovis28"
    "667azbDqzbEvuWN8UkKBiUdd7dx3vsIg4gPwQJRTZkzznNNbUSc0pYxdo6tHqNmJRI2A2w"
    "ch3LlI1BN3FnJfuGlOxm2Hb9uLNJOLbUQqaJg6DC21OB/a1+DTue2mhqp/mdh7fTmKBgso"
    "+2TWcdt2yISAcTJDfUiwleXL5G1KrKDppWVUolLXOlweLF3IHT/xVCLJ15UkIMjvCmbYLC"
    "VbUan9Y2HOTXDfvXD+9TkmMCxlY95uMfMPH21WOJrNPUY6qCFDak1eqx9di5qvkfVDVco+"
    "0lkhIZv6/iP75YylUnaYZ5gHeej50x+YiXuc8n5WXIafIrq0DA7KPnjepOTg3oXlT6ch2j"
    "P9zot21pdZwv8Tr2HXMiFf3DH3mutn6Nj2POFcyJLcqrLRXMD+wH67J/V1WdSDlyFbM7xc"
    "N/GmZLYw+I6/C3CbBWre4AEKJKAXJfRjx5hGJSoJz+ehj0S1RTnJIB+Uigg18tx6RXFdcJ"
    "6LfTxLqFIuv19jI6WzFnZA97QOvYf/Su/gUZ6i57"
)
