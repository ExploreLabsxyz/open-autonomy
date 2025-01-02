<a name="packages.valory.skills.abstract_round_abci.behaviour_utils"></a>
# packages.valory.skills.abstract`_`round`_`abci.behaviour`_`utils

This module contains helper classes for behaviours.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.SendException"></a>
## SendException Objects

```python
class SendException(Exception)
```

Exception raised if the 'try_send' to an AsyncBehaviour failed.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.TimeoutException"></a>
## TimeoutException Objects

```python
class TimeoutException(Exception)
```

Exception raised when a timeout during AsyncBehaviour occurs.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviourInternalError"></a>
## BaseBehaviourInternalError Objects

```python
class BaseBehaviourInternalError(Exception)
```

Internal error due to a bad implementation of the BaseBehaviour.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviourInternalError.__init__"></a>
#### `__`init`__`

```python
 | __init__(message: str, *args: Any) -> None
```

Initialize the error object.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour"></a>
## AsyncBehaviour Objects

```python
class AsyncBehaviour(ABC)
```

MixIn behaviour class that support limited asynchronous programming.

An AsyncBehaviour can be in three states:
- READY: no suspended 'async_act' execution;
- RUNNING: 'act' called, and waiting for a message
- WAITING_TICK: 'act' called, and waiting for the next 'act' call

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.AsyncState"></a>
## AsyncState Objects

```python
class AsyncState(Enum)
```

Enumeration of AsyncBehaviour states.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.__init__"></a>
#### `__`init`__`

```python
 | __init__() -> None
```

Initialize the async behaviour.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.async_act"></a>
#### async`_`act

```python
 | @abstractmethod
 | async_act() -> Generator
```

Do the act, supporting asynchronous execution.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.async_act_wrapper"></a>
#### async`_`act`_`wrapper

```python
 | @abstractmethod
 | async_act_wrapper() -> Generator
```

Do the act, supporting asynchronous execution.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.state"></a>
#### state

```python
 | @property
 | state() -> AsyncState
```

Get the 'async state'.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.is_notified"></a>
#### is`_`notified

```python
 | @property
 | is_notified() -> bool
```

Returns whether the behaviour has been notified about the arrival of a message.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.received_message"></a>
#### received`_`message

```python
 | @property
 | received_message() -> Any
```

Returns the message the behaviour has received. "__message" should be None if not availble or already consumed.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.is_stopped"></a>
#### is`_`stopped

```python
 | @property
 | is_stopped() -> bool
```

Check whether the behaviour has stopped.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.try_send"></a>
#### try`_`send

```python
 | try_send(message: Any) -> None
```

Try to send a message to a waiting behaviour.

It will be sent only if the behaviour is actually waiting for a message,
and it was not already notified.

**Arguments**:

- `message`: a Python object.
:raises: SendException if the behaviour was not waiting for a message,
or if it was already notified.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.wait_for_condition"></a>
#### wait`_`for`_`condition

```python
 | @classmethod
 | wait_for_condition(cls, condition: Callable[[], bool], timeout: Optional[float] = None) -> Generator[None, None, None]
```

Wait for a condition to happen.

This is a local method that does not depend on the global clock,
so the usage of datetime.now() is acceptable here.

**Arguments**:

- `condition`: the condition to wait for
- `timeout`: the maximum amount of time to wait
:yield: None

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.sleep"></a>
#### sleep

```python
 | sleep(seconds: float) -> Any
```

Delay execution for a given number of seconds.

The argument may be a floating point number for subsecond precision.
This is a local method that does not depend on the global clock, so the
usage of datetime.now() is acceptable here.

**Arguments**:

- `seconds`: the seconds
:yield: None

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.wait_for_message"></a>
#### wait`_`for`_`message

```python
 | wait_for_message(condition: Callable = lambda message: True, timeout: Optional[float] = None) -> Any
```

Wait for message.

Care must be taken. This method does not handle concurrent requests.
Use directly after a request is being sent.
This is a local method that does not depend on the global clock,
so the usage of datetime.now() is acceptable here.

**Arguments**:

- `condition`: a callable
- `timeout`: max time to wait (in seconds)

**Returns**:

a message
:yield: None

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.setup"></a>
#### setup

```python
 | setup() -> None
```

Setup behaviour.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.act"></a>
#### act

```python
 | act() -> None
```

Do the act.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.AsyncBehaviour.stop"></a>
#### stop

