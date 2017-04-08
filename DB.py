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
from sqlalchemy import func
from sqlalchemy import ForeignKey


from sqlalchemy.ext.automap import automap_base



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

class AuthorizationLevel(Base):
    __tablename__ = 'authorization_level'

    
    group_id     = Column(UnicodeText, primary_key=True)
    group_desc   = Column(UnicodeText)
    approval_max_amount = Column(UnicodeText)

    def __repr__(self):
        return "AuthorisationLevel %s %s %s" % (
                self.group_id, self.group_desc, self.approval_max_amount
                )


class BankTransferFile(Base):
    __tablename__ = 'bank_transfer_file'

    
    bnk_trn_ref  = Column(UnicodeText, primary_key=True)
    exec_dt      = Column(UnicodeText)
    debit_account_no = Column(UnicodeText)
    credit_account_no = Column(UnicodeText)
    amount = Column(UnicodeText)
    trn_desc = Column(UnicodeText)

    def __repr__(self):
        return "BankTransferFile %s %s %s" % (
                self.bnk_trn_ref,
                self.exec_dt,
                self.debit_account,
                self.credit_account_no,
                self.amount,
                self.trn_desc
                )


class Calendar(Base):
    __tablename__ = 'calendar'


    CalendarDate      = Column(UnicodeText, primary_key=True)
    Wday              = Column(UnicodeText)
    MonthLastBusinessDay      = Column(UnicodeText)
    MonthFirstBusinessday      = Column(UnicodeText) 
    WeekEndDay      = Column(UnicodeText) 
    PublicHolidays      = Column(UnicodeText) 
    PaymentDate      = Column(UnicodeText)

    def __repr__(self):
        return "Calendar %s" % (
                self.CalendarDate, self.Wday
               )

class Department(Base):
    __tablename__ = 'department'


    departement_id   = Column(UnicodeText, primary_key=True)
    departement_desc = Column(UnicodeText)

    def __repr__(self):
        return "Department %s %s" % (
                self.departement_id, self.departement_desc
               )


class Employee(Base):
    __tablename__ = 'employee'


    employee_id   = Column(UnicodeText, primary_key=True)
    birth_date    = Column(UnicodeText)
    first_name    = Column(UnicodeText)
    last_name     = Column(UnicodeText)
    gender        = Column(UnicodeText)
    hire_date     = Column(UnicodeText)
    leaving_date  = Column(UnicodeText)

    def __repr__(self):
        return "Emplyee %s %s %s" % (
                self.employee_id, self.last_name, self.first_name
               )


class EmployeeDepartement(Base):
    __tablename__ = 'employee_departement'


    employee_id    = Column(UnicodeText, primary_key=True)
    departement_id = Column(UnicodeText)

    def __repr__(self):
        return "EmplyeeDepartement %s %s" % (
                self.employee_id, self.departement_id
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
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (
                self.invoice_id, self.po_id, self.vendor_id,
                self.invoice_dt, self.invoice_image_path, self.payment_due_by_dt,
                self.received_dt, self.received_by_user_id, self.total
                )


class InvoiceTransactions(Base):
    __tablename__ = 'invoice_transactions'

    
    invoice_id     = Column(UnicodeText, primary_key=True)
    transaction_id = Column(UnicodeText)

    def __repr__(self):
        return "InvoiceTransactions %s %s" % (
                self.invoice_id, self.transaction_id
                )



class SystemUsers(Base):
    __tablename__ = 'system_users'


    user_id = Column(UnicodeText, primary_key=True)
    password_hash = Column(UnicodeText)
    email = Column(UnicodeText)
    employee_id = Column(UnicodeText)
    created_on = Column(UnicodeText)


class Transactions(Base):
    __tablename__ = 'transactions'


    transaction_id = Column(UnicodeText, primary_key=True)
    transaction_ref = Column(UnicodeText)
    transaction_dt = Column(UnicodeText)
    amount = Column(UnicodeText)
    debit_acct = Column(UnicodeText)
    credit_acct = Column(UnicodeText)
    status = Column(UnicodeText)
    narrative = Column(UnicodeText)
    approval_dt = Column(UnicodeText)
    approved_by_user_id = Column(UnicodeText)

    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (
        self.transaction_id, self.transaction_ref, self.transaction_dt,self.amount,
        self.debit_acct,self.credit_acct,self.status,self.narrative,self.approval_dt,
        self.approved_by_user_id
        )    


class Vendor(Base):
    __tablename__ = 'vendor'

    vendor_id = Column(UnicodeText, primary_key=True)
    vendor_name = Column(UnicodeText)
    vendor_status = Column(UnicodeText)
    vendor_persistence = Column(UnicodeText)
    vendor_type = Column(UnicodeText)
    created_on = Column(UnicodeText)
    created_by = Column(UnicodeText)
    status_last_updated_on = Column(UnicodeText)


class VendorAddress(Base):
    __tablename__ = 'vendor_address'

    vendor_address = Column(UnicodeText, primary_key=True)
    vendor_id = Column(UnicodeText, ForeignKey("vendor.vendor_id"))
    vendor_name = Column(UnicodeText)
    address_no = Column(UnicodeText)
    effective_dt = Column(UnicodeText)
    address_01 = Column(UnicodeText)
    city = Column(UnicodeText)
    postal = Column(UnicodeText)
    country = Column(UnicodeText)


Base.metadata.create_all()

Session = sessionmaker(bind=engine)
sess = Session()
