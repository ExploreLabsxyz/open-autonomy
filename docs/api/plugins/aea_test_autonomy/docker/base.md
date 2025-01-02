<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base"></a>
# plugins.aea-test-autonomy.aea`_`test`_`autonomy.docker.base

This module contains testing utilities.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerImage"></a>
## DockerImage Objects

```python
class DockerImage(ABC)
```

A class to wrap interaction with a Docker image.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerImage.__init__"></a>
#### `__`init`__`

```python
 | __init__(client: docker.DockerClient)
```

Initialize.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerImage.check_skip"></a>
#### check`_`skip

```python
 | check_skip() -> None
```

Check whether the test should be skipped.

By default, nothing happens.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerImage.image"></a>
#### image

```python
 | @property
 | @abstractmethod
 | image() -> str
```

Return the image name.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerImage.stop_if_already_running"></a>
#### stop`_`if`_`already`_`running

```python
 | stop_if_already_running() -> None
```

Stop the running images with the same tag, if any.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerImage.create"></a>
#### create

```python
 | @abstractmethod
 | create() -> Container
```

Instantiate the image in a container.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerImage.create_many"></a>
#### create`_`many

```python
 | @abstractmethod
 | create_many(nb_containers: int) -> List[Container]
```

Instantiate the image in many containers, parametrized.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerImage.wait"></a>
#### wait

```python
 | @abstractmethod
 | wait(max_attempts: int = 15, sleep_rate: float = 1.0) -> bool
```

Wait until the image is running.

**Arguments**:

- `max_attempts`: max number of attempts.
- `sleep_rate`: the amount of time to sleep between different requests.

**Returns**:

True if the wait was successful, False otherwise.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.launch_image"></a>
#### launch`_`image

```python
launch_image(image: DockerImage, timeout: float = 2.0, max_attempts: int = 10) -> Generator[DockerImage, None, None]
```

Launch a single container.

**Arguments**:

- `image`: an instance of Docker image.
- `timeout`: timeout to launch
- `max_attempts`: max launch attempts
:yield: image

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.launch_many_containers"></a>
#### launch`_`many`_`containers

```python
launch_many_containers(image: DockerImage, nb_containers: int, timeout: float = 2.0, max_attempts: int = 10) -> Generator[DockerImage, None, None]
```

Launch many containers from an image.

**Arguments**:

- `image`: an instance of Docker image.
- `nb_containers`: the number of containers to launch from the image.
- `timeout`: timeout to launch
- `max_attempts`: max launch attempts
:yield: image

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerBaseTest"></a>
## DockerBaseTest Objects

```python
class DockerBaseTest(ABC)
```

Base pytest class for setting up Docker images.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerBaseTest.setup_class"></a>
#### setup`_`class

```python
 | @classmethod
 | setup_class(cls) -> None
```

Setup up the test class.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerBaseTest.teardown_class"></a>
#### teardown`_`class

```python
 | @classmethod
 | teardown_class(cls) -> None
```

Tear down the test.

<a name="plugins.aea-test-autonomy.aea_test_autonomy.docker.base.DockerBaseTest.setup_class_kwargs"></a>
#### setup`_`class`_`kwargs

```python
 | @classmethod
 | @abstractmethod
 | setup_class_kwargs(cls) -> Dict[str, Any]
```

Get kwargs for _setup_class call.

