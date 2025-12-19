from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `landing_page` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `link` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlW9r2zAQxr9K8KsVutF66Vr2Lgv7S5aMLhuFUoxiXRwRWXIleUso+e67k+3acRLTwW"
    "AL7F383HPS3S936CFINQdpX4yY4kIlX1gCI6GWweveQ6BYCvjjkOW0F7Asqw0kODaTPkcW"
    "5ihDt3fOrDMsdhibM2kBJQ42NiJzQitUVS4liTpGI2bWUq7EfQ6R0wm4BRgM3N6hLBSHFd"
    "jqM1tGcwGSb1UuON3t9citM699VO6dN9JtsyjWMk9Vbc7WbqHVo1soR2oCCgxzQMc7k1P5"
    "VF3ZbdVRUWltKUps5HCYs1y6RrtPZBBrRfywGusbTOiW5+F5/7J/9fJV/wotvpJH5XJTtF"
    "f3XiR6AuNpsPFx5ljh8BhrbrL8f7fJTWF1AF3lb8HDktvwKlRd9CqhxlePzJ/h1wFn+vZm"
    "SkWn1t5LEsbfB9fDD4PrZ58HNyc+si4jo8n4fWXXONzF5I+Ho8kb5EtDOV828JIwY/HyJz"
    "M82onoUB/y7obSMG0rTOGm8bJj6q/c2gEYES/27XMZ6VxjVnv+L/ARLfAPMJZK2oE3XDCz"
    "n14j5VjWGKd+FUlQiaMBDy8uOphVW4yuk9bClqGwiBHYGiStxm9ALO3HCfD87OwJANF1EK"
    "CPbQPEGx0UO7gN8dPXyXg/xEZKC+Q3hQ3echG7054U1t39m1g7KFLX3c9L+yUhCtq6xPhT"
    "/AF//XnZ/AJWJEGC"
)
