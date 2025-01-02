<a name="autonomy.deploy.generators.localhost.tendermint.app"></a>
# autonomy.deploy.generators.localhost.tendermint.app

HTTP server to control the tendermint execution environment.

<a name="autonomy.deploy.generators.localhost.tendermint.app.load_genesis"></a>
#### load`_`genesis

```python
load_genesis() -> Any
```

Load genesis file.

<a name="autonomy.deploy.generators.localhost.tendermint.app.get_defaults"></a>
#### get`_`defaults

```python
get_defaults() -> Dict[str, str]
```

Get defaults from genesis file.

<a name="autonomy.deploy.generators.localhost.tendermint.app.override_config_toml"></a>
#### override`_`config`_`toml

```python
override_config_toml() -> None
```

Update sync method.

<a name="autonomy.deploy.generators.localhost.tendermint.app.update_peers"></a>
#### update`_`peers

```python
update_peers(validators: List[Dict], config_path: Path) -> None
```

Fix peers.

<a name="autonomy.deploy.generators.localhost.tendermint.app.update_external_address"></a>
#### update`_`external`_`address

```python
update_external_address(external_address: str, config_path: Path) -> None
```

Update the external address.

<a name="autonomy.deploy.generators.localhost.tendermint.app.update_genesis_config"></a>
#### update`_`genesis`_`config

```python
update_genesis_config(data: Dict) -> None
```

Update genesis.json file for the tendermint node.

<a name="autonomy.deploy.generators.localhost.tendermint.app.PeriodDumper"></a>
## PeriodDumper Objects

```python
class PeriodDumper()
```

Dumper for tendermint data.

<a name="autonomy.deploy.generators.localhost.tendermint.app.PeriodDumper.__init__"></a>
#### `__`init`__`

```python
 | __init__(logger: logging.Logger, dump_dir: Optional[Path] = None) -> None
```

Initialize object.

<a name="autonomy.deploy.generators.localhost.tendermint.app.PeriodDumper.readonly_handler"></a>
#### readonly`_`handler

```python
 | @staticmethod
 | readonly_handler(func: Callable, path: str, execinfo: Any) -> None
```

If permission is readonly, we change and retry.

<a name="autonomy.deploy.generators.localhost.tendermint.app.PeriodDumper.dump_period"></a>
#### dump`_`period

```python
 | dump_period() -> None
```

Dump tendermint run data for replay

<a name="autonomy.deploy.generators.localhost.tendermint.app.create_app"></a>
#### create`_`app

```python
create_app(dump_dir: Optional[Path] = None, debug: bool = False) -> Tuple[Flask, TendermintNode]
```

Create the Tendermint server app

<a name="autonomy.deploy.generators.localhost.tendermint.app.create_server"></a>
#### create`_`server

```python
create_server() -> Any
```

Function to retrieve just the app to be used by flask entry point.

