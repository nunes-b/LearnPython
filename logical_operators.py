print("==================================================")
print(False and False)
print(False and True)
print(False or False)
print(False or True)
print("==================================================")
print("(AND) Para ser True, tudo tem que ser (True).")
print("(OR) Para ser True, apenas um ter que ser (True).")
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print("==================================================")

balance = 1000
withdraw = 200
limit = 100
account_special = True

print(balance >= withdraw and balance <= limit)
# balance is plus or equal withdraw (and) balance is lower or equal limit? No!
print("==================================================")

print(balance >= withdraw and withdraw <=
      limit or account_special and balance >= withdraw)
# Balance is plus or equal withdraw? Yes! (And) withdraw is lower or equal limit? No! (Or) account_special (And) balance is plus or equal whitdraw?  Yes.
print("==================================================")

print((balance >= withdraw and withdraw <= limit)
      or (account_special and balance >= withdraw))
# Balance is plus or equal withdraw? Yes. withdraw is lower or equal limit? No.  (Or)  account_special and balance is plus or equal withdraw? Yes.
print("==================================================")
