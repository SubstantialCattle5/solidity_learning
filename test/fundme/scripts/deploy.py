from brownie import FundMe, config, network, MockV3Aggregator
from scripts.common import get_account

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = 200000000000



def deploy_mocks():
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    mock_aggregator = MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!")
    return  mock_aggregator.address

def fundme():
    # getting the key
    account = get_account()

    # deploying the contract
    # getting the price feed key
    pricefeed = 0
    if network.show_active() != "development":
        pricefeed = config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        pricefeed = deploy_mocks()

    print(f"The active network is {network.show_active()}")

    fundme_deploy = FundMe.deploy(
        pricefeed, {
            "from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"The Contract is deployed on {fundme_deploy.address}")
    print(f"The Price {fundme_deploy.getPrice()}")


def main():
    print("----Running the Program-----")
    fundme()
