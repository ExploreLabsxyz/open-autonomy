<a name="autonomy.analyse.logs.collection"></a>
# autonomy.analyse.logs.collection

Log streams

<a name="autonomy.analyse.logs.collection.LogCollection"></a>
## LogCollection Objects

```python
class LogCollection(ABC)
```

Collection of logs.

<a name="autonomy.analyse.logs.collection.LogCollection.__init__"></a>
#### `__`init`__`

```python
 | __init__() -> None
```

Initialize object.

<a name="autonomy.analyse.logs.collection.LogCollection.get_avilable_agents"></a>
#### get`_`avilable`_`agents

```python
 | @abstractmethod
 | get_avilable_agents() -> List[str]
```

Returns a list of agent names.

<a name="autonomy.analyse.logs.collection.LogCollection.create_agent_db"></a>
#### create`_`agent`_`db

```python
 | @abstractmethod
 | create_agent_db(agent: str, db: AgentLogsDB, reset: bool = False) -> "LogCollection"
```

Create logs database.

<a name="autonomy.analyse.logs.collection.LogCollection.get_next_log_block"></a>
#### get`_`next`_`log`_`block

```python
 | @staticmethod
 | get_next_log_block(fp: TextIO, prev_line: Optional[str]) -> Tuple[Optional[str], Optional[str]]
```

Get next log block.

<a name="autonomy.analyse.logs.collection.LogCollection.parse"></a>
#### parse

```python
 | @classmethod
 | parse(cls, file: Path) -> Generator[LogRow, None, None]
```

Parse logs and yield rows.

<a name="autonomy.analyse.logs.collection.FromDirectory"></a>
## FromDirectory Objects

```python
class FromDirectory(LogCollection)
```

Log stream from directory.

<a name="autonomy.analyse.logs.collection.FromDirectory.__init__"></a>
#### `__`init`__`

```python
 | __init__(directory: Path) -> None
```

Initialize object.

<a name="autonomy.analyse.logs.collection.FromDirectory.get_avilable_agents"></a>
#### get`_`avilable`_`agents

```python
 | get_avilable_agents() -> List[str]
```

Returns a list of agent names.

<a name="autonomy.analyse.logs.collection.FromDirectory.create_agent_db"></a>
#### create`_`agent`_`db

```python
 | create_agent_db(agent: str, db: AgentLogsDB, reset: bool = False) -> "FromDirectory"
```

Create logs table for agent.

