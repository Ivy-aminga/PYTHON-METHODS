class Account:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    self.deposits = []
    self.withdrawals = []
    self.loan_balance = 0
    self.deposit_count = 0

  def check_balance(self):
    return self.balance

  def deposit(self, amount):
    self.balance += amount
    self.deposits.append({"amount": amount, "narration": "deposit"})
    self.deposit_count += 1

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      self.withdrawals.append({"amount": amount, "narration": "withdrawal"})
      return True
    else:
      return False

  def print_statement(self):
    for transaction in self.deposits + self.withdrawals:
      narration = transaction["narration"]
      amount = transaction["amount"]
      print(f"{narration} - {amount}")

  def borrow_loan(self, amount):
    if self.loan_balance == 0 and amount > 100 and self.deposit_count >= 10 and amount <= (self.balance / 3):
      self.loan_balance += amount
      self.balance += amount
      return True
    else:
      return False

  def repay_loan(self, amount):
    if amount > self.loan_balance:
      self.balance += (amount - self.loan_balance)
      self.loan_balance = 0
    else:
      self.loan_balance -= amount
      self.balance -= amount

  def transfer(self, amount, destination):
    if self.balance >= amount:
      self.balance -= amount
      destination.deposit(amount)
      return True
    else:
      return False
