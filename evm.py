from ethjsonrpc import EthJsonRpc
import os

# get methods
get_methods = [
    'web3_clientVersion',
    'net_version',
    'net_peerCount',
    'net_listening',
    'eth_protocolVersion',
    'eth_syncing',
    'eth_coinbase',
    'eth_mining',
    'eth_hashrate',
    'eth_gasPrice',
    'eth_accounts',
    'eth_blockNumber',
    'eth_getWork',
]

# post methods
post_methods = [
    'eth_sendTransaction',
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


