from brownie import accounts, simplestorage, network, config


def deploy_simple_storage():
    account = get_account()
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


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    print("Hello!")
    deploy_simple_storage()
