from app import create_app, db
from app.models import CheckingAccount, IncomeSource, SavingsAccount, Expense, CreditCard

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'CheckingAccount': CheckingAccount, 'IncomeSource': IncomeSource,
            'SavingsAccount': SavingsAccount, 'Expense': Expense, 'CreditCard': CreditCard}

if __name__ == '__main__':
    app.run(debug=True)