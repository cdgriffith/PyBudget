#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
import os
import datetime

import bottle
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine


from pybudget.api import app as api_app
from pybudget.lib.database import Base

logger = logging.getLogger('PyBudget')

root = os.path.abspath(os.path.dirname(__file__))
bottle.TEMPLATE_PATH.append(os.path.join(root, "templates"))

app = bottle.Bottle()


@app.hook('after_request')
def log_after_request():
    logger.info('{ip} - - [{time}] "{method} {uri} {protocol}" {status}'.format(
        ip=bottle.request.environ.get('REMOTE_ADDR'),
        time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        method=bottle.request.environ.get('REQUEST_METHOD'),
        uri=bottle.request.environ.get('REQUEST_URI'),
        protocol=bottle.request.environ.get('SERVER_PROTOCOL'),
        status=bottle.response.status_code
    ))


def get_user_arguments():
    import argparse

    parser = argparse.ArgumentParser(description="PyFoto Server")
    parser.add_argument("-i", "--ip", default="localhost")
    parser.add_argument("-p", "--port", default=8080, type=int)
    parser.add_argument("-c", "--connect-string", default="sqlite:///pyfoto.sqlite")
    parser.add_argument("--debug", default=False, action="store_true")
    parser.add_argument("-q", "--quiet", default=False, action="store_true")

    args = parser.parse_args()

    if args.debug and args.quiet:
        parser.print_help()
        raise Exception("Really? How can you be quiet and write debug?"
                        "Try just one of those options at a time.")

    return args


def main():
    args = get_user_arguments()

    if args.quiet:
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.DEBUG if args.debug else logging.INFO)

    engine = create_engine(args.connect_string, echo=False)

    plugin = sqlalchemy.Plugin(
        engine,
        Base.metadata,
        keyword='db',
        create=True,
        commit=True,
        use_kwargs=False
    )

    app.install(plugin)
    app.mount("/api", api_app)

    bottle.run(app, host=args.ip, port=args.port, server="cherrypy")


if __name__ == '__main__':
    main()

