from brownie import network, accounts, config, MockV3Aggregator
import web3

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = web3.Web3.toWei(2000, 'ether')


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    # checking if the aggregator already exists or not
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {
            "from": account
        })
        print("Mocks Deployed!")

    return MockV3Aggregator[-1].address