```python
 | stop() -> None
```

Stop the execution of the behaviour.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.IPFSBehaviour"></a>
## IPFSBehaviour Objects

```python
class IPFSBehaviour(SimpleBehaviour,  ABC)
```

Behaviour for interactions with IPFS.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.IPFSBehaviour.__init__"></a>
#### `__`init`__`

```python
 | __init__(**kwargs: Any)
```

Initialize an `IPFSBehaviour`.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.CleanUpBehaviour"></a>
## CleanUpBehaviour Objects

```python
class CleanUpBehaviour(SimpleBehaviour,  ABC)
```

Class for clean-up related functionality of behaviours.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.CleanUpBehaviour.__init__"></a>
#### `__`init`__`

```python
 | __init__(**kwargs: Any)
```

Initialize a base behaviour.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.CleanUpBehaviour.clean_up"></a>
#### clean`_`up

```python
 | clean_up() -> None
```

Clean up the resources due to a 'stop' event.

It can be optionally implemented by the concrete classes.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.CleanUpBehaviour.handle_late_messages"></a>
#### handle`_`late`_`messages

```python
 | handle_late_messages(behaviour_id: str, message: Message) -> None
```

Handle late arriving messages.

Runs from another behaviour, even if the behaviour implementing the method has been exited.
It can be optionally implemented by the concrete classes.

**Arguments**:

- `behaviour_id`: the id of the behaviour in which the message belongs to.
- `message`: the late arriving message to handle.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.RPCResponseStatus"></a>
## RPCResponseStatus Objects

```python
class RPCResponseStatus(Enum)
```

A custom status of an RPC response.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils._MetaBaseBehaviour"></a>
## `_`MetaBaseBehaviour Objects

```python
class _MetaBaseBehaviour(ABCMeta)
```

A metaclass that validates BaseBehaviour's attributes.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils._MetaBaseBehaviour.__new__"></a>
#### `__`new`__`

```python
 | __new__(mcs, name: str, bases: Tuple, namespace: Dict, **kwargs: Any) -> Type
```

Initialize the class.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour"></a>
## BaseBehaviour Objects

```python
class BaseBehaviour(
    AsyncBehaviour,  IPFSBehaviour,  CleanUpBehaviour,  ABC, metaclass=_MetaBaseBehaviour)
```

This class represents the base class for FSM behaviours

A behaviour is a state of the FSM App execution. It usually involves
interactions between participants in the FSM App,
although this is not enforced at this level of abstraction.

Concrete classes must set:
- matching_round: the round class matching the behaviour;

Optionally, behaviour_id can be defined, although it is recommended to use the autogenerated id.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.__init__"></a>
#### `__`init`__`

```python
 | __init__(**kwargs: Any)
```

Initialize a base behaviour.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.auto_behaviour_id"></a>
#### auto`_`behaviour`_`id

```python
 | @classmethod
 | auto_behaviour_id(cls) -> str
```

Get behaviour id automatically.

This method returns the auto generated id from the class name if the
class variable behaviour_id is not set on the child class.
Otherwise, it returns the class variable behaviour_id.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.behaviour_id"></a>
#### behaviour`_`id

```python
 | @property
 | behaviour_id() -> str
```

Get behaviour id.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.params"></a>
#### params

```python
 | @property
 | params() -> BaseParams
```

Return the params.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.shared_state"></a>
#### shared`_`state

```python
 | @property
 | shared_state() -> SharedState
```

Return the round sequence.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.round_sequence"></a>
#### round`_`sequence

```python
 | @property
 | round_sequence() -> RoundSequence
```

Return the round sequence.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.synchronized_data"></a>
#### synchronized`_`data

```python
 | @property
 | synchronized_data() -> BaseSynchronizedData
```

Return the synchronized data.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.tm_communication_unhealthy"></a>
#### tm`_`communication`_`unhealthy

```python
 | @property
 | tm_communication_unhealthy() -> bool
```

Return if the Tendermint communication is not healthy anymore.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.check_in_round"></a>
#### check`_`in`_`round

```python
 | check_in_round(round_id: str) -> bool
```

Check that we entered a specific round.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.check_in_last_round"></a>
#### check`_`in`_`last`_`round

```python
 | check_in_last_round(round_id: str) -> bool
```

Check that we entered a specific round.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.check_not_in_round"></a>
#### check`_`not`_`in`_`round

