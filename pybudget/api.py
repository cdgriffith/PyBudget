#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bottle

from pybudget.database import (Categories, Transaction,
                               TransactionDescription,
                               Accounts, Ledger, Base)

app = bottle.Bottle()


@app.get("/transaction")
def get_transaction(db):
    """   """
    data = []
    for row in db.query(Transaction).all():
        data.append(dict(row))

    return {"data": data}


@app.post("/transaction")
def post_transaction(db):
    """    """


@app.delete("/transaction")
def delete_transaction(db):
    """     """


