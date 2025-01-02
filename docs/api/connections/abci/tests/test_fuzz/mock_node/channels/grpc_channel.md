<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel"></a>
# packages.valory.connections.abci.tests.test`_`fuzz.mock`_`node.channels.grpc`_`channel

GrpcChannel for MockNode

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel"></a>
## GrpcChannel Objects

```python
class GrpcChannel(BaseChannel)
```

Implements BaseChannel to use gRPC

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.__init__"></a>
#### `__`init`__`

```python
 | __init__(**kwargs: Dict) -> None
```

Initializes a GrpcChannel

:param: kwargs:
- host: the host of the ABCI app (localhost by default)
- port: the port of the ABCI app (26658 by default)

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_info"></a>
#### send`_`info

```python
 | send_info(request: abci_types.RequestInfo) -> abci_types.ResponseInfo
```

Sends an info request.

:param: request: RequestInfo pb object

**Returns**:

ResponseInfo pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_echo"></a>
#### send`_`echo

```python
 | send_echo(request: abci_types.RequestEcho) -> abci_types.ResponseEcho
```

Sends an echo request.

:param: request: RequestEcho pb object

**Returns**:

ResponseEcho pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_flush"></a>
#### send`_`flush

```python
 | send_flush(request: abci_types.RequestFlush) -> abci_types.ResponseFlush
```

Sends an flush request.

:param: request: RequestFlush pb object

**Returns**:

ResponseFlush pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_set_option"></a>
#### send`_`set`_`option

```python
 | send_set_option(request: abci_types.RequestSetOption) -> abci_types.ResponseSetOption
```

Sends an setOption request.

:param: request: RequestSetOption pb object

**Returns**:

ResponseSetOption pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_deliver_tx"></a>
#### send`_`deliver`_`tx

```python
 | send_deliver_tx(request: abci_types.RequestDeliverTx) -> abci_types.ResponseDeliverTx
```

Sends an deliverTx request.

:param: request: RequestDeliverTx pb object

**Returns**:

ResponseDeliverTx pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_check_tx"></a>
#### send`_`check`_`tx

```python
 | send_check_tx(request: abci_types.RequestCheckTx) -> abci_types.ResponseCheckTx
```

Sends an checkTx request.

:param: request: RequestCheckTx pb object

**Returns**:

ResponseCheckTx pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_query"></a>
#### send`_`query

```python
 | send_query(request: abci_types.RequestQuery) -> abci_types.ResponseQuery
```

Sends an query request.

:param: request: RequestQuery pb object

**Returns**:

ResponseQuery pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_commit"></a>
#### send`_`commit

```python
 | send_commit(request: abci_types.RequestCommit) -> abci_types.ResponseCommit
```

Sends an commit request.

:param: request: RequestCommit pb object

**Returns**:

ResponseCommit pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_init_chain"></a>
#### send`_`init`_`chain

```python
 | send_init_chain(request: abci_types.RequestInitChain) -> abci_types.ResponseInitChain
```

Sends an initChain request.

:param: request: RequestInitChain pb object

**Returns**:

ResponseInitChain pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_begin_block"></a>
#### send`_`begin`_`block

```python
 | send_begin_block(request: abci_types.RequestBeginBlock) -> abci_types.ResponseBeginBlock
```

Sends an beginBlock request.

:param: request: RequestBeginBlock pb object

**Returns**:

ResponseBeginBlock pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_end_block"></a>
#### send`_`end`_`block

```python
 | send_end_block(request: abci_types.RequestEndBlock) -> abci_types.ResponseEndBlock
```

Sends an endBlock request.

:param: request: RequestEndBlock pb object

**Returns**:

ResponseEndBlock pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_list_snapshots"></a>
#### send`_`list`_`snapshots

```python
 | send_list_snapshots(request: abci_types.RequestListSnapshots) -> abci_types.ResponseListSnapshots
```

Sends an listSnapshots request.

:param: request: RequestListSnapshots pb object

**Returns**:

ResponseListSnapshots pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_offer_snapshot"></a>
#### send`_`offer`_`snapshot

```python
 | send_offer_snapshot(request: abci_types.RequestOfferSnapshot) -> abci_types.ResponseOfferSnapshot
```

Sends an offerSnapshot request.

:param: request: RequestOfferSnapshot pb object

**Returns**:

ResponseOfferSnapshot pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_load_snapshot_chunk"></a>
#### send`_`load`_`snapshot`_`chunk

```python
 | send_load_snapshot_chunk(request: abci_types.RequestLoadSnapshotChunk) -> abci_types.ResponseLoadSnapshotChunk
```

Sends an loadSnapshotChunk request.

:param: request: RequestLoadSnapshotChunk pb object

**Returns**:

ResponseLoadSnapshotChunk pb object

<a name="packages.valory.connections.abci.tests.test_fuzz.mock_node.channels.grpc_channel.GrpcChannel.send_apply_snapshot_chunk"></a>
#### send`_`apply`_`snapshot`_`chunk

```python
 | send_apply_snapshot_chunk(request: abci_types.RequestApplySnapshotChunk) -> abci_types.ResponseApplySnapshotChunk
```

Sends an applySnapshotChunk request.

:param: request: RequestApplySnapshotChunk pb object

**Returns**:

ResponseApplySnapshotChunk pb object

