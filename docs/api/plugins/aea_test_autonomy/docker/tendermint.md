<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint"></a>
# plugins.aea-test-autonomy.aea`_`test`_`autonomy.docker.tendermint

Tendermint Docker image.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.TendermintDockerImage"></a>
## TendermintDockerImage Objects

```python
class TendermintDockerImage(DockerImage)
```

Tendermint Docker image.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.TendermintDockerImage.__init__"></a>
#### `__`init`__`

```python
 | __init__(client: docker.DockerClient, abci_host: str = DEFAULT_ABCI_HOST, abci_port: int = DEFAULT_ABCI_PORT, port: int = DEFAULT_TENDERMINT_PORT, p2p_port: int = DEFAULT_P2P_PORT, com_port: int = DEFAULT_TENDERMINT_COM_PORT)
```

Initialize.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.TendermintDockerImage.image"></a>
#### image

```python
 | @property
 | image() -> str
```

Get the image name.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.TendermintDockerImage.create"></a>
#### create

```python
 | create() -> Container
```

Create the container.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.TendermintDockerImage.create_many"></a>
#### create`_`many

```python
 | create_many(nb_containers: int) -> List[Container]
```

Instantiate the image in many containers, parametrized.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.TendermintDockerImage.wait"></a>
#### wait

```python
 | wait(max_attempts: int = 15, sleep_rate: float = 1.0) -> bool
```

Wait until the image is running.

**Arguments**:

- `max_attempts`: max number of attempts.
- `sleep_rate`: the amount of time to sleep between different requests.

**Returns**:

True if the wait was successful, False otherwise.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage"></a>
## FlaskTendermintDockerImage Objects

```python
class FlaskTendermintDockerImage(TendermintDockerImage)
```

Flask app with Tendermint Docker image.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.__init__"></a>
#### `__`init`__`

```python
 | __init__(client: docker.DockerClient, abci_host: str = DEFAULT_ABCI_HOST, abci_port: int = DEFAULT_ABCI_PORT, port: int = DEFAULT_TENDERMINT_PORT, p2p_port: int = DEFAULT_P2P_PORT, com_port: int = DEFAULT_TENDERMINT_COM_PORT + 2)
```

Initialize.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.image"></a>
#### image

```python
 | @property
 | image() -> str
```

Get the image name.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.get_node_name"></a>
#### get`_`node`_`name

```python
 | @staticmethod
 | get_node_name(i: int) -> str
```

Get the ith node's name.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.get_port"></a>
#### get`_`port

```python
 | get_port(i: int) -> int
```

Get the ith port.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.get_com_port"></a>
#### get`_`com`_`port

```python
 | get_com_port(i: int) -> int
```

Get the ith com port.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.get_p2p_port"></a>
#### get`_`p2p`_`port

```python
 | get_p2p_port(i: int) -> int
```

Get the ith p2p port.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.get_abci_port"></a>
#### get`_`abci`_`port

```python
 | get_abci_port(i: int) -> int
```

Get the ith abci port.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.get_addr"></a>
#### get`_`addr

```python
 | get_addr(prefix: str, i: int, p2p: bool = False) -> str
```

Get a node's address.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.p2p_seeds"></a>
#### p2p`_`seeds

```python
 | @property
 | p2p_seeds() -> List[str]
```

Get p2p seeds.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.create_many"></a>
#### create`_`many

```python
 | create_many(nb_containers: int) -> List[Container]
```

Create a list of node containers.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.health_check"></a>
#### health`_`check

```python
 | health_check(**kwargs: Any) -> None
```

Do a health-check of the Tendermint network.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.tendermint.FlaskTendermintDockerImage.cleanup"></a>
#### cleanup

```python
 | @staticmethod
 | cleanup(nb_containers: int) -> None
```

Cleanup dangling containers.

