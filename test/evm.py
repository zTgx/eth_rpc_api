import sys
sys.path.append("..")

from ethjsonrpc import EthJsonRpc
import os
import rlp
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
# get methods
get_methods = [
    'eth_protocolVersion',
    'eth_hashrate',
    'eth_chainId',
    'eth_accounts',
    'eth_coinbase',
    'eth_mining',
    'eth_gasPrice',
    'eth_blockNumber',
    'eth_getWork',
    'web3_clientVersion',
    'net_version',
    'net_peerCount',
    'net_listening',
    'eth_syncing',
]

# post methods
post_methods = [
    'eth_sendTransaction',
    'eth_getBalance',
    'eth_call',
    'eth_getStorageAt',
    'eth_getBlockByHash',
    'eth_getBlockByNumber',
    'eth_getTransactionCount',
    'eth_getBlockTransactionCountByHash',
    'eth_getBlockTransactionCountByNumber',
    'eth_getUncleCountByBlockHash',
    'eth_getUncleCountByBlockNumber',
    'eth_getCode',
    'eth_sendRawTransaction',
    'eth_estimateGas',
    'eth_getTransactionByHash',
    'eth_getTransactionByBlockHashAndIndex',
    'eth_getTransactionByBlockNumberAndIndex',
    'eth_getTransactionReceipt',
    'eth_getUncleByBlockHashAndIndex',
    'eth_getUncleByBlockNumberAndIndex',
    'eth_getLogs',

    # eth_submitWork, #false 
    # eth_submitHashrate, #false
]

# env_dist = os.environ
# evm_service = env_dist['EVM_SERVICE']
# evm_service_port = env_dist['EVM_SERVICE_PORT']
# print ("evm_service : [", evm_service, "]")
# print ("evm_service_port : ", evm_service_port)
 
def init(service='127.0.0.1', port=8545):
    return EthJsonRpc(service, port)

c = init()

################################################################################
print('*' * 80)
print("Method Type : GET")
print("Get Method Numbers : ", len(get_methods))
print ()
for m in get_methods:
    meth = getattr(c, m)
    result = meth()
    print('%s: %s (%s)' % (m, result, type(result)))

print('*' * 80)

################################################################################
print("Method Type : POST")
print("POST Method Numbers : ", len(post_methods))
print()

# params = [{
#   "from": "0x407d73d8a49eeb85d32cf465507dd71d507100c1",
# #   "to": "0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b",
#   "value": "0x186a0" // 100000
# }
# result = c.eth_call()

# ################################################################################

addr = '0xF5224110db945b54466D275Cd224feD2dD110E67'
tx = '0xcd41788d99a4744f58308dbe3d422e5f5dee647523dace24bde4f3373b2aa096'

result = c.eth_getBalance(addr)
print('eth_getBalance: %s (%s)' % (result, type(result)))

# ################################################################################

b_hash = '0x3e9c3c9eb70439924fa95f1bdd9513d053c17f9ed1b8b96615067b3009e931c0'
result = c.eth_getBlockByHash(b_hash, tx_objects=False)
print('eth_getBlockByHash: %s (%s)' % (result, type(result)))

# ################################################################################
result = c.eth_getBlockByNumber()
print('eth_getBlockByNumber: %s (%s)' % (result, type(result)))

# ################################################################################

for x in ['earliest', 'latest', 'pending', 150000]:
    result = c.eth_getTransactionCount(addr, x)
    print('eth_getTransactionCount: %s (%s)' % (result, type(result)))

# ################################################################################
result = c.eth_getTransactionByHash(tx)
print ('eth_getTransactionByHash: %s (%s)' % (result, type(result)))

# ################################################################################
result = c.eth_getStorageAt('0x0033f3f4bfa0a4a74c0be0a4cb33a893226a7f65');
print ('eth_getStorageAt: %s (%s)' % (result, type(result)))

# ################################################################################

result = c.eth_getBlockTransactionCountByNumber()
print('eth_getBlockTransactionCountByNumber: %s (%s)' % (result, type(result)))
    
# ################################################################################

result = c.eth_getUncleCountByBlockHash(b_hash)
print('eth_getUncleCountByBlockHash: %s (%s)' % (result, type(result)))


# ################################################################################

result = c.eth_getUncleCountByBlockNumber()
print('eth_getUncleCountByBlockNumber: %s (%s)' % (result, type(result)))


# ################################################################################
result = c.eth_getCode(addr)
print('eth_getCode: %s (%s)' % (result, type(result)))

# ################################################################################
result = c.eth_getTransactionByHash(tx)
print('eth_getTransactionByHash: %s (%s)' % (result, type(result)))

# ################################################################################

result = c.eth_getTransactionByBlockHashAndIndex(b_hash)
print('eth_getTransactionByBlockHashAndIndex: %s (%s)' % (result, type(result)))

# ################################################################################
result = c.eth_getTransactionByBlockNumberAndIndex()
print('eth_getTransactionByBlockNumberAndIndex: %s (%s)' % (result, type(result)))

# ################################################################################
result = c.eth_getTransactionReceipt(tx)
print('eth_getTransactionReceipt: %s (%s)' % (result, type(result)))

# ################################################################################
result = c.eth_getUncleByBlockHashAndIndex(b_hash)
print('eth_getUncleByBlockHashAndIndex: %s (%s)' % (result, type(result)))

# ################################################################################
result = c.eth_getUncleByBlockNumberAndIndex()
print('eth_getUncleByBlockNumberAndIndex: %s (%s)' % (result, type(result)))

# ################################################################################
result = c.eth_estimateGas()
print('eth_estimateGas: %s (%s)' % (result, type(result)))

################################################################################

req = {
  "from": "0xf6aca39539374993b37d29ccf0d93fa214ea0af1",
  "to": "0xf6aca39539374993b37d29ccf0d93fa214ea0af1",
  "gas": 0x76c0, # 30400
  "gasPrice": 0x9184e72a000, # 10000000000000
  "value": 0x9184e72a, # 2441406250
  "nonce": 3,
  "data": 4,
}
result = c.eth_sendTransaction(req['to'], req['from'], req['gas'], req['gasPrice'], req['value'])
print('eth_sendTransaction: %s (%s)' % (result, type(result)))
# 0xe2a086048a6788dbafc84ac0b345136249a5fe295597cfa83373bd743d8f9654

################################################################################

# Transaction
# pub struct Transaction {
# 	pub nonce: U256,
# 	pub gas_price: U256,
# 	pub gas_limit: U256,
# 	pub action: TransactionAction,
# 	pub value: U256,
# 	pub input: Bytes,
# 	pub signature: TransactionSignature,
# }

signed_txn = w3.eth.account.sign_transaction(dict(
    nonce=3,
    gasPrice=3000000000,
    # gasLimit=2000000000,
    gas=100000,
    to='0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
    value=12345,
    data=b'x',
    # action=2,
  ),
  '9f7bebaa5c55464b10150bc2e0fd552e915e2bdbca95cc45ed1c909aca96e7f5',
)
result = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print('result : ', result)

# data = '0xb1092cb5b23c2aa55e5b5787729c6be812509376de99a52bea2b41e5a5f8601c5641e74d01e4493c17bf1ef8b179c49362b2c721222128d58422a539310c6ecd1b'
# result = c.eth_sendRawTransaction(data)
# print('eth_sendRawTransaction: %s (%s)' % (result, type(result)))


# ################################################################################

filt = w3.eth.filter('latest')
result = w3.eth.get_filter_logs(filt.filter_id)
print('eth_getLogs: %s (%s)' % (result, type(result)))
