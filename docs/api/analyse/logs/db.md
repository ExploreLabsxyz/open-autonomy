<a name="autonomy.analyse.logs.db"></a>
# autonomy.analyse.logs.db

Database schemas and helpers

<a name="autonomy.analyse.logs.db.AgentLogsDB"></a>
## AgentLogsDB Objects

```python
class AgentLogsDB()
```

Logs DB

<a name="autonomy.analyse.logs.db.AgentLogsDB.__init__"></a>
#### `__`init`__`

```python
 | __init__(agent: str, file: Path) -> None
```

Initialize object.

<a name="autonomy.analyse.logs.db.AgentLogsDB.select"></a>
#### select

```python
 | select(start_time: Optional[datetime] = None, end_time: Optional[datetime] = None, log_level: Optional[str] = None, period: Optional[int] = None, round_name: Optional[str] = None, behaviour_name: Optional[str] = None) -> List[LogRow]
```

Build select query.

<a name="autonomy.analyse.logs.db.AgentLogsDB.execution_path"></a>
#### execution`_`path

```python
 | execution_path() -> List[Tuple[int, str, str]]
```

Extraction FSM execution path

<a name="autonomy.analyse.logs.db.AgentLogsDB.cursor"></a>
#### cursor

```python
 | @property
 | cursor() -> sqlite3.Cursor
```

Creates and returns a database cursor.

<a name="autonomy.analyse.logs.db.AgentLogsDB.exists"></a>
#### exists

```python
 | exists() -> bool
```

Check if table already exists.

<a name="autonomy.analyse.logs.db.AgentLogsDB.delete"></a>
#### delete

```python
 | delete() -> "AgentLogsDB"
```

Delete table

<a name="autonomy.analyse.logs.db.AgentLogsDB.create"></a>
#### create

```python
 | create(reset: bool = False) -> "AgentLogsDB"
```

Create agent table

<a name="autonomy.analyse.logs.db.AgentLogsDB.insert_many"></a>
#### insert`_`many

```python
 | insert_many(logs: Iterator[LogRow]) -> "AgentLogsDB"
```

Insert a record

