# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import CheckingAccount, IncomeSource, SavingsAccount, Expense, CreditCard
from app.forms import CheckingAccountForm, IncomeSourceForm, SavingsAccountForm, ExpenseForm, CreditCardForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/accounts', methods=['GET', 'POST'])
def accounts():
    form = CheckingAccountForm()
    if form.validate_on_submit():
        account = CheckingAccount(name=form.name.data, balance=form.balance.data, date=form.date.data)
        db.session.add(account)
        db.session.commit()
        flash('Account added successfully!', 'success')
        return redirect(url_for('main.accounts'))
    accounts = CheckingAccount.query.all()
    return render_template('accounts.html', form=form, accounts=accounts)

@bp.route('/income', methods=['GET', 'POST'])
def income():
    form = IncomeSourceForm()
    if form.validate_on_submit():
        income = IncomeSource(name=form.name.data, amount=form.amount.data, frequency=form.frequency.data)
        db.session.add(income)
        db.session.commit()
        flash('Income source added successfully!', 'success')
        return redirect(url_for('main.income'))
    income_sources = IncomeSource.query.all()
    return render_template('income.html', form=form, income_sources=income_sources)

@bp.route('/savings', methods=['GET', 'POST'])
def savings():
    form = SavingsAccountForm()
    if form.validate_on_submit():
        account = SavingsAccount(name=form.name.data, balance=form.balance.data, account_type=form.account_type.data)
        db.session.add(account)
        db.session.commit()
        flash('Savings account added successfully!', 'success')
        return redirect(url_for('main.savings'))
    accounts = SavingsAccount.query.all()
    return render_template('savings.html', form=form, accounts=accounts)

@bp.route('/expenses', methods=['GET', 'POST'])
def expenses():
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(name=form.name.data, amount=form.amount.data, expense_type=form.expense_type.data, due_date=form.due_date.data)
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully!', 'success')
        return redirect(url_for('main.expenses'))
    expenses = Expense.query.all()
    return render_template('expenses.html', form=form, expenses=expenses)

@bp.route('/credit_cards', methods=['GET', 'POST'])
def credit_cards():
    form = CreditCardForm()
    if form.validate_on_submit():
        card = CreditCard(name=form.name.data, balance=form.balance.data, interest_rate=form.interest_rate.data,
                          promo_end_date=form.promo_end_date.data, min_payment=form.min_payment.data)
        db.session.add(card)
        db.session.commit()
        flash('Credit card added successfully!', 'success')
        return redirect(url_for('main.credit_cards'))
    cards = CreditCard.query.all()
    return render_template('credit_cards.html', form=form, cards=cards)

@bp.route('/dashboard')
def dashboard():
    # Fetch data for charts
    expenses = Expense.query.all()
    incomes = IncomeSource.query.all()
    accounts = CheckingAccount.query.all()
    savings = SavingsAccount.query.all()
    credit_cards = CreditCard.query.all()

    return render_template('dashboard.html', 
                           expenses=expenses, 
                           incomes=incomes, 
                           accounts=accounts, 
                           savings=savings, 
                           credit_cards=credit_cards)

@bp.route('/api/chart-data')
def chart_data():
    expenses = Expense.query.all()
    incomes = IncomeSource.query.all()

    expense_data = [{'name': e.name, 'amount': e.amount} for e in expenses]
    income_data = [{'name': i.name, 'amount': i.amount} for i in incomes]

    return jsonify({
        'expenses': expense_data,
        'incomes': income_data
    })