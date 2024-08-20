# app/models.py
from app import db
from datetime import datetime

class CheckingAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

class IncomeSource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    frequency = db.Column(db.String(50), nullable=False)

class SavingsAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    account_type = db.Column(db.String(50), nullable=False)  # 'liquid' or 'investment'

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    expense_type = db.Column(db.String(50), nullable=False)  # 'fixed' or 'variable'
    due_date = db.Column(db.Date)

class CreditCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    promo_end_date = db.Column(db.Date)
    min_payment = db.Column(db.Float, nullable=False)
    payment_made = db.Column(db.Boolean, default=False)
