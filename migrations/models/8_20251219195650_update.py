from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `fb_token` DROP INDEX `type`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `fb_token` ADD UNIQUE INDEX `type` (`type`);"""


MODELS_STATE = (
    "eJztmm1v2kgQx78K8qtEylXggE3uHSTkmiuBKiFt1aayFnsNFmbt2usGVOW73+yaxc8uSU"
    "sxOr9BMDtj7/5mH/5j80NaOga2/Tc91x1aZCH93fghEbTE8CXddNaQkOtGDcxA0dTmvtCi"
    "2cJr6lMP6RTsJrJ9DCYD+7pnudRyCFhJYNvM6OjgaJFZZAqI9S3AGnVmmM6xBw1fvoLZIg"
    "ZeYV/8dBeaaWHbSPTWMti9uV2ja5fbbgi95o7sblNNd+xgSSJnd03nDtl6W4Qy6wwT7CGK"
    "2eWpF7Dus95tRipGFPY0cgm7GIsxsIkCm8aGuyMD3SGMH/TG5wOcsbv8Jbfaart7rrS74M"
    "J7srWoz+HworGHgZzAaCI983ZEUejBMUbc+OjzyA1IsOT0bqA/iOg4Q1GE/pyjoFYGUhgi"
    "ktHsEShbGY4Sm3WPgaqr08ego3an0kuonsuqsgXKfpSxvL/tDYcCaARQTPskwAleFcw94Z"
    "+iBr3bF7XcCciW7GNw0TbxY6Cco85u3ErwTAafJuwiS9//ZjPD6EPv7vJt7+7ktvfplLes"
    "Ny3D8egf4e7AVhHuIaPL4bifgqt7mMHQEM0ivoIWai1xPuZkZAq2sQl9I778UfS7r30Ygz"
    "Em9nqzrZTRv7kd3E96t+8TKbjqTQasRU7gF9YT5TSZge1FGh9vJm8b7Gfj83g04AQdn848"
    "fsfIb/JZYn1CAXU04jxpyIjtgMIqwCQSCycIZqgzWe07jo0RyU9qLCqV0SmE7SuJ+aeYBO"
    "tGkU3YddqyAp+GKcOnLDdhVSlK+5fXU388HiaS2b9JL5iH2/7g7qTFswhOFsXRns8OSnMR"
    "2/KZYYr0xRPyDC3T4shOkW+2aSkv0xZE0IzjY+Nko9qohwefH+MZVcHtpZIiEB61nDgiOc"
    "Gyxr9n6F3OkZePLx7ze07FV1KEJa125C4sbPlcZQu7aewoJ5ZopdmYzOicoex0ShiKUxG8"
    "UtuvODDlsC15ErrI958cL2daFoONxxxabgDOqQ77pNptthhaHTB3cFOvDOCjEsLyz+buAQ"
    "VxrdlqzVZrtj1rtti+5Sww8XOSsom7fneHbcQBZFMQU2MTdp1qrqlnMaeEVaytfSrX635I"
    "JEe8iqZS/WpONbr1qjXsEWnYfCVQLLMKjv8DSKyLrtqBT1WBbU3pNkEHdEF0vUZiKe0dFJ"
    "bSLhRYrCmlr8Ri2PVB2Tbg0FyvkY7hrFo0kK5j329sO1a952WutcK2lrfwS6qEWExlUPNO"
    "NaxX1V+/f+7WymfPyqeuH/4H9UPgGq9MbDKyTuxBE7tV3hV5vFwo0xNVTfmD5lqqH6lUP1"
    "pRGdeSDTiKzy/gcFY6XbWawpL3U5sjf/6iyigRddhn+yFpf47kjnIyx6vTakhLvHIt2Ilf"
    "cSgmIyt1KILa7Jo6lJ+K2uLT2gTNedExf11nVuloFDBKRY+Hv8PEe2npEIuqZumgtFGbpb"
    "TZrEuHWmHuv3RgGu1FIikW8edeyx1eLGV0eZJhFuC142FrRt7hdeYdZ/G7gmryK3pNAGYP"
    "PW1Vd3xqwPDCpzRcx/TuL3tXA+n5MLVMD3uWPpfy/oIbtpyV/gM38qkrmIotyrOSCuY79v"
    "zNu7ldVXUs5MBVzO4U9///DbY0XgBx436cAFvN5g4AwasQIG9LiSeHUExylNO/9+NRgWqK"
    "QlIgHwgM8Ith6fSsYVs+/VpNrCUU2ajLy+h0xZySPewC/UP/E/P5P3L/4BU="
)
