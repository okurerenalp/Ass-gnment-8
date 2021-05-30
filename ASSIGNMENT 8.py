import os

userType = input("Press 1 to open an existing account, press 2 to create a new account: ")
# If userType is 1, the program will update an existing account, and if it's 2, 
# it'll create a new one.
if userType == "1":
    name = input("What is the name of the account: ")
    if os.path.exists(name):
        print("[EXISTS] An account with the given name exists...")
        file = open(name)
        transactions = file.readlines()

        # Splitting the lines by "\t.""
        for i in range(len(transactions)):
            transactions[i] = transactions[i].split("\t")
            transactions[i][6] = transactions[i][6].replace("\n", "")
        
        # If debit is zero, print creadit balance.
        # Else, print debit.
        if transactions[len(transactions) - 1][5] == 0:
            print(transactions[len(transactions) - 1][6])
        else:
            print(transactions[len(transactions) - 1][5])

        # Ask for an operation.
        operation = input("Press 1 for deposit, press 2 for credit: ")
        date = input("What is the date: ")

        # ---- DEBIT ----
        if operation == "1":
            debit = int(input("Enter the debit that you'd like to deposit: "))

            

            toAdd = debit - int(transactions[len(transactions) - 1][6])
            if toAdd > 0:
                creditBal = 0
                debitBal = int(transactions[len(transactions) - 1][5]) + toAdd
            else:
                creditBal = toAdd * (-1)
                debitBal = int(transactions[len(transactions) - 1][5])

            # This is the new transaction.
            newTransaction = transactions[len(transactions) - 1]
            newTransaction[0] = "\n" + newTransaction[0]
            newTransaction[2] = date
            newTransaction[3] = str(debit)
            newTransaction[4] = str(0)
            newTransaction[5] = str(debitBal)
            newTransaction[6] = str(creditBal)

            newTransaction = "\t".join(newTransaction)
            print("newTransaction:", newTransaction)

            # Write down the newly created transaction to the account.
            file = open(name, "a")
            file.write(newTransaction)
            file.close()
                

        # ---- WITDHRAWAL ----
        else:
            credit = int(input("Enter the debit that you'd like to witdhraw: "))

            toAdd = credit - int(transactions[len(transactions) - 1][5])
            if toAdd > 0:
                debitBal = 0
                creditBal = int(transactions[len(transactions) - 1][6]) + toAdd
            else:
                debitBal = toAdd * (-1)
                creditBal = int(transactions[len(transactions) - 1][6])


            # This is the new transaction.
            newTransaction = transactions[len(transactions) - 1]
            newTransaction[0] = "\n" + newTransaction[0]
            newTransaction[3] = str(0)
            newTransaction[4] = str(credit)
            newTransaction[5] = str(creditBal)
            newTransaction[6] = str(debitBal)

            newTransaction = "\t".join(newTransaction)
            print("newTransaction:", newTransaction)

            # Write down the newly created transaction to the account.
            file = open(name, "a")
            file.write(newTransaction)
            file.close()
    else:
        print("[ERROR] An account with the given name does not exists: ")
        print("Try creating a new account instead: ")
        exit(0)
else:
    file = input("What is the name of the account: ")
    f = open(file, "w")
    accNumber = input("What is the name account number: ")
    date = input("What is the date: ")
    newTransaction = []
    newTransaction.append(file)
    newTransaction.append(accNumber)
    newTransaction.append(date)
    for i in range(4):
        newTransaction.append("0")

    newTransaction = "\t".join(newTransaction)
    f.write(newTransaction)
    print("[DONE] Account creation is successful.")
    f.close()