```python
 | check_not_in_round(round_id: str) -> bool
```

Check that we are not in a specific round.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.check_not_in_last_round"></a>
#### check`_`not`_`in`_`last`_`round

```python
 | check_not_in_last_round(round_id: str) -> bool
```

Check that we are not in a specific round.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.check_round_has_finished"></a>
#### check`_`round`_`has`_`finished

```python
 | check_round_has_finished(round_id: str) -> bool
```

Check that the round has finished.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.check_round_height_has_changed"></a>
#### check`_`round`_`height`_`has`_`changed

```python
 | check_round_height_has_changed(round_height: int) -> bool
```

Check that the round height has changed.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.is_round_ended"></a>
#### is`_`round`_`ended

```python
 | is_round_ended(round_id: str) -> Callable[[], bool]
```

Get a callable to check whether the current round has ended.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.wait_until_round_end"></a>
#### wait`_`until`_`round`_`end

```python
 | wait_until_round_end(timeout: Optional[float] = None) -> Generator[None, None, None]
```

Wait until the ABCI application exits from a round.

**Arguments**:

- `timeout`: the timeout for the wait
:yield: None

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.wait_from_last_timestamp"></a>
#### wait`_`from`_`last`_`timestamp

```python
 | wait_from_last_timestamp(seconds: float) -> Any
```

Delay execution for a given number of seconds from the last timestamp.

The argument may be a floating point number for subsecond precision.
This is a local method that does not depend on the global clock,
so the usage of datetime.now() is acceptable here.

**Arguments**:

- `seconds`: the seconds
:yield: None

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.is_done"></a>
#### is`_`done

```python
 | is_done() -> bool
```

Check whether the behaviour is done.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.set_done"></a>
#### set`_`done

```python
 | set_done() -> None
```

Set the behaviour to done.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.send_a2a_transaction"></a>
#### send`_`a2a`_`transaction

```python
 | send_a2a_transaction(payload: BaseTxPayload, resetting: bool = False) -> Generator
```

Send transaction and wait for the response, and repeat until not successful.

:param: payload: the payload to send
:param: resetting: flag indicating if we are resetting Tendermint nodes in this round.
:yield: the responses

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.async_act_wrapper"></a>
#### async`_`act`_`wrapper

```python
 | async_act_wrapper() -> Generator
```

Do the act, supporting asynchronous execution.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.num_active_peers"></a>
#### num`_`active`_`peers

```python
 | num_active_peers(timeout: Optional[float] = None) -> Generator[None, None, Optional[int]]
```

Returns the number of active peers in the network.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.get_callback_request"></a>
#### get`_`callback`_`request

```python
 | get_callback_request() -> Callable[[Message, "BaseBehaviour"], None]
```

Wrapper for callback request which depends on whether the message has not been handled on time.

**Returns**:

the request callback.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.get_http_response"></a>
#### get`_`http`_`response

```python
 | get_http_response(method: str, url: str, content: Optional[bytes] = None, headers: Optional[Dict[str, str]] = None, parameters: Optional[Dict[str, str]] = None) -> Generator[None, None, HttpMessage]
```

Send an http request message from the skill context.

This method is skill-specific, and therefore
should not be used elsewhere.

Happy-path full flow of the messages.

_do_request:
AbstractRoundAbci skill -> (HttpMessage | REQUEST) -> Http client connection
Http client connection -> (HttpMessage | RESPONSE) -> AbstractRoundAbci skill

**Arguments**:

- `method`: the http request method (i.e. 'GET' or 'POST').
- `url`: the url to send the message to.
- `content`: the payload.
- `headers`: headers to be included.
- `parameters`: url query parameters.
:yield: HttpMessage object

**Returns**:

the http message and the http dialogue

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.get_signature"></a>
#### get`_`signature

```python
 | get_signature(message: bytes, is_deprecated_mode: bool = False) -> Generator[None, None, str]
```

Get signature for message.

Happy-path full flow of the messages.

_send_signing_request:
AbstractRoundAbci skill -> (SigningMessage | SIGN_MESSAGE) -> DecisionMaker
DecisionMaker -> (SigningMessage | SIGNED_MESSAGE) -> AbstractRoundAbci skill

**Arguments**:

- `message`: message bytes
- `is_deprecated_mode`: is deprecated mode flag
:yield: SigningMessage object

**Returns**:

