from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `fb_token` ADD `token` LONGTEXT NOT NULL COMMENT 'Facebook access token';
        ALTER TABLE `fb_token` ADD `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `fb_token` ADD `pixel_id` VARCHAR(64) NOT NULL COMMENT 'Facebook pixel id';
        ALTER TABLE `fb_token` DROP COLUMN `fb_token`;
        ALTER TABLE `fb_token` DROP COLUMN `fb_pixel_id`;
        ALTER TABLE `fb_token` MODIFY COLUMN `type` VARCHAR(64) NOT NULL COMMENT '页面标识';
        ALTER TABLE `fb_token` MODIFY COLUMN `type` VARCHAR(64) NOT NULL COMMENT '页面标识';
        ALTER TABLE `fb_token` ADD UNIQUE INDEX `type` (`type`);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `fb_token` DROP INDEX `type`;
        ALTER TABLE `fb_token` ADD `fb_token` VARCHAR(256) NOT NULL COMMENT 'fb_token';
        ALTER TABLE `fb_token` ADD `fb_pixel_id` VARCHAR(256) NOT NULL COMMENT 'fb_token';
        ALTER TABLE `fb_token` DROP COLUMN `token`;
        ALTER TABLE `fb_token` DROP COLUMN `updated_at`;
        ALTER TABLE `fb_token` DROP COLUMN `pixel_id`;
        ALTER TABLE `fb_token` MODIFY COLUMN `type` VARCHAR(256) NOT NULL COMMENT '页面的type';
        ALTER TABLE `fb_token` MODIFY COLUMN `type` VARCHAR(256) NOT NULL COMMENT '页面的type';"""


MODELS_STATE = (
    "eJztmm1v2kgQx78K8qtEylXggE3uHSTkmiuBKiFt1aayFnsNFmbt2uuGqMp3v9k1i58dkp"
    "ZgdH6DYHbG3v3NPvzH5pe0dAxs++96rju0yEL6u/FLImiJ4Uu66aQhIdeNGpiBoqnNfaFF"
    "s4XX1Kce0inYTWT7GEwG9nXPcqnlELCSwLaZ0dHB0SKzyBQQ60eANerMMJ1jDxq+fQezRQ"
    "y8wr746S4008K2keitZbB7c7tGH11uuyL0kjuyu0013bGDJYmc3Uc6d8jG2yKUWWeYYA9R"
    "zC5PvYB1n/VuPVIxorCnkUvYxViMgU0U2DQ23C0Z6A5h/KA3Ph/gjN3lL7nVVtvdU6XdBR"
    "fek41FfQqHF409DOQERhPpibcjikIPjjHixkefR25AgiWndwX9QUTHGYoi9HmOgloZSGGI"
    "SEazR6BsZThKbNbdB6quTu+DjtqdSi+heiqrygYo+1HG8va6NxwKoBFAMe2TACd4VTD3hH"
    "+KGvRuV9RyJyBbsvfBWdvE94FyijrbcSvBMxl8mbCLLH3/h80Mo0+9m/P3vZuj696XY97y"
    "uG4Zjkf/CHcHtopwDxmdD8f9FFzdwwyGhmgW8QW0UGuJ8zEnI1OwjXXoO/HlTdFvv/ZhDM"
    "aY2I/rbaWM/tX14HbSu/6YSMFFbzJgLXICv7AeKcfJDGwu0vh8NXnfYD8bX8ejASfo+HTm"
    "8TtGfpOvEusTCqijEedBQ0ZsBxRWASaRWDhBMEOdyWrfcWyMSH5SY1GpjE4hbFdJzD/FJF"
    "g3imzCrtOWFfg0TBk+ZbkJq0pR2r+9nvrj8TCRzP5VesHcXfcHN0ctnkVwsiiO9nx2UJqL"
    "2JbPDFOkLx6QZ2iZFkd2inyzTUt5mbYggmYcHxsnG9VaPdz5/BjPqApuf1ZSBMKrlhQHJC"
    "lY1vj3DL3zOfLy8cVj/szJ+EqKsKzVjtyFxS2fqmxxN40tJcUSrTQbkxmdM5SdTglDcTKC"
    "V2oLFoemHLYlT0MX+f6D4+VMy2Kw8Zh9Sw7AOdVhr1S7zRZDqwPmDm7qlQF8UGJYfm7u7l"
    "EU17qt1m21btuxbovtW84CEz8nKeu4yw832EYcQDYFMUU2Ydep5pp6EnNKWMXa2qV6veyH"
    "RHIErGgq1bDmVKMbr1rDHpCGzVcCxTKr4Ph/c+161lU78KkqsKkp3SaogC5IrtcILKW9hb"
    "5S2oXyijWl1JVYCts+KtsE7Fu4XiIdw0m1aCBdx77f2HSsek/MXGuFbS1v2ZfUCLGYyqDm"
    "nWpYr6q+/vzcrXXPjnVPXT38D6qHwDVemdhkZJ3YvSZ2o7sr8oC5UKQnappimc4ePtZC/U"
    "CF+sGKyriWbMBRfHoGh7PS6arVFJa8n9oc+fMX1UWJqP1WRyFpf47kjnI0x6vjakhLvHIt"
    "2IlfcSgmIyt1KILa7Jo6lJ+K2uLT2gTNedYxf19nVuloFDBKRY+Hf8LEe2npEIuqZumgtF"
    "GbpbTZrEuHWmHuvnRgGu1FIikW8XYv5fYvljK6PMkwC/DS8bA1Ix/wY+YNZ/GbgmryK3pJ"
    "AGYPPWxUd3xqwPDCpzRcx/Ruz3sXA+lpP7VMD3uWPpfy/oQbtpyU/mEm8qkrmIotypOSCu"
    "Yn9vz1m7ltVXUsZM9VzPYUd//vDbY0XgBx7X6YAFvN5hYAwasQIG9LiSeHUExylNO/t+NR"
    "gWqKQlIg7wgM8Jth6fSkYVs+/V5NrCUU2ajLy+h0xZySPewC/X3/F/PpPyOh4R8="
)
