<a name="packages.valory.connections.abci.connection"></a>
# packages.valory.connections.abci.connection

Connection to interact with an ABCI server.

<a name="packages.valory.connections.abci.connection.DecodeVarintError"></a>
## DecodeVarintError Objects

```python
class DecodeVarintError(Exception)
```

This exception is raised when an error occurs while decoding a varint.

<a name="packages.valory.connections.abci.connection.EncodeVarintError"></a>
## EncodeVarintError Objects

```python
class EncodeVarintError(Exception)
```

This exception is raised when an error occurs while encoding a varint.

<a name="packages.valory.connections.abci.connection.TooLargeVarint"></a>
## TooLargeVarint Objects

```python
class TooLargeVarint(Exception)
```

This exception is raised when a message with varint exceeding the max size is received.

<a name="packages.valory.connections.abci.connection.TooLargeVarint.__init__"></a>
#### `__`init`__`

```python
 | __init__(received_size: int, max_size: int = MAX_READ_IN_BYTES)
```

Initialize the exception object.

**Arguments**:

- `received_size`: the received size.
- `max_size`: the maximum amount the connection supports.

<a name="packages.valory.connections.abci.connection.ShortBufferLengthError"></a>
## ShortBufferLengthError Objects

```python
class ShortBufferLengthError(Exception)
```

This exception is raised when the buffer length is shorter than expected.

<a name="packages.valory.connections.abci.connection.ShortBufferLengthError.__init__"></a>
#### `__`init`__`

```python
 | __init__(expected_length: int, data: bytes)
```

Initialize the exception object.

**Arguments**:

- `expected_length`: the expected length to be read
- `data`: the data actually read

<a name="packages.valory.connections.abci.connection._TendermintABCISerializer"></a>
## `_`TendermintABCISerializer Objects

```python
class _TendermintABCISerializer()
```

(stateless) utility class to encode/decode messages for the communication with Tendermint.

<a name="packages.valory.connections.abci.connection._TendermintABCISerializer.encode_varint"></a>
#### encode`_`varint

```python
 | @classmethod
 | encode_varint(cls, number: int) -> bytes
```

Encode a number in varint coding.

<a name="packages.valory.connections.abci.connection._TendermintABCISerializer.decode_varint"></a>
#### decode`_`varint

```python
 | @classmethod
 | async decode_varint(cls, buffer: asyncio.StreamReader, max_length: int = MAX_VARINT_BYTES) -> int
```

Decode a number from its varint coding.

**Arguments**:

- `buffer`: the buffer to read from.
- `max_length`: the max number of bytes that can be read.

**Returns**:

the decoded int.

:raise: DecodeVarintError if the varint could not be decoded.
:raise: EOFError if EOF byte is read and the process of decoding a varint has not started.

<a name="packages.valory.connections.abci.connection._TendermintABCISerializer.write_message"></a>
#### write`_`message

```python
 | @classmethod
 | write_message(cls, message: Response) -> bytes
```

Write a message in a buffer.

<a name="packages.valory.connections.abci.connection.VarintMessageReader"></a>
## VarintMessageReader Objects

```python
class VarintMessageReader()
```

Varint message reader.

<a name="packages.valory.connections.abci.connection.VarintMessageReader.__init__"></a>
#### `__`init`__`

```python
 | __init__(reader: asyncio.StreamReader) -> None
```

Initialize the reader.

<a name="packages.valory.connections.abci.connection.VarintMessageReader.read_next_message"></a>
#### read`_`next`_`message

```python
 | async read_next_message() -> bytes
```

Read next message.

<a name="packages.valory.connections.abci.connection.VarintMessageReader.read_until"></a>
#### read`_`until

```python
 | async read_until(n: int) -> bytes
```

Wait until n bytes are read from the stream.

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer"></a>
## ABCIApplicationServicer Objects

```python
class ABCIApplicationServicer(types_pb2_grpc.ABCIApplicationServicer)
```

Implements the gRPC servicer (handler)

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.__init__"></a>
#### `__`init`__`

```python
 | __init__(request_queue: asyncio.Queue, dialogues: AbciDialogues, target_skill: str)
```

Initializes the abci handler.

**Arguments**:

