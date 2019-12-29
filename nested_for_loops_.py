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

def format_transactions(transactions):
    accts = []
    amts = []
    places = []
    fmt_amts = []

    for transaction in transactions:
        for component in transaction:
            if(component == "amount"):
                amount_formatted = round(float(transaction[component]), 2)
                if(amount_formatted > 100):
                    amts.append(amount_formatted)
            if(component == "place"):
                if(transaction[component] not in places):
                    places.append(transaction[component])
            if(component == "acct"):
                if(transaction[component] not in accts):
                    accts.append(transaction[component])
    for amt in amts:
        dollar = "${:.2f}".format(amt)
        fmt_amts.append(dollar)

    print(accts)
    print(places)
    print(fmt_amts)

format_transactions(blist)