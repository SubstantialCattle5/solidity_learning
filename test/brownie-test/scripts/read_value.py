from brownie import accounts, simplestorage, network, config


def read_contract():
    simple_storage = simplestorage[-1]
    print(simple_storage)
    print(simple_storage.retrieve())
def main():
    print("Hello!")
    read_contract()
