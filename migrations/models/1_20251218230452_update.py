from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `app_link` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `type` SMALLINT NOT NULL COMMENT 'link类型' DEFAULT 1,
    `link` LONGTEXT NOT NULL COMMENT 'app链接',
    `deleted` BOOL NOT NULL COMMENT '是否已删除' DEFAULT 0
) CHARACTER SET utf8mb4;
        DROP TABLE IF EXISTS `landing_page`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `app_link`;"""


MODELS_STATE = (
    "eJztlWFP2zAQhv8KyieQ2NSmbcr2rUVs61RaCcqERFHkJE5q1bFD4mwg1P++O6cmbRqyog"
    "kxpH2Jmvde23dPnbtHK5YB5dnHQZKMmVhanw8eLUFiCj+qoeMDiyRJGUBBEY9rL0Rcblxe"
    "plLiK9BDwjMKUkAzP2WJYlKAKnLOUZQ+GJmISikX7C6nrpIRVQuaQuDmFmQmAnpPM/OaLN"
    "2QUR5sZcsCPFvrrnpItDYS6os24mme60uex6I0Jw9qIcWTmwmFakQFTYmiuL1Kc0wfs1tX"
    "aioqMi0tRYobawIakpyrjXL3ZOBLgfwgm0wXGOEpH+x2t9896TjdE7DoTJ6U/qoor6y9WK"
    "gJTGbWSseJIoVDYyy56erryJ2JPNb0RpAPET7doWiW/pmjodYE0gglyfL2GJTtHY4W3rp5"
    "3vf73jzv9U886yVUO3bfeQKKL00sL88H47EBWgI0134b4IzeP3P3jL9CDbJ7LWq1FxA/2X"
    "n+qRvSee50SG8/bg14ZmfXM9wkzrI7jsLkx+Di9Nvg4vB8cH2kIw/ryHg6+WrsElpF0UMm"
    "p+PpsAIXGg1FGDt8h1JySkQ94o1VFcoeLHstzPXNzgK8jh3C5ezaDjyD0IanbbcAvuN0/x"
    "r7cDodb2Efjqpcr86HZxeHbf0fgIkpWrYG7KfhcqMzoOARf/mLpIG7E5G2fM67G4rtuKoQ"
    "QSKND+vEqsyQoSnzF7Xjp4g0T5/S83/2vKPZ85OmGaa0A+90QdJ6ehtL3riB7k8xJvcupy"
    "JSeMHtXq+BmWmZ4DqqfMXrkF3EttskfhovgLi2v0+A7VZrD4Dgehagjm0DhBMVLb7BbYjf"
    "L6eTeogbSyogrwQUeBMwXx0fcJap238TawNFrLp5llfHNlKQmYpSvYveYPjW42X1G9SaFT"
    "M="
)
