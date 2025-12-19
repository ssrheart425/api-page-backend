from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `app_link` ADD `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `app_link` DROP COLUMN `created_at`;"""


MODELS_STATE = (
    "eJztmVtv2kgUx78K8lMiZSswxiZ9MwnZsiWwSki3alNZgz0GCzOm9rgBVXz3PTNm8J1Aui"
    "mOlhcE52LP/OZy/jP8lOaehd3gnb5Y9B0yk97XfkoEzTF8ybouahJaLGIHM1A0dnkseAxX"
    "RI0D6iOTgt1GboDBZOHA9J0FdTwCVhK6LjN6JgQ6ZBKbQuJ8D7FBvQmmU+yD4+s3MDvEwk"
    "sciJ+LmWE72LVSrXUs9m5uN+hqwW09Qm94IHvb2DA9N5yTOHixolOPbKMdQpl1ggn2EcXs"
    "8dQPWfNZ6zY9FT2KWhqHRE1M5FjYRqFLE93dk4HpEcYPWhPwDk7YW/6QG4qmtJuq0oYQ3p"
    "KtRVtH3Yv7HiVyAoORtOZ+RFEUwTHG3Hjvi8h1STjn9HrQHkRMnKMoUp/nKKjtAikMMcl4"
    "9giUjRxHic26x1AztfFj2NLaY+kQqk1ZU7dA2Y9dLO9v9X5fAI0BimmfBjjCy5K5J+Iz1K"
    "B1r0WtcAKyJfsYXio2fgzVJmrtx20HnlH384g9ZB4E311mGHzS764+6Hdnt/rnc+5ZbTz9"
    "4eBPEe7BVhHtIYOr/rCTgWv6mMEwEM0jvgYPdea4GHM6MwPb2qS+E19+K/r91z70wRoSd7"
    "XZVnbR791270f67d+pIbjWR13mkVP4hfVMPU+PwPYhtX96ow819rP2ZTjocoJeQCc+f2Mc"
    "N/oisTahkHoG8Z4MZCV2QGEVYFIDCxUEM9S5Ue14nosRKR7URFZmRMeQ9lqDWFzFJFg3qm"
    "zDrqPIKnxatgyfslyHVaWqyi+vp85w2E8NZqeXXTAPt53u3VmDjyIEORTHez4rlPYsseUz"
    "wxiZsyfkW0bO48leWWzeNZfnWQsiaMLxsX6yXm3Uw0PAy3hOVXD7s5IiFFEnSfGGJAUbNf"
    "49R+9qivxifMmc/6YyvpAiLGutJbdhcctNjS3uurWnpJijpeFiMqFThrLV2sFQVEaIymzB"
    "omjKkS9dDRcoCJ48v2BaloNN5hxbcgDOsQl7pdauNxhaEzC3cN2sDOA3JYbl5+buEUXxqb"
    "xXp7wnprc3wyQoGJRN3s3HO+wiDiA/BInCPWLPqaZkXos5JaybjX/92iInYlKidLbAyuUO"
    "K4AG3cadBM8bEjzbYdv3DmCbcOyKjEwTB0GNt6cG+1vzEnY8tdXWqnkdwNtpTFEwPUQCpb"
    "OOqy4j0sEUyS31bIqX5y/RPqqyh/RRlVLlw1xpsHi5cOBw/4J7lnRmpe5ZoIS3bROEkKo1"
    "+LS2oZBftuxfL95Vum0RMHZet/j4B0y8Q/VYIquaekxVkMKGtF4/th47XVr+Dy4tuUY7SC"
    "QlMn7fwfD4Yil3OkkzzAO88XzsTMhHvMqdssuPIdXkV3YCAbOPnraqOzk1oHvR0ZfrGP3+"
    "Sr/uSuvjXNjq2HfMqVT0R3Dkudh5aRvHnE4wFVuUFztOMD+wH2yO/fuq6kTKkU8x+1N8/R"
    "tEtjQOgLgJf5sAG/X6HgAhqhQg92XEk0coJgXK6a/74aBENcUpGZAPBDr41XJMelFznYB+"
    "qybWHRRZr3cfo7Mn5ozsYQ/oHPv/wPW/Z/+XGw=="
)
