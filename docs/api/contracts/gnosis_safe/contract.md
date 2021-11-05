<a id="packages.valory.contracts.gnosis_safe.contract"></a>

# packages.valory.contracts.gnosis`_`safe.contract

This module contains the class to connect to an Gnosis Safe contract.

<a id="packages.valory.contracts.gnosis_safe.contract.checksum_address"></a>

#### checksum`_`address

```python
def checksum_address(agent_address: str) -> ChecksumAddress
```

Get the checksum address.

<a id="packages.valory.contracts.gnosis_safe.contract.SafeOperation"></a>

## SafeOperation Objects

```python
class SafeOperation(Enum)
```

Operation types.

<a id="packages.valory.contracts.gnosis_safe.contract.GnosisSafeContract"></a>

## GnosisSafeContract Objects

```python
class GnosisSafeContract(Contract)
```

The Gnosis Safe contract.

<a id="packages.valory.contracts.gnosis_safe.contract.GnosisSafeContract.get_raw_transaction"></a>

#### get`_`raw`_`transaction

```python
@classmethod
def get_raw_transaction(cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any) -> Optional[JSONLike]
```

Get the Safe transaction.

<a id="packages.valory.contracts.gnosis_safe.contract.GnosisSafeContract.get_raw_message"></a>

#### get`_`raw`_`message

```python
@classmethod
def get_raw_message(cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any) -> Optional[bytes]
```

Get raw message.

<a id="packages.valory.contracts.gnosis_safe.contract.GnosisSafeContract.get_state"></a>

#### get`_`state

```python
@classmethod
def get_state(cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any) -> Optional[JSONLike]
```

Get state.

<a id="packages.valory.contracts.gnosis_safe.contract.GnosisSafeContract.get_deploy_transaction"></a>

#### get`_`deploy`_`transaction

```python
@classmethod
def get_deploy_transaction(cls, ledger_api: LedgerApi, deployer_address: str, **kwargs: Any) -> Optional[JSONLike]
```

Get deploy transaction.

**Arguments**:

- `ledger_api`: ledger API object.
- `deployer_address`: the deployer address.
- `kwargs`: the keyword arguments.

**Returns**:

an optional JSON-like object.

<a id="packages.valory.contracts.gnosis_safe.contract.GnosisSafeContract.get_raw_safe_transaction_hash"></a>

#### get`_`raw`_`safe`_`transaction`_`hash

```python
@classmethod
def get_raw_safe_transaction_hash(cls, ledger_api: LedgerApi, contract_address: str, to_address: str, value: int, data: bytes, operation: int = SafeOperation.CALL.value, safe_tx_gas: int = 0, base_gas: int = 0, gas_price: int = 0, gas_token: str = NULL_ADDRESS, refund_receiver: str = NULL_ADDRESS, safe_nonce: Optional[int] = None, safe_version: Optional[str] = None, chain_id: Optional[int] = None) -> JSONLike
```

Get the hash of the raw Safe transaction.

Adapted from https://github.com/gnosis/gnosis-py/blob/69f1ee3263086403f6017effa0841c6a2fbba6d6/gnosis/safe/safe_tx.py#L125

Note, because safe_nonce is included in the tx_hash the agents implicitly agree on the order of txs if they agree on a tx_hash.

**Arguments**:

    (e.g. base transaction fee, signature check, payment of the refund)
- `ledger_api`: the ledger API object
- `contract_address`: the contract address
- `to_address`: the tx recipient address
- `value`: the ETH value of the transaction
- `data`: the data of the transaction
- `operation`: Operation type of Safe transaction
- `safe_tx_gas`: Gas that should be used for the Safe transaction
- `base_gas`: Gas costs for that are independent of the transaction execution
- `gas_price`: Gas price that should be used for the payment calculation
- `gas_token`: Token address (or `0x000..000` if ETH) that is used for the payment
- `refund_receiver`: Address of receiver of gas payment (or `0x000..000`  if tx.origin).
- `safe_nonce`: Current nonce of the Safe. If not provided, it will be retrieved from network
- `safe_version`: Safe version 1.0.0 renamed `baseGas` to `dataGas`. Safe version 1.3.0 added `chainId` to the `domainSeparator`. If not provided, it will be retrieved from network
- `chain_id`: Ethereum network chain_id is used in hash calculation for Safes >= 1.3.0. If not provided, it will be retrieved from the provided ethereum_client

