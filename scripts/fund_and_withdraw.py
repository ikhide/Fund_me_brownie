from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    print('this account 1', account.address)
    entrance_fee = fund_me.getEntranceFee() +100
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})

def fundBalance():
    fund_me = FundMe[-1]
    account = get_account()
    print('this account 2', account.address)
    balance =  fund_me.addressToAmountFunded(account.address)
    print('balance', balance)

def main():
    fund()
    fundBalance()