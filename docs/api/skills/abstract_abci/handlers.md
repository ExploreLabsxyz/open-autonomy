<a name="packages.valory.skills.abstract_abci.handlers"></a>
# packages.valory.skills.abstract`_`abci.handlers

This module contains the handler for the 'abci' skill.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler"></a>
## ABCIHandler Objects

```python
class ABCIHandler(Handler)
```

Default ABCI handler.

This abstract skill provides a template of an ABCI application managed by an
AEA. This abstract Handler replies to ABCI requests with default responses.
In another skill, extend the class and override the request handlers
to implement a custom behaviour.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.setup"></a>
#### setup

```python
 | setup() -> None
```

Set up the handler.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.handle"></a>
#### handle

```python
 | handle(message: Message) -> None
```

Handle the message.

**Arguments**:

- `message`: the message.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.teardown"></a>
#### teardown

```python
 | teardown() -> None
```

Teardown the handler.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.log_exception"></a>
#### log`_`exception

```python
 | log_exception(message: AbciMessage, error_message: str) -> None
```

Log a response exception.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.echo"></a>
#### echo

```python
 | echo(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_ECHO performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.info"></a>
#### info

```python
 | info(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_INFO performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.flush"></a>
#### flush

```python
 | flush(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_FLUSH performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.set_option"></a>
#### set`_`option

```python
 | set_option(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_SET_OPTION performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.init_chain"></a>
#### init`_`chain

```python
 | init_chain(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_INIT_CHAIN performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.query"></a>
#### query

```python
 | query(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_QUERY performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.check_tx"></a>
#### check`_`tx

```python
 | check_tx(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_CHECK_TX performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.deliver_tx"></a>
#### deliver`_`tx

```python
 | deliver_tx(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_DELIVER_TX performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.begin_block"></a>
#### begin`_`block

```python
 | begin_block(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_BEGIN_BLOCK performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.end_block"></a>
#### end`_`block

```python
 | end_block(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_END_BLOCK performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.commit"></a>
#### commit

```python
 | commit(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_COMMIT performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.list_snapshots"></a>
#### list`_`snapshots

```python
 | list_snapshots(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_LIST_SNAPSHOT performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.offer_snapshot"></a>
#### offer`_`snapshot

```python
 | offer_snapshot(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_OFFER_SNAPSHOT performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.load_snapshot_chunk"></a>
#### load`_`snapshot`_`chunk

```python
 | load_snapshot_chunk(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_LOAD_SNAPSHOT_CHUNK performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

<a name="packages.valory.skills.abstract_abci.handlers.ABCIHandler.apply_snapshot_chunk"></a>
#### apply`_`snapshot`_`chunk

```python
 | apply_snapshot_chunk(message: AbciMessage, dialogue: AbciDialogue) -> AbciMessage
```

Handle a message of REQUEST_APPLY_SNAPSHOT_CHUNK performative.

**Arguments**:

- `message`: the ABCI request.
- `dialogue`: the ABCI dialogue.

**Returns**:

the response.