**Returns**:

the hash of the raw Safe transaction

<a id="packages.valory.contracts.gnosis_safe.contract.GnosisSafeContract.get_raw_safe_transaction"></a>

#### get`_`raw`_`safe`_`transaction

```python
@classmethod
def get_raw_safe_transaction(cls, ledger_api: LedgerApi, contract_address: str, sender_address: str, owners: Tuple[str], to_address: str, value: int, data: bytes, signatures_by_owner: Dict[str, str], operation: int = SafeOperation.CALL.value, safe_tx_gas: int = 0, base_gas: int = 0, gas_price: int = 0, gas_token: str = NULL_ADDRESS, refund_receiver: str = NULL_ADDRESS, safe_nonce: Optional[int] = None) -> JSONLike
```

Get the raw Safe transaction

**Arguments**:

    (e.g. base transaction fee, signature check, payment of the refund)
- `ledger_api`: the ledger API object
- `contract_address`: the contract address
- `sender_address`: the address of the sender
- `owners`: the sequence of owners
- `to_address`: Destination address of Safe transaction
- `value`: Ether value of Safe transaction
- `data`: Data payload of Safe transaction
- `signatures_by_owner`: mapping from owners to signatures
- `operation`: Operation type of Safe transaction
- `safe_tx_gas`: Gas that should be used for the Safe transaction
- `base_gas`: Gas costs for that are independent of the transaction execution
- `gas_price`: Gas price that should be used for the payment calculation
- `gas_token`: Token address (or `0x000..000` if ETH) that is used for the payment
- `refund_receiver`: Address of receiver of gas payment (or `0x000..000`  if tx.origin).
- `safe_nonce`: Current nonce of the Safe. If not provided, it will be retrieved from network

**Returns**:

the raw Safe transaction

<a id="packages.valory.contracts.gnosis_safe.contract.GnosisSafeContract.verify_contract"></a>

#### verify`_`contract

```python
@classmethod
def verify_contract(cls, ledger_api: LedgerApi, contract_address: str) -> JSONLike
```

Verify the contract's bytecode

**Arguments**:

- `ledger_api`: the ledger API object
- `contract_address`: the contract address

**Returns**:

the verified status

<a id="packages.valory.contracts.gnosis_safe.contract.GnosisSafeContract.verify_tx"></a>

#### verify`_`tx

```python
@classmethod
def verify_tx(cls, ledger_api: LedgerApi, contract_address: str, tx_hash: str, owners: Tuple[str], to_address: str, value: int, data: bytes, signatures_by_owner: Dict[str, str], operation: int = SafeOperation.CALL.value, safe_tx_gas: int = 0, base_gas: int = 0, gas_price: int = 0, gas_token: str = NULL_ADDRESS, refund_receiver: str = NULL_ADDRESS, safe_version: Optional[str] = None) -> JSONLike
```

Verify a tx hash exists on the blockchain.

Currently, the implementation is an overkill as most of the verification is implicit by the acceptance of the transaction in the Safe.

**Arguments**:

    (e.g. base transaction fee, signature check, payment of the refund)
- `ledger_api`: the ledger API object
- `contract_address`: the contract address
- `tx_hash`: the transaction hash
- `owners`: the sequence of owners
- `to_address`: Destination address of Safe transaction
- `value`: Ether value of Safe transaction
- `data`: Data payload of Safe transaction
- `signatures_by_owner`: mapping from owners to signatures
- `operation`: Operation type of Safe transaction
- `safe_tx_gas`: Gas that should be used for the Safe transaction
- `base_gas`: Gas costs for that are independent of the transaction execution
- `gas_price`: Gas price that should be used for the payment calculation
- `gas_token`: Token address (or `0x000..000` if ETH) that is used for the payment
- `refund_receiver`: Address of receiver of gas payment (or `0x000..000`  if tx.origin).
- `safe_version`: Safe version 1.0.0 renamed `baseGas` to `dataGas`. Safe version 1.3.0 added `chainId` to the `domainSeparator`. If not provided, it will be retrieved from network

**Returns**:

the verified status
