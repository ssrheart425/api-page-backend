from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `fb_token` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `type` VARCHAR(256) NOT NULL COMMENT '页面的type',
    `fb_token` VARCHAR(256) NOT NULL COMMENT 'fb_token',
    `fb_pixel_id` VARCHAR(256) NOT NULL COMMENT 'fb_token',
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `deleted` BOOL NOT NULL COMMENT '是否已删除' DEFAULT 0
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `fb_token`;"""


MODELS_STATE = (
    "eJztml1z2jgUhv8K46tkJtsBx9hk7yAh22wJdBKy22nT8QhbBk+M7NpyA9PJf98jGeFvB9"
    "JNcXZ9w8D5sKVHOtIrmx/S0jWxE7zre97IJg/S760fEkFLDF+yrpOWhDwvdjADRTOHx4JH"
    "d0TULKA+MijYLeQEGEwmDgzf9qjtErCS0HGY0TUg0Cbz2BQS+1uIderOMV1gHxxfvoLZJi"
    "Ze4UD89B50y8aOmWqtbbJ7c7tO1x63XRF6yQPZ3Wa64TrhksTB3pouXLKNtgll1jkm2EcU"
    "s8tTP2TNZ63b9FT0KGppHBI1MZFjYguFDk10d0cGhksYP2hNwDs4Z3f5Te4omtI7VZUehP"
    "CWbC3aU9S9uO9RIicwnkpP3I8oiiI4xpgb730RuSEJl5zeFbQHEQPnKIrU5zkKalUghSEm"
    "Gc8egbKT4yixWXcfaoY2uw+7Wm8m7UP1VNbULVD2o4rl7XV/NBJAY4Bi2qcBTvGqZO6J+A"
    "w1aN1rUSucgKxk78MzxcL3oXqKurtxq8AzHX6asossg+Cbwwzjv/o35+/7N0fX/U/H3LPe"
    "eEaT8R8i3IWlIlpDxuejySAD1/Axg6Ejmkd8AR5qL3Ex5nRmBra5SX0nvvxS9LvXPvTBnB"
    "BnvVlWquhfXQ9vp/3rj6khuOhPh8wjp/AL65F6nB6B7UVaf19N37fYz9bnyXjICboBnfv8"
    "jnHc9LPE2oRC6urEfdSRmVgBhVWASQ0s7CCYoc6N6sB1HYxI8aAmsjIjOoO01xrE4l1Mgr"
    "pRZQtWHUVW4dO0ZPiU5TZUlaoqP11Pg8lklBrMwVW2YO6uB8Obow4fRQiyKY7XfLZRWg+J"
    "JZ8ZZsh4eES+qec8ruyWxeZdS3mZtSCC5hwf6yfr1UY93AV8G8+pCm5/VlKEIqqRFG9IUr"
    "BR499z9M4XyC/Gl8z5d3bGF1KEsta6cg+KWz7VWHG3zR0lxRKtdAeTOV0wlN1uBUOxM0JU"
    "ZgkWm6Yc+dK7oYeC4NH1C6ZlOdhkzqElB+CcGbBWar12h6E1AHMXt43aAH5TYlh+bu4eUB"
    "Q3uq3RbY1ue2Xdlli33AdMgoJB2eRdfrjBDuIA8kOQUGRTdp161tSTmFPCKmrrNdXr5SAi"
    "UiBghatSw1oznW6jGg37hjRssRIol1kl2/8BJNZZT+vCp6bCsgYbuSJatr/AUncSWNnNKC"
    "mw1KzAShbErmiTOYfGm2xLXYB69go7elGhVzJNpjVYG/3a6NdGv0r/qeeOpdotJXXL1Rt7"
    "JtXotzeq34pVRvlrudpIDGQYOAhavD0tqOzTM6h1tdvT6vmGjrdTX6BgsZdcTmUd9oFvRD"
    "pYINABRwu8On6JClGVHUSIqpRqEOZKg8Urz4Z97wUSJJ1ZKwkCm1fPMjSY0FqHT2sLtrCz"
    "rvXz21adhIiAUalEfPwdJt6+SiSRVU8loipIYUPabh9aiTR6/n+g57lG20skJTJ+3buaw4"
    "ulnC5PM8wDvHR9bM/JB7zOvfgqf4BcT35lz47B7KPHrepOTg3oXnTo4zqmf3vevxhKT4c5"
    "y/SxbxsLqei/mZHnpPJ/FHFMc4KpWVGeVJxgvmM/2Lyw2VVVJ1IOfIrZneLrv9RnpbEHxE"
    "342wTYabd3AAhRpQC5LyOeXEIxKVBOf95OxiWqKU7JgLwj0MEvpm3Qk5ZjB/RrPbFWUGS9"
    "rj5GZ0/MGdnDLjA49KOyp38AcsxEqg=="
)
