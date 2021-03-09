from clickhouse_driver import Client
import os

client = Client(host=os.environ['CH_HOST'])
def t(x):
  client.execute('INSERT INTO events (x) VALUES', x)
