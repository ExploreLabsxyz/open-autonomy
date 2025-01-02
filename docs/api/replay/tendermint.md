<a name="autonomy.replay.tendermint"></a>
# autonomy.replay.tendermint

Script to build and run tendermint nodes from data dumps.

<a name="autonomy.replay.tendermint.RanOutOfDumpsToReplay"></a>
## RanOutOfDumpsToReplay Objects

```python
class RanOutOfDumpsToReplay(Exception)
```

Error to raise when we run out of dumps to replay.

<a name="autonomy.replay.tendermint.TendermintRunner"></a>
## TendermintRunner Objects

```python
class TendermintRunner()
```

Run tednermint using the dump.

<a name="autonomy.replay.tendermint.TendermintRunner.__init__"></a>
#### `__`init`__`

```python
 | __init__(node_id: int, dump_dir: Path, n_periods: int) -> None
```

Initialize object.

<a name="autonomy.replay.tendermint.TendermintRunner.update_period"></a>
#### update`_`period

```python
 | update_period() -> None
```

Update period.

<a name="autonomy.replay.tendermint.TendermintRunner.get_last_block_height"></a>
#### get`_`last`_`block`_`height

```python
 | get_last_block_height() -> int
```

Returns the last block height before dumping.

<a name="autonomy.replay.tendermint.TendermintRunner.start"></a>
#### start

```python
 | start() -> None
```

Start tendermint process.

<a name="autonomy.replay.tendermint.TendermintRunner.stop"></a>
#### stop

```python
 | stop() -> None
```

Stop tendermint process.

<a name="autonomy.replay.tendermint.TendermintNetwork"></a>
## TendermintNetwork Objects

```python
class TendermintNetwork()
```

Tendermint network.

<a name="autonomy.replay.tendermint.TendermintNetwork.init"></a>
#### init

```python
 | init(dump_dir: Path) -> None
```

Initialize object.

<a name="autonomy.replay.tendermint.TendermintNetwork.update_period"></a>
#### update`_`period

```python
 | update_period(node_id: int) -> None
```

Update period for nth node.

<a name="autonomy.replay.tendermint.TendermintNetwork.get_last_block_height"></a>
#### get`_`last`_`block`_`height

```python
 | get_last_block_height(node_id: int) -> int
```

Returns last block height before dumping for `node_id`

<a name="autonomy.replay.tendermint.TendermintNetwork.stop_node"></a>
#### stop`_`node

```python
 | stop_node(node_id: int) -> None
```

Stop a specific node.

<a name="autonomy.replay.tendermint.TendermintNetwork.start"></a>
#### start

```python
 | start() -> None
```

Start networks.

<a name="autonomy.replay.tendermint.TendermintNetwork.stop"></a>
#### stop

```python
 | stop() -> None
```

Stop network.

<a name="autonomy.replay.tendermint.TendermintNetwork.run_until_interruption"></a>
#### run`_`until`_`interruption

```python
 | run_until_interruption() -> None
```

Run network until interruption.

<a name="autonomy.replay.tendermint.build_tendermint_apps"></a>
#### build`_`tendermint`_`apps

```python
build_tendermint_apps() -> Tuple[Flask, TendermintNetwork]
```

Build flask app and tendermint network.

