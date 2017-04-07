#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:10:08 2017

@author: root
"""

from sqlalchemy import Column, Integer, UnicodeText, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import collate
from sqlalchemy import desc, asc



engine = create_engine('sqlite:///db.sqlite', echo=True)
Base = declarative_base(bind=engine)


class AccessLog(Base):
    __tablename__ = 'access_log'

    
    date_time    = Column(UnicodeText, primary_key=True)
    user_id      = Column(UnicodeText)
    action       = Column(UnicodeText)
    value        = Column(UnicodeText)

    def __repr__(self):
        return "AccessLog datetime=%s userid=%s, %s, %s'" % (
                self.date_time, self.user_id, self.action, self.value)
        

class AccountCompany(Base):
    __tablename__ = 'account_company'

    
    account_id   = Column(UnicodeText, primary_key=True)
    effective_dt = Column(UnicodeText)
    iban         = Column(UnicodeText)
    status       = Column(UnicodeText)

    def __repr__(self):
        return "AccountCompany %s %s %s %s" % (
                self.account_id, self.effective_dt,
                self.iban, self.status
                )
        
class AccountExternal(Base):
    __tablename__ = 'account_external'

    
    account_id   = Column(UnicodeText, primary_key=True)
    vendor_id    = Column(UnicodeText)
    effective_dt = Column(UnicodeText)
    iban         = Column(UnicodeText)
    status       = Column(UnicodeText)

    def __repr__(self):
        return "AccountCompany %s %s %s %s %s" % (
                self.account_id, self.vendor_id, self.effective_dt,
                self.iban, self.status
                )

class AuthorisationLevel(Base):
    __tablename__ = 'authorisation_level'

    
    group_id     = Column(UnicodeText, primary_key=True)
    group_desc   = Column(UnicodeText)
    approval_max_amount = Column(UnicodeText)

    def __repr__(self):
        return "AccountCompany %s %s %s" % (
                self.group_id, self.group_desc, self.approval_max_amount
                )







class InvoicePurchaseOrder(Base):
    __tablename__ = 'invoice_purchase_order'

    
    invoice_id   = Column(UnicodeText, primary_key=True)
    po_id        = Column(UnicodeText)
    vendor_id    = Column(UnicodeText)
    invoice_dt   = Column(UnicodeText)
    invoice_image_path = Column(UnicodeText)
    payment_due_by_dt = Column(UnicodeText)
    received_dt = Column(UnicodeText)
    received_by_user_id = Column(UnicodeText)
    total = Column(UnicodeText)

    def __repr__(self):
        return "InvoicePurchaseOrder %s %s %s %s" % (
                self.invoice_id, self.po_id, self.vendor_id,
                self.total
                )


class InvoiceTransactions(Base):
    __tablename__ = 'invoice_transactions'

    
    invoice_id     = Column(UnicodeText, primary_key=True)
    transaction_id = Column(UnicodeText)

    def __repr__(self):
        return "InvoiceTransactions %s %s" % (
                self.invoice_id, self.transaction_id
                )








Base.metadata.create_all()

Session = sessionmaker(bind=engine)
sess = Session()
