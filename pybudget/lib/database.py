#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import (Column, Integer, String, Float,
                        Boolean, DateTime, ForeignKey)

Base = declarative_base()


class Categories(Base):

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class TransactionDescription(Base):

    __tablename__ = "transaction_description"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))


class Accounts(Base):

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Transaction(Base):

    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    description = Column(Integer)
    account = Column(Integer, ForeignKey("accounts.id"))
    recurring = Column(Boolean)
    days_to_recur = Column(Integer)
    amount = Column(Float)  # if the amount does not recur, this should be blank


class Ledger(Base):

    __tablename__ = "ledger"

    id = Column(Integer, primary_key=True)
    transaction = Column(Integer)
    date = Column(DateTime, default=func.now())
    account = Column(Integer)
    amount = Column(Float)
