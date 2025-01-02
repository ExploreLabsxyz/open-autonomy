<a name="autonomy.cli.helpers.analyse"></a>
# autonomy.cli.helpers.analyse

Helpers for analyse command

<a name="autonomy.cli.helpers.analyse.load_package_tree"></a>
#### load`_`package`_`tree

```python
load_package_tree(packages_dir: Path) -> None
```

Load package tree.

<a name="autonomy.cli.helpers.analyse.list_all_skill_yaml_files"></a>
#### list`_`all`_`skill`_`yaml`_`files

```python
list_all_skill_yaml_files(registry_path: Path) -> List[Path]
```

List all skill yaml files in a local registry

<a name="autonomy.cli.helpers.analyse.run_dialogues_check"></a>
#### run`_`dialogues`_`check

```python
run_dialogues_check(packages_dir: Path, ignore: List[str], dialogues: List[str]) -> None
```

Run dialogues check.

<a name="autonomy.cli.helpers.analyse.ParseLogs"></a>
## ParseLogs Objects

```python
class ParseLogs()
```

Parse agent logs.

<a name="autonomy.cli.helpers.analyse.ParseLogs.__init__"></a>
#### `__`init`__`

```python
 | __init__() -> None
```

Initialize object.

<a name="autonomy.cli.helpers.analyse.ParseLogs.agents"></a>
#### agents

```python
 | @property
 | agents() -> List[str]
```

Available agents.

<a name="autonomy.cli.helpers.analyse.ParseLogs.n_agents"></a>
#### n`_`agents

```python
 | @property
 | n_agents() -> int
```

Available agents.

<a name="autonomy.cli.helpers.analyse.ParseLogs.from_dir"></a>
#### from`_`dir

```python
 | from_dir(logs_dir: Path) -> "ParseLogs"
```

From directory

<a name="autonomy.cli.helpers.analyse.ParseLogs.create_tables"></a>
#### create`_`tables

```python
 | create_tables(reset: bool = False) -> "ParseLogs"
```

Create required tables.

<a name="autonomy.cli.helpers.analyse.ParseLogs.select"></a>
#### select

```python
 | select(agents: List[str], start_time: Optional[datetime], end_time: Optional[datetime], log_level: Optional[str], period: Optional[int], round_name: Optional[str], behaviour_name: Optional[str]) -> "ParseLogs"
```

Query and return results.

<a name="autonomy.cli.helpers.analyse.ParseLogs.re_include"></a>
#### re`_`include

```python
 | re_include(regexes: List[str]) -> "ParseLogs"
```

Apply a set of regexes on the result.

<a name="autonomy.cli.helpers.analyse.ParseLogs.re_exclude"></a>
#### re`_`exclude

```python
 | re_exclude(regexes: List[str]) -> "ParseLogs"
```

Apply a set of regexes on the result.

<a name="autonomy.cli.helpers.analyse.ParseLogs.execution_path"></a>
#### execution`_`path

```python
 | execution_path() -> None
```

Output FSM path

<a name="autonomy.cli.helpers.analyse.ParseLogs.table"></a>
#### table

```python
 | table() -> None
```

Print table.

<a name="autonomy.cli.helpers.analyse.check_service_readiness"></a>
#### check`_`service`_`readiness

```python
check_service_readiness(token_id: Optional[int], public_id: Optional[PublicId], chain_type: ChainType, packages_dir: Path, skip_warnings: bool = False) -> None
```

Check deployment readiness of a service.

