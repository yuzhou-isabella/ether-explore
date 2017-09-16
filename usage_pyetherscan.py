from pyetherscan import Client

client = Client()
address_bw = "0xbcdfc35b86bedf72f0cda046a3c16829a2ef41d1"
address_balance = client.get_single_balance(address_bw)
address_balance.response_status_code
address_balance.message
# in the units of wei
address_balance.balance