- `request_queue`: queue holding translated abci messages.
- `dialogues`: dialogues
- `target_skill`: target skill of messages

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.send"></a>
#### send

```python
 | async send(envelope: Envelope) -> Response
```

Returns response to the waiting request

:param: envelope: Envelope to be returned

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.Echo"></a>
#### Echo

```python
 | async Echo(request: RequestEcho, context: grpc.ServicerContext) -> ResponseEcho
```

Handles "Echo" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.Flush"></a>
#### Flush

```python
 | async Flush(request: RequestFlush, context: grpc.ServicerContext) -> ResponseFlush
```

Handles "Flush" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.Info"></a>
#### Info

```python
 | async Info(request: RequestInfo, context: grpc.ServicerContext) -> ResponseInfo
```

Handles "Info" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.SetOption"></a>
#### SetOption

```python
 | async SetOption(request: RequestSetOption, context: grpc.ServicerContext) -> ResponseSetOption
```

Handles "SetOption" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.DeliverTx"></a>
#### DeliverTx

```python
 | async DeliverTx(request: RequestDeliverTx, context: grpc.ServicerContext) -> ResponseDeliverTx
```

Handles "DeliverTx" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.CheckTx"></a>
#### CheckTx

```python
 | async CheckTx(request: RequestCheckTx, context: grpc.ServicerContext) -> ResponseCheckTx
```

Handles "CheckTx" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.Query"></a>
#### Query

```python
 | async Query(request: RequestQuery, context: grpc.ServicerContext) -> ResponseQuery
```

Handles "Query" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.Commit"></a>
#### Commit

```python
 | async Commit(request: RequestCommit, context: grpc.ServicerContext) -> ResponseCommit
```

Handles "Commit" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.InitChain"></a>
#### InitChain

```python
 | async InitChain(request: RequestInitChain, context: grpc.ServicerContext) -> ResponseInitChain
```

Handles "InitChain" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.BeginBlock"></a>
#### BeginBlock

```python
 | async BeginBlock(request: RequestBeginBlock, context: grpc.ServicerContext) -> ResponseBeginBlock
```

Handles "BeginBlock" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.EndBlock"></a>
#### EndBlock

```python
 | async EndBlock(request: RequestEndBlock, context: grpc.ServicerContext) -> ResponseEndBlock
```

Handles "EndBlock" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.ListSnapshots"></a>
#### ListSnapshots

```python
 | async ListSnapshots(request: RequestListSnapshots, context: grpc.ServicerContext) -> ResponseListSnapshots
```

Handles "ListSnapshots" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.OfferSnapshot"></a>
#### OfferSnapshot

```python
 | async OfferSnapshot(request: RequestOfferSnapshot, context: grpc.ServicerContext) -> ResponseOfferSnapshot
```

Handles "OfferSnapshot" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.LoadSnapshotChunk"></a>
#### LoadSnapshotChunk

```python
 | async LoadSnapshotChunk(request: RequestLoadSnapshotChunk, context: grpc.ServicerContext) -> ResponseLoadSnapshotChunk
```

Handles "LoadSnapshotChunk" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.ABCIApplicationServicer.ApplySnapshotChunk"></a>
#### ApplySnapshotChunk

```python
 | async ApplySnapshotChunk(request: RequestApplySnapshotChunk, context: grpc.ServicerContext) -> ResponseApplySnapshotChunk
```

Handles "ApplySnapshotChunk" gRPC requests

:param: request: The request from the Tendermint node
:param: context: The request context

**Returns**:

the Echo response

<a name="packages.valory.connections.abci.connection.GrpcServerChannel"></a>
## GrpcServerChannel Objects

```python
class GrpcServerChannel()
```

gRPC server channel to handle incoming communication from the Tendermint node.

<a name="packages.valory.connections.abci.connection.GrpcServerChannel.__init__"></a>
#### `__`init`__`

```python
 | __init__(target_skill_id: PublicId, address: str, port: int, logger: Optional[Logger] = None)
```

Initialize the gRPC server.

**Arguments**:

- `target_skill_id`: the public id of the target skill.
- `address`: the listen address.
- `port`: the port to listen from.
- `logger`: the logger.

<a name="packages.valory.connections.abci.connection.GrpcServerChannel.is_stopped"></a>
#### is`_`stopped

