<a name="packages.valory.skills.transaction_settlement_abci.behaviours"></a>
# packages.valory.skills.transaction`_`settlement`_`abci.behaviours

This module contains the behaviours for the 'abci' skill.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.TransactionSettlementBaseBehaviour"></a>
## TransactionSettlementBaseBehaviour Objects

```python
class TransactionSettlementBaseBehaviour(BaseBehaviour,  ABC)
```

Base behaviour for the common apps' skill.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.TransactionSettlementBaseBehaviour.synchronized_data"></a>
#### synchronized`_`data

```python
 | @property
 | synchronized_data() -> SynchronizedData
```

Return the synchronized data.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.TransactionSettlementBaseBehaviour.params"></a>
#### params

```python
 | @property
 | params() -> TransactionParams
```

Return the params.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.TransactionSettlementBaseBehaviour.serialized_keepers"></a>
#### serialized`_`keepers

```python
 | @staticmethod
 | serialized_keepers(keepers: Deque[str], keeper_retries: int) -> str
```

Get the keepers serialized.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.TransactionSettlementBaseBehaviour.get_gas_price_params"></a>
#### get`_`gas`_`price`_`params

```python
 | get_gas_price_params(tx_body: dict) -> List[str]
```

Guess the gas strategy from the transaction params

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.RandomnessTransactionSubmissionBehaviour"></a>
## RandomnessTransactionSubmissionBehaviour Objects

```python
class RandomnessTransactionSubmissionBehaviour(RandomnessBehaviour)
```

Retrieve randomness.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SelectKeeperTransactionSubmissionBehaviourA"></a>
## SelectKeeperTransactionSubmissionBehaviourA Objects

```python
class SelectKeeperTransactionSubmissionBehaviourA(  # pylint: disable=too-many-ancestors
    SelectKeeperBehaviour,  TransactionSettlementBaseBehaviour)
```

Select the keeper agent.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SelectKeeperTransactionSubmissionBehaviourA.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Do the action.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SelectKeeperTransactionSubmissionBehaviourB"></a>
## SelectKeeperTransactionSubmissionBehaviourB Objects

```python
class SelectKeeperTransactionSubmissionBehaviourB(  # pylint: disable=too-many-ancestors
    SelectKeeperTransactionSubmissionBehaviourA)
```

Select the keeper b agent.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SelectKeeperTransactionSubmissionBehaviourB.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Do the action.

Steps:
    - If we have not selected enough keepers for the period,
        select a keeper randomly and add it to the keepers' queue, with top priority.
    - Otherwise, cycle through the keepers' subset, using the following logic:
        A `PENDING` verification status means that we have not received any errors,
        therefore, all we know is that the tx has not been mined yet due to low pricing.
        Consequently, we are going to retry with the same keeper in order to replace the transaction.
        However, if we receive a status other than `PENDING`, we need to cycle through the keepers' subset.
        Moreover, if the current keeper has reached the allowed number of retries, then we cycle anyway.
    - Send the transaction with the keepers and wait for it to be mined.
    - Wait until ABCI application transitions to the next round.
    - Go to the next behaviour (set done event).

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SelectKeeperTransactionSubmissionBehaviourBAfterTimeout"></a>
## SelectKeeperTransactionSubmissionBehaviourBAfterTimeout Objects

```python
class SelectKeeperTransactionSubmissionBehaviourBAfterTimeout(  # pylint: disable=too-many-ancestors
    SelectKeeperTransactionSubmissionBehaviourB)
```

Select the keeper b agent after a timeout.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.ValidateTransactionBehaviour"></a>
## ValidateTransactionBehaviour Objects

```python
class ValidateTransactionBehaviour(TransactionSettlementBaseBehaviour)
```

Validate a transaction.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.ValidateTransactionBehaviour.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Do the action.

Steps:
- Validate that the transaction hash provided by the keeper points to a
  valid transaction.
- Send the transaction with the validation result and wait for it to be
  mined.
- Wait until ABCI application transitions to the next round.
- Go to the next behaviour (set done event).

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.ValidateTransactionBehaviour.has_transaction_been_sent"></a>
#### has`_`transaction`_`been`_`sent

```python
 | has_transaction_been_sent() -> Generator[None, None, Optional[bool]]
```

Transaction verification.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.CheckTransactionHistoryBehaviour"></a>
## CheckTransactionHistoryBehaviour Objects

```python
class CheckTransactionHistoryBehaviour(TransactionSettlementBaseBehaviour)
```

Check the transaction history.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.CheckTransactionHistoryBehaviour.history"></a>
#### history

```python
 | @property
 | history() -> List[str]
```

Get the history of hashes.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.CheckTransactionHistoryBehaviour.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Do the action.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.CheckLateTxHashesBehaviour"></a>
## CheckLateTxHashesBehaviour Objects

```python
class CheckLateTxHashesBehaviour(  # pylint: disable=too-many-ancestors
    CheckTransactionHistoryBehaviour)
```

Check the late-arriving transaction hashes.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.CheckLateTxHashesBehaviour.history"></a>
#### history

```python
 | @property
 | history() -> List[str]
```

Get the history of hashes.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SynchronizeLateMessagesBehaviour"></a>
## SynchronizeLateMessagesBehaviour Objects

```python
class SynchronizeLateMessagesBehaviour(TransactionSettlementBaseBehaviour)
```

Synchronize late-arriving messages behaviour.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SynchronizeLateMessagesBehaviour.__init__"></a>
#### `__`init`__`

```python
 | __init__(**kwargs: Any)
```

Initialize a `SynchronizeLateMessagesBehaviour`

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SynchronizeLateMessagesBehaviour.setup"></a>
#### setup

```python
 | setup() -> None
```

Setup the `SynchronizeLateMessagesBehaviour`.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SynchronizeLateMessagesBehaviour.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Do the action.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SignatureBehaviour"></a>
## SignatureBehaviour Objects

```python
class SignatureBehaviour(TransactionSettlementBaseBehaviour)
```

Signature behaviour.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.SignatureBehaviour.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Do the action.

Steps:
- Request the signature of the transaction hash.
- Send the signature as a transaction and wait for it to be mined.
- Wait until ABCI application transitions to the next round.
- Go to the next behaviour (set done event).

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.FinalizeBehaviour"></a>
## FinalizeBehaviour Objects

```python
class FinalizeBehaviour(TransactionSettlementBaseBehaviour)
```

Finalize behaviour.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.FinalizeBehaviour.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator[None, None, None]
```

Do the action.

Steps:
- If the agent is the keeper, then prepare the transaction and send it.
- Otherwise, wait until the next round.
- If a timeout is hit, set exit A event, otherwise set done event.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.FinalizeBehaviour.handle_late_messages"></a>
#### handle`_`late`_`messages

```python
 | handle_late_messages(behaviour_id: str, message: Message) -> None
```

Store a potentially late-arriving message locally.

**Arguments**:

- `behaviour_id`: the id of the behaviour in which the message belongs to.
- `message`: the late arriving message to handle.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.ResetBehaviour"></a>
## ResetBehaviour Objects

```python
class ResetBehaviour(TransactionSettlementBaseBehaviour)
```

Reset behaviour.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.ResetBehaviour.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Do the action.

<a name="packages.valory.skills.transaction_settlement_abci.behaviours.TransactionSettlementRoundBehaviour"></a>
## TransactionSettlementRoundBehaviour Objects

```python
class TransactionSettlementRoundBehaviour(AbstractRoundBehaviour)
```

This behaviour manages the consensus stages for the basic transaction settlement.

