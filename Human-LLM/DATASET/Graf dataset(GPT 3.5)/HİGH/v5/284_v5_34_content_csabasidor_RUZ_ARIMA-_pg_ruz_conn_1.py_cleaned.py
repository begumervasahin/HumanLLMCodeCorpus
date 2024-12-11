import pandas.io.sql as psql
import psycopg2 as pg
b1 = {
    "dbname": "datahub",
    "user": "CONTACT SLOVAKIA.DIGITAL",
    "host": "sql.ekosystem.slovensko.digital",
    "port": 5432,
    "password": "CONTACT SLOVENSKO.DIGITAL"
}
b2 = pg.connect(**b1)