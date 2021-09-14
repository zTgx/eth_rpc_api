import sys
sys.path.append("..")

from ethjsonrpc import EthJsonRpc
import os

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
    # eth_sendTransaction,
    # eth_call,
    # eth_getStorageAt,
    'eth_getBlockByHash',
    'eth_getBlockByNumber',
    'eth_getTransactionCount',
    'eth_getBlockTransactionCountByHash',
    # eth_getBlockTransactionCountByNumber,
    # eth_getUncleCountByBlockHash,
    # eth_getUncleCountByBlockNumber,
    # eth_getCode,
    # eth_sendRawTransaction,
    # eth_estimateGas,
    # eth_getTransactionByHash,
    # eth_getTransactionByBlockHashAndIndex,
    # eth_getTransactionByBlockNumberAndIndex,
    # eth_getTransactionReceipt,
    # eth_getUncleByBlockHashAndIndex,
    # eth_getUncleByBlockNumberAndIndex,
    # eth_getLogs,
    # eth_submitWork,
    # eth_submitHashrate,

    'eth_getBalance',
]

env_dist = os.environ
evm_service = env_dist['EVM_SERVICE']
evm_service_port = env_dist['EVM_SERVICE_PORT']
print ("evm_service : [", evm_service, "]")
print ("evm_service_port : ", evm_service_port)
 
def init(service='127.0.0.1', port=8545):
    return EthJsonRpc(service, port)

c = init(evm_service, evm_service_port)

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

################################################################################

req = {
  "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
  "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
  "gas": 0x76c0, # 30400
  "gasPrice": 0x9184e72a000, # 10000000000000
  "value": 0x9184e72a, # 2441406250
  "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675",
}
result = c.eth_sendTransaction(req['to'], req['from'], req['gas'], req['gasPrice'], req['value'], req['data'])
print('eth_sendTransaction: %s (%s)' % (result, type(result)))

################################################################################

addr = '0xfd4745f393979351a1c5ea96ae21d18bcddc9468'
result = c.eth_getBalance(addr)
print('eth_getBalance: %s (%s)' % (result, type(result)))

################################################################################

b = (199583, '0x19d761c6f944eefe91ad70b9aff3d2d76c972e5bb68c443eea7c0eaa144cef9f')
result = c.eth_getBlockByHash(b[1], tx_objects=False)
print('eth_getBlockByHash: %s (%s)' % (result, type(result)))

result = c.eth_getBlockByNumber(b[0], tx_objects=False)
print('eth_getBlockByNumber: %s (%s)' % (result, type(result)))

################################################################################

addr = '0xfa52d88ffe966bf2bfab290b08e132efd28e9eaa'
for x in ['earliest', 'latest', 'pending', 150000]:
    result = c.eth_getTransactionCount(addr, x)
    print('eth_getTransactionCount: %s (%s)' % (result, type(result)))

################################################################################
tx_hash = '0x9476018748ba1dae5bdf5e3725f8966df1fa127d49f58e66f621bf6868a23c85'
result = c.eth_getBlockTransactionCountByHash(tx_hash)
print ('eth_getBlockTransactionCountByHash: %s (%s)' % (result, type(result)))
