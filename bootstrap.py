import os

import rethinkdb as r

r.connect(os.environ.get('RETHINK_HOST', 'localhost'), int(os.environ.get('RETHINK_PORT', 28015))).repl()

if 'khadgar' not in r.db_list().run():
    r.db_create('khadgar').run()

table_list = r.db('khadgar').table_list().run()

if 'url' not in table_list:
    r.db('khadgar').table_create('url').run()

index_list = r.db('khadgar').table('url').index_list().run()

if 'external_id' not in index_list:
    r.db('khadgar').table('url').index_create('external_id').run()
