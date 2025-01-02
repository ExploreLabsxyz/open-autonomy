<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils"></a>
# plugins.aea-test-autonomy.aea`_`test`_`autonomy.helpers.tendermint`_`utils

Helpers for Tendermint.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintNodeInfo"></a>
## TendermintNodeInfo Objects

```python
class TendermintNodeInfo()
```

Data class to store Tendermint node info.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintNodeInfo.__init__"></a>
#### `__`init`__`

```python
 | __init__(node_id: str, abci_port: int, rpc_port: int, p2p_port: int, home: Path)
```

Initialize Tendermint node info.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintNodeInfo.rpc_laddr"></a>
#### rpc`_`laddr

```python
 | @property
 | rpc_laddr() -> str
```

Get ith rpc_laddr.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintNodeInfo.get_http_addr"></a>
#### get`_`http`_`addr

```python
 | get_http_addr(host: str) -> str
```

Get ith HTTP RCP address, given the host.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintNodeInfo.p2p_laddr"></a>
#### p2p`_`laddr

```python
 | @property
 | p2p_laddr() -> str
```

Get ith p2p_laddr.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintLocalNetworkBuilder"></a>
## TendermintLocalNetworkBuilder Objects

```python
class TendermintLocalNetworkBuilder()
```

Build a local Tendermint network.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintLocalNetworkBuilder.__init__"></a>
#### `__`init`__`

```python
 | __init__(nb_nodes: int, directory: Path, consensus_create_empty_blocks: bool = True) -> None
```

Initialize the builder.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintLocalNetworkBuilder.get_p2p_seeds"></a>
#### get`_`p2p`_`seeds

```python
 | get_p2p_seeds() -> List[str]
```

Get p2p seeds.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintLocalNetworkBuilder.get_command"></a>
#### get`_`command

```python
 | get_command(i: int) -> List[str]
```

Get command-line command for the ith process.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.TendermintLocalNetworkBuilder.http_rpc_laddrs"></a>
#### http`_`rpc`_`laddrs

```python
 | @property
 | http_rpc_laddrs() -> List[str]
```

Get HTTP RPC listening addresses.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.BaseTendermintTestClass"></a>
## BaseTendermintTestClass Objects

```python
class BaseTendermintTestClass()
```

MixIn class for Pytest classes.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.helpers.tendermint_utils.BaseTendermintTestClass.health_check"></a>
#### health`_`check

```python
 | @staticmethod
 | health_check(tendermint_net: TendermintLocalNetworkBuilder, **kwargs: Any) -> None
```

Do a health-check of the Tendermint network.

