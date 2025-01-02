<a name="autonomy.chain.tx"></a>
# autonomy.chain.tx

Tx settlement helper.

<a name="autonomy.chain.tx.should_rebuild"></a>
#### should`_`rebuild

```python
should_rebuild(error: str) -> bool
```

Check if we should rebuild the transaction.

<a name="autonomy.chain.tx.should_retry"></a>
#### should`_`retry

```python
should_retry(error: str) -> bool
```

Check an error message to check if we should raise an error or retry the tx

<a name="autonomy.chain.tx.should_reprice"></a>
#### should`_`reprice

```python
should_reprice(error: str) -> bool
```

Check an error message to check if we should reprice the transaction

<a name="autonomy.chain.tx.TxSettler"></a>
## TxSettler Objects

```python
class TxSettler()
```

Tx settlement helper

<a name="autonomy.chain.tx.TxSettler.__init__"></a>
#### `__`init`__`

```python
 | __init__(ledger_api: LedgerApi, crypto: Crypto, chain_type: ChainType, timeout: Optional[float] = None, retries: Optional[int] = None, sleep: Optional[float] = None) -> None
```

Initialize object.

<a name="autonomy.chain.tx.TxSettler.build"></a>
#### build

```python
 | build(method: Callable[[], Dict], contract: str, kwargs: Dict) -> Dict
```

Build transaction.

<a name="autonomy.chain.tx.TxSettler.transact"></a>
#### transact

```python
 | transact(method: Callable[[], Dict], contract: str, kwargs: Dict, dry_run: bool = False) -> Dict
```

Make a transaction and return a receipt

<a name="autonomy.chain.tx.TxSettler.process"></a>
#### process

```python
 | process(event: str, receipt: Dict, contract: PublicId) -> Dict
```

Process tx receipt.

