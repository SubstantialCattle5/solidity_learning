from brownie import FundMe, config
from scripts.common import get_account


def fundme():
    # getting the key
    account = get_account()
    pricefeed = config['networks']['rinkeby']['eth_usd_price_feed']
    fundme_deploy = FundMe.deploy(pricefeed, {
        "from": account
    })
    print(f"The Contract is deployed on {fundme_deploy.address}")
    fundme_deploy

def main():
    print("----Running the Program-----")
    fundme()
