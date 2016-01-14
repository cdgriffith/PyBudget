#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String, Float, Boolean, DateTime)
from sqlalchemy.sql import func


Base = declarative_base()


class Categories(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)


class TransactionDescription(Base):
    id = Column(Integer, primary_key=True)
    description = Column(String)
    category_id = Column(Integer)


class Accounts(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Transaction(Base):
    id = Column(Integer, primary_key=True)
    description = Column(Integer)
    account = Column(Integer)
    recurring = Column(Boolean)
    days_to_recur = Column(Integer)
    amount = Column(Float)  # if the amount does not recur, this should be blank


class Ledger(Base):
    id = Column(Integer, primary_key=True)
    transaction = Column(Integer)
    date = Column(DateTime, default=func.now())
    account = Column(Integer)
    amount = Column(Float)