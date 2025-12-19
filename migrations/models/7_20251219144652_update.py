from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `app_user` RENAME TO `user`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` RENAME TO `app_user`;"""


MODELS_STATE = (
    "eJztmm1v2kgQx78K8qtEylXggE3uHSTkmiuBKiF3VZvKWuw1WJi1a68bUJXvfrNrFj+7JC"
    "3B6PwGweyMvfubffiPzQ9p6RjY9t/1XHdokYX0Z+OHRNASw5d001lDQq4bNTADRVOb+0KL"
    "ZguvqU89pFOwm8j2MZgM7Oue5VLLIWAlgW0zo6ODo0VmkSkg1rcAa9SZYTrHHjR8+Qpmix"
    "h4hX3x011opoVtI9Fby2D35naNrl1uuyH0mjuyu0013bGDJYmc3TWdO2TrbRHKrDNMsIco"
    "ZpenXsC6z3q3GakYUdjTyCXsYizGwCYKbBob7o4MdIcwftAbnw9wxu7yh9xqq+3uudLugg"
    "vvydaiPofDi8YeBnICo4n0zNsRRaEHxxhx46PPIzcgwZLTu4H+IKLjDEUR+nOOgloZSGGI"
    "SEazR6BsZThKbNY9BqquTh+DjtqdSi+hei6ryhYo+1HG8v62NxwKoBFAMe2TACd4VTD3hH"
    "+KGvRuX9RyJyBbso/BRdvEj4Fyjjq7cSvBMxl8mrCLLH3/m80Mo396d5fve3cnt71Pp7xl"
    "vWkZjkd/CXcHtopwDxldDsf9FFzdwwyGhmgW8RW0UGuJ8zEnI1OwjU3oO/HlTdHvvvZhDM"
    "aY2OvNtlJG/+Z2cD/p3X5MpOCqNxmwFjmBX1hPlNNkBrYXafx7M3nfYD8bn8ejASfo+HTm"
    "8TtGfpPPEusTCqijEedJQ0ZsBxRWASaRWDhBMEOdyWrfcWyMSH5SY1GpjE4hbF9JzD/FJF"
    "g3imzCrtOWFfg0TBk+ZbkJq0pR2r+8nvrj8TCRzP5NesE83PYHdyctnkVwsiiO9nx2UJqL"
    "2JbPDFOkL56QZ2iZFkd2inyzTUt5mbYggmYcHxsnG9VGPTz4/BjPqApuL5UUgfCo5cQRyQ"
    "mWNf49Q+9yjrx8fPGY33MqvpIiLGm1I3dhYcvnKlvYTWNHObFEK83GZEbnDGWnU8JQnIrg"
    "ldp+xYEph23Jk9BFvv/keDnTshhsPObQcgNwTnXYJ9Vus8XQ6oC5g5t6ZQAflRCWfzZ3Dy"
    "iIa81Wa7Zas+1Zs8X2LWeBiZ+TlE3c9Yc7bCMOIJuCmBqbsOtUc009izklrGJt7VO5XvdD"
    "IjniVTSV6ldzqtGtV61hj0jD5iuBYplVcPy/uXa96Kod+FQV2NSUbhNUQBck12sEltLeQV"
    "8p7UJ5xZpS6koshV0fk20DDi1cr5GO4aRaNJCuY99vbDtWvadlrrXCtpa37EtqhFhMZVDz"
    "TjWsV1Vfv3/u1rpnz7qnrh7+B9VD4BqvTGwysk7sQRO71d0VebhcKNITNU35Y+ZaqB+pUD"
    "9aURnXkg04is8v4HBWOl21msKS91ObI3/+orooEXXY6igk7c+R3FFO5nh1Wg1piVeuBTvx"
    "Kw7FZGSlDkVQm11Th/JTUVt8WpugOS865q/rzCodjQJGqejx8HeYeC8tHWJR1SwdlDZqs5"
    "Q2m3XpUCvM/ZcOTKO9SCTFIt7updzhxVJGlycZZgFeOx62ZuQDXmfecBa/Kagmv6KXBGD2"
    "0NNWdcenBgwvfErDdUzv/rJ3NZCeD1PL9LBn6XMp7w+4YctZ6f9vI5+6gqnYojwrqWC+Y8"
    "/fvJnbVVXHQg5cxexOcf//3mBL4wUQN+7HCbDVbO4AELwKAfK2lHhyCMUkRzn9fT8eFaim"
    "KCQF8oHAAL8Ylk7PGrbl06/VxFpCkY26vIxOV8wp2cMu0D/0/zCf/wMixN9/"
)
