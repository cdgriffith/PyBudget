#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bottle
from sqlalchemy.orm.exc import NoResultFound

from pybudget.lib.database import (Categories, Transaction,
                                    TransactionDescription,
                                    Accounts, Ledger, Base)


app = bottle.Bottle()


@app.get("/transaction")
def get_transaction(db):
    """ Return all transactions. """
    data = []
    for row in db.query(Transaction).all():
        data.append(dict(row))

    return {"data": data}


@app.post("/transaction/<account>")
def post_transaction(account, db):
    """ Add a new transaction. """

    params = bottle.request.query.decode()

    if "amount" not in params:
        return bottle.abort(422, "Amount must be a GET parameter")

    try:
        db_account = db.query(Accounts).filter(Accounts.id == int(account)).one()
    except NoResultFound:
        return bottle.abort(404, "Account not found")


@app.delete("/transaction/<transaction_id>")
def delete_transaction(transaction_id, db):
    """ Remove a transaction. """

    try:
        db.query(Transaction).filter(Transaction.id == int(transaction_id)).delete()
    except Exception as err: # NoResultFound:
        print(str(err))
        return bottle.abort(500, str(err))
        #return bottle.abort(404, "Account not found")

    return {}