```python
 | @property
 | is_stopped() -> bool
```

Check that the channel is stopped.

<a name="packages.valory.connections.abci.connection.GrpcServerChannel.connect"></a>
#### connect

```python
 | async connect(loop: AbstractEventLoop) -> None
```

Connect.

**Arguments**:

- `loop`: asyncio event loop

<a name="packages.valory.connections.abci.connection.GrpcServerChannel.disconnect"></a>
#### disconnect

```python
 | async disconnect() -> None
```

Disconnect the channel

<a name="packages.valory.connections.abci.connection.GrpcServerChannel.get_message"></a>
#### get`_`message

```python
 | async get_message() -> Envelope
```

Get a message from the queue.

<a name="packages.valory.connections.abci.connection.GrpcServerChannel.send"></a>
#### send

```python
 | async send(envelope: Envelope) -> None
```

Send a message.

<a name="packages.valory.connections.abci.connection.TcpServerChannel"></a>
## TcpServerChannel Objects

```python
class TcpServerChannel()
```

TCP server channel to handle incoming communication from the Tendermint node.

<a name="packages.valory.connections.abci.connection.TcpServerChannel.__init__"></a>
#### `__`init`__`

```python
 | __init__(target_skill_id: PublicId, address: str, port: int, logger: Optional[Logger] = None)
```

Initialize the TCP server.

**Arguments**:

- `target_skill_id`: the public id of the target skill.
- `address`: the listen address.
- `port`: the port to listen from.
- `logger`: the logger.

<a name="packages.valory.connections.abci.connection.TcpServerChannel.is_stopped"></a>
#### is`_`stopped

```python
 | @property
 | is_stopped() -> bool
```

Check that the channel is stopped.

<a name="packages.valory.connections.abci.connection.TcpServerChannel.connect"></a>
#### connect

```python
 | async connect(loop: AbstractEventLoop) -> None
```

Connect.

Upon TCP Channel connection, start the TCP Server asynchronously.

**Arguments**:

- `loop`: asyncio event loop

<a name="packages.valory.connections.abci.connection.TcpServerChannel.disconnect"></a>
#### disconnect

```python
 | async disconnect() -> None
```

Disconnect the channel

<a name="packages.valory.connections.abci.connection.TcpServerChannel.receive_messages"></a>
#### receive`_`messages

```python
 | async receive_messages(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None
```

Receive incoming messages.

<a name="packages.valory.connections.abci.connection.TcpServerChannel.get_message"></a>
#### get`_`message

```python
 | async get_message() -> Envelope
```

Get a message from the queue.

<a name="packages.valory.connections.abci.connection.TcpServerChannel.send"></a>
#### send

```python
 | async send(envelope: Envelope) -> None
```

Send a message.

<a name="packages.valory.connections.abci.connection.StoppableThread"></a>
## StoppableThread Objects

```python
class StoppableThread(
    Thread)
```

Thread class with a stop() method.

<a name="packages.valory.connections.abci.connection.StoppableThread.__init__"></a>
#### `__`init`__`

```python
 | __init__(*args: Any, **kwargs: Any) -> None
```

Initialise the thread.

<a name="packages.valory.connections.abci.connection.StoppableThread.stop"></a>
#### stop

```python
 | stop() -> None
```

Set the stop event.

<a name="packages.valory.connections.abci.connection.StoppableThread.stopped"></a>
#### stopped

```python
 | stopped() -> bool
```

Check if the thread is stopped.

<a name="packages.valory.connections.abci.connection.TendermintParams"></a>
## TendermintParams Objects

```python
class TendermintParams()
```

Tendermint node parameters.

<a name="packages.valory.connections.abci.connection.TendermintParams.__init__"></a>
#### `__`init`__`

```python
 | __init__(proxy_app: str, rpc_laddr: str = DEFAULT_RPC_LISTEN_ADDRESS, p2p_laddr: str = DEFAULT_P2P_LISTEN_ADDRESS, p2p_seeds: Optional[List[str]] = None, consensus_create_empty_blocks: bool = True, home: Optional[str] = None, use_grpc: bool = False)
```

Initialize the parameters to the Tendermint node.

**Arguments**:

