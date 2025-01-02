<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.acn_node"></a>
# plugins.aea-test-autonomy.aea`_`test`_`autonomy.docker.acn`_`node

ACN Docker Image.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.acn_node.ACNNodeDockerImage"></a>
## ACNNodeDockerImage Objects

```python
class ACNNodeDockerImage(DockerImage)
```

Wrapper to ACNNode Docker image.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.acn_node.ACNNodeDockerImage.__init__"></a>
#### `__`init`__`

```python
 | __init__(client: DockerClient, config: Optional[Dict] = None)
```

Initialize the ACNNode Docker image.

**Arguments**:

- `client`: the Docker client.
- `config`: optional configuration to command line.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.acn_node.ACNNodeDockerImage.image"></a>
#### image

```python
 | @property
 | image() -> str
```

Get the image name.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.acn_node.ACNNodeDockerImage.create"></a>
#### create

```python
 | create() -> Container
```

Create the container.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.acn_node.ACNNodeDockerImage.create_many"></a>
#### create`_`many

```python
 | create_many(nb_containers: int) -> List[Container]
```

Instantiate the image in many containers, parametrized.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.acn_node.ACNNodeDockerImage.wait"></a>
#### wait

```python
 | wait(max_attempts: int = 15, sleep_rate: float = 1.0) -> bool
```

Wait until the image is up.