message signature

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.send_raw_transaction"></a>
#### send`_`raw`_`transaction

```python
 | send_raw_transaction(transaction: RawTransaction, use_flashbots: bool = False, target_block_numbers: Optional[List[int]] = None, raise_on_failed_simulation: bool = False, chain_id: Optional[str] = None) -> Generator[
 |         None,
 |         Union[None, SigningMessage, LedgerApiMessage],
 |         Tuple[Optional[str], RPCResponseStatus],
 |     ]
```

Send raw transactions to the ledger for mining.

Happy-path full flow of the messages.

_send_transaction_signing_request:
AbstractRoundAbci skill -> (SigningMessage | SIGN_TRANSACTION) -> DecisionMaker
DecisionMaker -> (SigningMessage | SIGNED_TRANSACTION) -> AbstractRoundAbci skill

_send_transaction_request:
AbstractRoundAbci skill -> (LedgerApiMessage | SEND_SIGNED_TRANSACTION) -> Ledger connection
Ledger connection -> (LedgerApiMessage | TRANSACTION_DIGEST) -> AbstractRoundAbci skill

**Arguments**:

- `transaction`: transaction data
- `use_flashbots`: whether to use flashbots for the transaction or not
- `target_block_numbers`: the target block numbers in case we are using flashbots
- `raise_on_failed_simulation`: whether to raise an exception if the transaction fails the simulation or not
- `chain_id`: the chain name to use for the ledger call
:yield: SigningMessage object

**Returns**:

transaction hash

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.get_transaction_receipt"></a>
#### get`_`transaction`_`receipt

```python
 | get_transaction_receipt(tx_digest: str, retry_timeout: Optional[int] = None, retry_attempts: Optional[int] = None, chain_id: Optional[str] = None) -> Generator[None, None, Optional[Dict]]
```

Get transaction receipt.

Happy-path full flow of the messages.

_send_transaction_receipt_request:
AbstractRoundAbci skill -> (LedgerApiMessage | GET_TRANSACTION_RECEIPT) -> Ledger connection
Ledger connection -> (LedgerApiMessage | TRANSACTION_RECEIPT) -> AbstractRoundAbci skill

**Arguments**:

- `tx_digest`: transaction digest received from raw transaction.
- `retry_timeout`: retry timeout.
- `retry_attempts`: number of retry attempts allowed.
:yield: LedgerApiMessage object

**Returns**:

transaction receipt data

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.get_ledger_api_response"></a>
#### get`_`ledger`_`api`_`response

```python
 | get_ledger_api_response(performative: LedgerApiMessage.Performative, ledger_callable: str, **kwargs: Any, ,) -> Generator[None, None, LedgerApiMessage]
```

Request data from ledger api

Happy-path full flow of the messages.

AbstractRoundAbci skill -> (LedgerApiMessage | LedgerApiMessage.Performative) -> Ledger connection
Ledger connection -> (LedgerApiMessage | LedgerApiMessage.Performative) -> AbstractRoundAbci skill

**Arguments**:

- `performative`: the message performative
- `ledger_callable`: the callable to call on the contract
- `kwargs`: keyword argument for the contract api request

**Returns**:

the contract api response
:yields: the contract api response

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.get_contract_api_response"></a>
#### get`_`contract`_`api`_`response

```python
 | get_contract_api_response(performative: ContractApiMessage.Performative, contract_address: Optional[str], contract_id: str, contract_callable: str, ledger_id: Optional[str] = None, **kwargs: Any, ,) -> Generator[None, None, ContractApiMessage]
```

Request contract safe transaction hash

Happy-path full flow of the messages.

AbstractRoundAbci skill -> (ContractApiMessage | ContractApiMessage.Performative) -> Ledger connection (contract dispatcher)
Ledger connection (contract dispatcher) -> (ContractApiMessage | ContractApiMessage.Performative) -> AbstractRoundAbci skill

**Arguments**:

- `performative`: the message performative
- `contract_address`: the contract address
- `contract_id`: the contract id
- `contract_callable`: the callable to call on the contract
- `ledger_id`: the ledger id, if not specified, the default ledger id is used
- `kwargs`: keyword argument for the contract api request

**Returns**:

the contract api response
:yields: the contract api response

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.request_recovery_params"></a>
#### request`_`recovery`_`params

```python
 | request_recovery_params(should_log: bool) -> Generator[None, None, bool]
```

