from brownie import accounts, simplestorage


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = simplestorage.deploy({
        'from': account
    })

    stored_value = simple_storage.retrieve()
    print(stored_value)

    transaction = simple_storage.store(15, {
        "from": account,
    })
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)


def main():
    print("Hello!")
    deploy_simple_storage()
