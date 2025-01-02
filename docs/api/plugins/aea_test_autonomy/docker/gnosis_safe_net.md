<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.gnosis_safe_net"></a>
# plugins.aea-test-autonomy.aea`_`test`_`autonomy.docker.gnosis`_`safe`_`net

Tendermint Docker image.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.gnosis_safe_net.GnosisSafeNetDockerImage"></a>
## GnosisSafeNetDockerImage Objects

```python
class GnosisSafeNetDockerImage(DockerImage)
```

Spawn a local Ethereum network with deployed Gnosis Safe contracts, using HardHat.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.gnosis_safe_net.GnosisSafeNetDockerImage.__init__"></a>
#### `__`init`__`

```python
 | __init__(client: docker.DockerClient, addr: str = DEFAULT_HARDHAT_ADDR, port: int = DEFAULT_HARDHAT_PORT)
```

Initialize.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.gnosis_safe_net.GnosisSafeNetDockerImage.image"></a>
#### image

```python
 | @property
 | image() -> str
```

Get the image name.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.gnosis_safe_net.GnosisSafeNetDockerImage.create"></a>
#### create

```python
 | create() -> Container
```

Create the container.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.gnosis_safe_net.GnosisSafeNetDockerImage.create_many"></a>
#### create`_`many

```python
 | create_many(nb_containers: int) -> List[Container]
```

Instantiate the image in many containers, parametrized.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.gnosis_safe_net.GnosisSafeNetDockerImage.wait"></a>
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