Request the Tendermint recovery parameters from the other agents via the ACN.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.hard_reset_sleep"></a>
#### hard`_`reset`_`sleep

```python
 | @property
 | hard_reset_sleep() -> float
```

Amount of time to sleep before and after performing a hard reset.

We sleep for half the reset pause duration as there are no immediate transactions on either side of the reset.

**Returns**:

the amount of time to sleep in seconds

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.reset_tendermint_with_wait"></a>
#### reset`_`tendermint`_`with`_`wait

```python
 | reset_tendermint_with_wait(on_startup: bool = False, is_recovery: bool = False) -> Generator[None, None, bool]
```

Performs a hard reset (unsafe-reset-all) on the tendermint node.

**Arguments**:

- `on_startup`: whether we are resetting on the start of the agent.
- `is_recovery`: whether the reset is being performed to recover the agent <-> tm communication.
:yields: None

**Returns**:

whether the reset was successful.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.send_to_ipfs"></a>
#### send`_`to`_`ipfs

```python
 | send_to_ipfs(filename: str, obj: SupportedObjectType, multiple: bool = False, filetype: Optional[SupportedFiletype] = None, custom_storer: Optional[CustomStorerType] = None, timeout: Optional[float] = None, **kwargs: Any, ,) -> Generator[None, None, Optional[str]]
```

Store an object on IPFS.

**Arguments**:

- `filename`: the file name to store obj in. If "multiple" is True, filename will be the name of the dir.
- `obj`: the object(s) to serialize and store in IPFS as "filename".
- `multiple`: whether obj should be stored as multiple files, i.e. directory.
- `filetype`: the file type of the object being downloaded.
- `custom_storer`: a custom serializer for "obj".
- `timeout`: timeout for the request.

**Returns**:

the downloaded object, corresponding to ipfs_hash.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.BaseBehaviour.get_from_ipfs"></a>
#### get`_`from`_`ipfs

```python
 | get_from_ipfs(ipfs_hash: str, filetype: Optional[SupportedFiletype] = None, custom_loader: CustomLoaderType = None, timeout: Optional[float] = None) -> Generator[None, None, Optional[SupportedObjectType]]
```

Gets an object from IPFS.

**Arguments**:

- `ipfs_hash`: the ipfs hash of the file/dir to download.
- `filetype`: the file type of the object being downloaded.
- `custom_loader`: a custom deserializer for the object received from IPFS.
- `timeout`: timeout for the request.

**Returns**:

the downloaded object, corresponding to ipfs_hash.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.TmManager"></a>
## TmManager Objects

```python
class TmManager(BaseBehaviour)
```

Util class to be used for managing the tendermint node.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.TmManager.__init__"></a>
#### `__`init`__`

```python
 | __init__(**kwargs: Any)
```

Initialize the `TmManager`.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.TmManager.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

The behaviour act.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.TmManager.is_acting"></a>
#### is`_`acting

```python
 | @property
 | is_acting() -> bool
```

This method returns whether there is an active fix being applied.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.TmManager.hard_reset_sleep"></a>
#### hard`_`reset`_`sleep

```python
 | @property
 | hard_reset_sleep() -> float
```

Amount of time to sleep before and after performing a hard reset.

We don't need to wait for half the reset pause duration, like in normal cases where we perform a hard reset.

**Returns**:

the amount of time to sleep in seconds

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.TmManager.get_callback_request"></a>
#### get`_`callback`_`request

```python
 | get_callback_request() -> Callable[[Message, "BaseBehaviour"], None]
```

Wrapper for callback_request(), overridden to remove checks not applicable to TmManager.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.TmManager.try_fix"></a>
#### try`_`fix

```python
 | try_fix() -> None
```

This method tries to fix an unhealthy tendermint node.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.DegenerateBehaviour"></a>
## DegenerateBehaviour Objects

```python
class DegenerateBehaviour(BaseBehaviour,  ABC)
```

An abstract matching behaviour for final and degenerate rounds.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.DegenerateBehaviour.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Exit the agent with error when a degenerate round is reached.

<a name="packages.valory.skills.abstract_round_abci.behaviour_utils.make_degenerate_behaviour"></a>
#### make`_`degenerate`_`behaviour

```python
make_degenerate_behaviour(round_cls: Type[AbstractRound]) -> Type[DegenerateBehaviour]
```

Make a degenerate behaviour class.

