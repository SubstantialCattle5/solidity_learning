import json
import solcx
import web3.eth
from flask.cli import load_dotenv
from web3 import Web3
import os

load_dotenv("/home/nilay/Programming/pvt_keys/keys.txt")

with open("SimpleStorage.sol", "r") as file:
    SimpleStorage_file = file.read()
    solcx.install_solc('0.6.0')

    compiled_sol = solcx.compile_standard(
        input_data={
            "language": "Solidity",
            "sources": {
                "SimpleStorage.sol": {"content": SimpleStorage_file}
            },
            "settings": {
                "outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}}
            },

        },
        solc_version="0.6.0"
    )

with open("compiled_code.json", 'w') as file:
    json.dump(compiled_sol, file, indent=4)

# get the bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/a9bfcabc92bb4375a2f9d53e6e25c272"))
chain_id = 4
address = os.getenv('address')
private_key = os.getenv('private_key')

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# latest transaction count for nonce
nonce = w3.eth.getTransactionCount(address)

# building a transaction
# sign a transaction
# send a transaction

transaction = SimpleStorage.constructor().buildTransaction({
    "gasPrice": w3.eth.gas_price,
    "chainId": chain_id,
    "from": address,
    "nonce": nonce,
})

# signing a transaction
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# sending the transaction to the blockchain
tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# working with the contract
#  address + contract abi
# cal --> simulate making the call but no state changes
# transact call --> make the state change

# Working with deployed Contracts
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(f"Initial Stored Value {simple_storage.functions.retrieve().call()}")
greeting_transaction = simple_storage.functions.store(20).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": address,
        "nonce": nonce + 1,
    }
)
signed_greeting_txn = w3.eth.account.sign_transaction(
    greeting_transaction, private_key=private_key
)
tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.rawTransaction)
print("Updating stored Value...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)

print(simple_storage.functions.retrieve().call())
