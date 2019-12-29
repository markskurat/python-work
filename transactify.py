# blist[1]["place"] = qdoba

blist = [
    {
        "amount": 2307.21,
        "place": "Apple Store",
        "acct": "Chase Checking",
    },
    {
        "amount": 75.20,
        "place": "Qdoba",
        "acct": "Wells Savings",
    },
    {
        "amount": 25,
        "place": "Food Depot",
        "acct": "Chase Checking",
    },
    {
        "amount": 10000,
        "place": "Home Depot",
        "acct": "BofA Savings",
    },
    {
        "amount": "1500",
        "place": "Chipotle",
        "acct": "Chase Checking",
    },
    {
        "amount": 1700.56565656,
        "place": "Lowe's",
        "acct": "Chase Checking",
    },
    {
        "amount": 150,
        "place": "AMC Theaters",
        "acct": "Deutsche Bank",
    },
]

# create 3 lists for each part of the transaction

# Create and print a list of transactions above $100 
# Create and print a list of places we made transactions
# Create and print a list of the bank accounts we used

def transactify(transactions):
    print(transactions)
    accts = []
    amts = []
    new_amts = []
    places = []
    for transaction in transactions:
        print(transaction)
        for component in transaction:
            print(component)
            if(component == "amount"):
                amount_formatted = round(float(transaction[component]), 2)
                if(amount_formatted > 100):
                    amts.append(amount_formatted)
                else:
                    print("transaction below $100")
            if(component == "place"):
                if(transaction[component] not in places):
                    places.append(transaction[component])
                else:
                    print("repeat place")
            if(component == "acct"):
                if(transaction[component] not in accts):
                    accts.append(transaction[component])

    for amount in amts:
        new_amt_num = round(float(amount), 2)
        new_amt = "${:.2f}".format(new_amt_num)
        new_amts.append(new_amt)

    print(accts)
    print(new_amts)
    print(places)

transactify(blist)