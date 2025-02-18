
Installation
------------

You may need additional libraries and tools before installing ethjsonrpc.
If you see something like that:

.. code:: bash
    scrypt-1.2.1/libcperciva/crypto/crypto_aes.c:6:10: fatal error: openssl/aes.h: Нет такого файла или каталога
     #include <openssl/aes.h>
              ^~~~~~~~~~~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1


Install libssl-dev packqage



To install  eth_rpc_api:

.. code:: bash

   $ pip3 install eth_rpc_api


Make sure to have a node running an Ethereum client (such as geth) for the library to connect to.

Example
-------

.. code:: python

   >>> from ethjsonrpc import EthJsonRpc  # to use Parity-specific methods, import ParityEthJsonRpc
   >>> c = EthJsonRpc('127.0.0.1', 8545)
   >>> c.net_version()
   u'1'
   >>> c.web3_clientVersion()
   u'Geth/v1.3.3/linux/go1.5.1'
   >>> c.eth_gasPrice()
   50000000000
   >>> c.eth_blockNumber()
   828948


High-level functionality
------------------------

These examples assume the following simple Solidity contract:

.. code::

   contract Example {

       string s;

       function set_s(string new_s) {
           s = new_s;
       }

       function get_s() returns (string) {
           return s;
       }
   }


Compile it like this:

.. code:: bash

   $ solc --binary stdout example.sol


Setup
`````

.. code:: python

   >>> compiled = '606060405261020f806100136000396000f30060606040526000357c01000000000000000000000000000000000000000000000000000000009004806375d74f3914610044578063e7aab290146100bd57610042565b005b61004f600450610191565b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156100af5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b61010d6004803590602001906004018035906020019191908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050905061010f565b005b806000600050908051906020019082805482825590600052602060002090601f01602090048101928215610160579182015b8281111561015f578251826000505591602001919060010190610141565b5b50905061018b919061016d565b80821115610187576000818150600090555060010161016d565b5090565b50505b50565b60206040519081016040528060008152602001506000600050805480601f0160208091040260200160405190810160405280929190818152602001828054801561020057820191906000526020600020905b8154815290600101906020018083116101e357829003601f168201915b5050505050905061020c565b9056'
   >>> from ethjsonrpc import EthJsonRpc  # to use Parity-specific methods, import ParityEthJsonRpc
   >>> c = EthJsonRpc('127.0.0.1', 8545)


Creating a contract on the blockchain
`````````````````````````````````````

.. code:: python

   >>> # continued from above
   >>> contract_tx = c.create_contract(c.eth_coinbase(), compiled, gas=300000)
   >>> # wait here for the contract to be created when a new block is mined
   >>> contract_addr = c.get_contract_address(contract_tx)
   >>> contract_addr
   u'0x24988147f2f2300450103d8c42c43182cf226857'


Calling a contract function with a transaction (storing data)
`````````````````````````````````````````````````````````````

.. code:: python

   >>> # continued from above
   >>> tx = c.call_with_transaction(c.eth_coinbase(), contract_addr, 'set_s(string)', ['Hello, world'])
   >>> tx
   u'0x15bde63d79466e3db5169a913bb2069130ca387033d2ff2e29f4dfbef1bc6e0d'


Calling a contract function on the local blockchain (reading data)
``````````````````````````````````````````````````````````````````

.. code:: python

   >>> # continued from above
   >>> results = c.call(contract_addr, 'get_s()', [], ['string'])
   >>> results
   ['Hello, world']


Additional examples
-------------------

Please see ``test.py`` for additional examples.
