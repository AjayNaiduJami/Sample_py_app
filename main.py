import argparse

import sqlalchemy as sa

from pyhocon import ConfigFactory
from bottle import route, run

from utils import as_dict

arg_parser = argparse.ArgumentParser(description="Test service")
arg_parser.add_argument("--config", dest="conf_path", default="example.conf")
args = arg_parser.parse_args()
conf = ConfigFactory.parse_file(args.conf_path)


@route('/list')
def list_values():
    pg = sa.create_engine(
        "postgresql+psycopg2://%s:%s@%s:%s/%s" % (
            conf["postgres"]["user"],
            conf["postgres"]["pwd"],
            conf["postgres"]["host"],
            conf["postgres"]["port"],
            conf["postgres"]["db"]
        )
    )

    return as_dict(pg.execute("SELECT id, value FROM {table}".format(table=conf["postgres"]["table"])))

run(host=conf["main"]["bind_host"], port=conf["main"]["bind_port"])