- `proxy_app`: ABCI address.
- `rpc_laddr`: RPC address.
- `p2p_laddr`: P2P address.
- `p2p_seeds`: P2P seeds.
- `consensus_create_empty_blocks`: if true, Tendermint node creates empty blocks.
- `home`: Tendermint's home directory.
- `use_grpc`: Whether to use a gRPC server, or TCP

<a name="packages.valory.connections.abci.connection.TendermintParams.__str__"></a>
#### `__`str`__`

```python
 | __str__() -> str
```

Get the string representation.

<a name="packages.valory.connections.abci.connection.TendermintParams.build_node_command"></a>
#### build`_`node`_`command

```python
 | build_node_command(debug: bool = False) -> List[str]
```

Build the 'node' command.

<a name="packages.valory.connections.abci.connection.TendermintParams.get_node_command_kwargs"></a>
#### get`_`node`_`command`_`kwargs

```python
 | @staticmethod
 | get_node_command_kwargs() -> Dict
```

Get the node command kwargs

<a name="packages.valory.connections.abci.connection.TendermintNode"></a>
## TendermintNode Objects

```python
class TendermintNode()
```

A class to manage a Tendermint node.

<a name="packages.valory.connections.abci.connection.TendermintNode.__init__"></a>
#### `__`init`__`

```python
 | __init__(params: TendermintParams, logger: Optional[Logger] = None, write_to_log: bool = False)
```

Initialize a Tendermint node.

**Arguments**:

- `params`: the parameters.
- `logger`: the logger.
- `write_to_log`: Write to log file.

<a name="packages.valory.connections.abci.connection.TendermintNode.init"></a>
#### init

```python
 | init() -> None
```

Initialize Tendermint node.

<a name="packages.valory.connections.abci.connection.TendermintNode.start"></a>
#### start

```python
 | start(debug: bool = False) -> None
```

Start a Tendermint node process.

<a name="packages.valory.connections.abci.connection.TendermintNode.stop"></a>
#### stop

```python
 | stop() -> None
```

Stop a Tendermint node process.

<a name="packages.valory.connections.abci.connection.TendermintNode.log"></a>
#### log

```python
 | log(line: str) -> None
```

Open and write a line to the log file.

<a name="packages.valory.connections.abci.connection.TendermintNode.prune_blocks"></a>
#### prune`_`blocks

```python
 | prune_blocks() -> int
```

Prune blocks from the Tendermint state

<a name="packages.valory.connections.abci.connection.TendermintNode.reset_genesis_file"></a>
#### reset`_`genesis`_`file

```python
 | reset_genesis_file(genesis_time: str, initial_height: str, period_count: str) -> None
```

Reset genesis file.

<a name="packages.valory.connections.abci.connection.ABCIServerConnection"></a>
## ABCIServerConnection Objects

```python
class ABCIServerConnection(Connection)
```

ABCI server.

<a name="packages.valory.connections.abci.connection.ABCIServerConnection.__init__"></a>
#### `__`init`__`

```python
 | __init__(**kwargs: Any) -> None
```

Initialize the connection.

**Arguments**:

- `kwargs`: keyword arguments passed to component base

<a name="packages.valory.connections.abci.connection.ABCIServerConnection.connect"></a>
#### connect

```python
 | async connect() -> None
```

Set up the connection.

In the implementation, remember to update 'connection_status' accordingly.

<a name="packages.valory.connections.abci.connection.ABCIServerConnection.disconnect"></a>
#### disconnect

```python
 | async disconnect() -> None
```

Tear down the connection.

In the implementation, remember to update 'connection_status' accordingly.

<a name="packages.valory.connections.abci.connection.ABCIServerConnection.send"></a>
#### send

```python
 | async send(envelope: Envelope) -> None
```

Send an envelope.

**Arguments**:

- `envelope`: the envelope to send.

<a name="packages.valory.connections.abci.connection.ABCIServerConnection.receive"></a>
#### receive

```python
 | async receive(*args: Any, **kwargs: Any) -> Optional[Envelope]
```

Receive an envelope. Blocking.

**Arguments**:

- `args`: arguments to receive
- `kwargs`: keyword arguments to receive

**Returns**:

the envelope received, if present.  # noqa: DAR202

