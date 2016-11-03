import sqlalchemy as sa
import configparser

cfg = configparser.ConfigParser()
cfg.read('settings.cfg')

url = 'mysql+pymysql://{0}:{1}@{2}/infbot_db?charset=utf8'.format(cfg['mysql']['user'], cfg['mysql']['password'], cfg['mysql']['host']) #'mysql+pymysql://phpmyadmin:m@localhost/infbot_db?charset=utf8'
print(url)

engine = sa.create_engine(url, echo=True)

engine.execute('DROP TABLE zoo')
engine.execute('CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)')

# SQL文に「?」が使用できないので、代わりに「%s」を使用
ins = "INSERT INTO zoo (critter, count, damages) VALUES (%s, %s, %s)"
engine.execute(ins, "あひる", 10, 0.0)
engine.execute(ins, "くま", 2, 1000.0)
engine.execute(ins, "いたち", 1, 2000.0)

rows = engine.execute('SELECT * FROM zoo')

for row in rows:
    print(row)
