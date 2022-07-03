from brownie import FundMe
from scripts.common import get_account


def fund():
    fundme = FundMe[-1]
    account = get_account()
    entrance_fee = fundme.getEntranceFee()
    print(f"The current entry fee {entrance_fee}")
    print("Funding")
    fundme.fund({
        "from": account,
        "value": entrance_fee,
    })


def withdraw():
    fundme = FundMe[-1]
    account = get_account()
    withdraw = fundme.withdraw({
        "from": account
    })


def main():
    fund()
    withdraw()