from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `app_user` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(255) NOT NULL UNIQUE COMMENT '用户名',
    `password` VARCHAR(255) NOT NULL COMMENT '密码哈希',
    `type` SMALLINT NOT NULL COMMENT '用户类型' DEFAULT 2,
    `deleted` BOOL NOT NULL COMMENT '是否已删除' DEFAULT 0
) CHARACTER SET utf8mb4;
        CREATE TABLE IF NOT EXISTS `user_token` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `token` LONGTEXT NOT NULL COMMENT 'access token 原文',
    `token_hash` VARCHAR(64) NOT NULL UNIQUE COMMENT 'token sha256(hex)',
    `expires_at` DATETIME(6) NOT NULL COMMENT '过期时间',
    `revoked` BOOL NOT NULL COMMENT '是否已撤销' DEFAULT 0,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_user_tok_app_user_1ae66a6b` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `app_user`;
        DROP TABLE IF EXISTS `user_token`;"""


MODELS_STATE = (
    "eJztmVtv4jgUgP8KylMrdUcQQkL3LbR0hx0KozbdHc10FJnEgYjgMLEzBY3472s7MbnT0N"
    "kWkPqC4FyC/fn4XOCXtPBt6OEP+nI5dNFc+rPxS0JgAembvOqiIYHlMlEwAQETj9tSjekJ"
    "qwkmAbAIlTvAw5CKbIitwF0S10dUikLPY0LfooYumiaiELk/QmgSfwrJDAZU8e07FbvIhi"
    "uIxcfl3HRc6NmZ1bo2+24uN8l6yWUDRG64Ifu2iWn5XrhAifFyTWY+2lq7iDDpFCIYAALZ"
    "40kQsuWz1cU7FTuKVpqYREtM+djQAaFHUtutycDyEeNHV4P5BqfsW/6QW4qmdNuq0qUmfC"
    "VbibaJtpfsPXLkBEaGtOF6QEBkwTEm3Pjuy8j1Ubjg9AZ0PQBZsEBRuD7PUVDbBVIIEpJJ"
    "9AiUrQJHiUXdY6hZ2uQx7GjdibQP1basqVug7MMulve3+nAogCYARdhnARpwVRF7wj5Hja"
    "7utaiVBiC7so/hpeLAx1Btg049bjvwGP0vBnvIAuMfHhOM/tHvrj7qd2e3+pdzrlnHmuF4"
    "9Jcw92mqiHLI6Go47uXg0kQDGYwC357vexCgcsQprxzlCXV7LczlyU6ieFXZocGpyCp9tR"
    "2Zvspyk8JXVeW3sffG42EGe2+Q5/pw2+vfnbX4GVAjl8AkNbB86sxTmYEJJsCaP4HANgsa"
    "X/arbIuqhbzISwACU46P7ZPtKi4yD5hn+0Lx4fJnK08orN4rzwlVHnZq/H2B3tUMBOX40j"
    "7/TwJ9IUV6rbWO3KWXW25r7HI37ZqVZwFWpgfRlMwYyk5nB0ORQKnVee5Oxyo50mWT5hJg"
    "/OQHJWFZDTbtc+jKRHFOLJortW6zxdBaFHMHNq2jAXxSPZP8XOwesHd6L+/HU95T4e3PIc"
    "IlhxL73Xy6gx7gAIpHkCrcBnvOm6aO2rVtI2JKSOPEv3ntJidiUtHpbIFVtzusAJpka/fe"
    "8JxQw7M9trqj4tbh0BUZWBbEuMHX06D5rX1JM57a6WrHOTXydZozgGf7tEBZr8N2lxFpPA"
    "NyRz2bwdX5S3ofVanR+qhKZefDVFmwcLV0A4hNQIpgrykW4i5gOdysZw6uHbt+EG/eut/s"
    "OhZthFStxcPaoYX8suP8fvE2Brf9e0O//ZyJ8Gvd6DONnIluIT1Tc+exfUjj34HxscE+Nr"
    "6OR33O0cdkGvBvTOyMrxJbEwiJbyL/yQR2GoYQC1HmfAP4kwbevv1Yyus4+zFVAQo70mbz"
    "0P1YGrYVQIbkBZcp63lUl6l+saV7sMfIW4vO6zSuUZy/d94i3qPt1SSlPN5uMDx8s1SYTr"
    "IMiwBv/AC6U/QJrgtTdvUYcpz8qiYQKg7A07brTocG3V40+vI+Rr+/0q/70uYwP9jqMHCt"
    "mVT2f2Gkudj5o21i8z7BHNmlvNgxwfyEAY7H/rpddcrlwFNMfYqv/wsiuxp7QIzNTxNgq9"
    "msAZBaVQLkulzz5CMCUUnn9Pf9eFTRNSUuOZAPiG7wm+1a5KLhuZh8P06sOyiyXe8eo/MT"
    "c67tYQ/oHfr/wM1/o2L/uw=="
)
