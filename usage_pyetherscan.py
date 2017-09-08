from pyetherscan import Client
from geth import LiveGethProcess
# ！！！ http://pyetherscan.readthedocs.io/en/latest/
client = Client()
# my public address
address = '0x39B9ff96753d04C816109b347baC0313545e93cf'
address_balance = client.get_single_balance(address)
address_balance.response_status_code
address_balance.message
address_balance.balance

geth = LiveGethProcess()
geth.start()
geth.data_dir
geth.rpc_port

from pyetherscan import Address
ethereum_address = Address('0x70faa28A6B8d6829a4b1E649d26eC9a2a39ba413')
ethereum_address.balance
ethereum_address.transactions


block_number = 2165403
block_data = client.get_block_and_uncle_rewards_by_block_number(block_number)
block_data.rewards_data