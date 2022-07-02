from brownie import accounts


def deploy_simple_storage():
    account = accounts.load("main_account")
    print(account)


def main():
    print("Hello!")
    deploy_simple_storage()
