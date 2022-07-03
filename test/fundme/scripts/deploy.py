from brownie import FundMe, config, network
from scripts.common import get_account , deploy_mocks



def fundme():
    # getting the key
    account = get_account()

    # getting the price feed key
    pricefeed = config['networks'][network.show_active()][
        'eth_usd_price_feed'] if network.show_active() != "development" else deploy_mocks()

    # deploying the contract
    print(f"The active network is {network.show_active()}\n")
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
