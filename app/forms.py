# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CheckingAccountForm(FlaskForm):
    name = StringField('Account Name', validators=[DataRequired()])
    balance = FloatField('Balance', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Account')

class IncomeSourceForm(FlaskForm):
    name = StringField('Income Source', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    frequency = SelectField('Frequency', choices=[('monthly', 'Monthly'), ('bi-weekly', 'Bi-Weekly'), ('weekly', 'Weekly'), ('once', 'Once')], validators=[DataRequired()])
    income_date = DateField('Income Date')
    submit = SubmitField('Add Income Source')

class SavingsAccountForm(FlaskForm):
    name = StringField('Account Name', validators=[DataRequired()])
    balance = FloatField('Balance', validators=[DataRequired()])
    account_type = SelectField('Account Type', choices=[('liquid', 'Liquid Savings'), ('investment', 'Investment')], validators=[DataRequired()])
    submit = SubmitField('Add Savings Account')

class ExpenseForm(FlaskForm):
    name = StringField('Expense Name', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    expense_type = SelectField('Expense Type', choices=[('fixed', 'Fixed'), ('variable', 'Variable')], validators=[DataRequired()])
    due_date = DateField('Due Date')
    submit = SubmitField('Add Expense')

class CreditCardForm(FlaskForm):
    name = StringField('Card Name', validators=[DataRequired()])
    balance = FloatField('Balance', validators=[DataRequired()])
    interest_rate = FloatField('Interest Rate', validators=[DataRequired()])
    promo_end_date = DateField('Promotional End Date')
    min_payment = FloatField('Minimum Payment', validators=[DataRequired()])
    submit = SubmitField('Add Credit Card')