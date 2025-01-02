<a name="autonomy.fsm.scaffold.base"></a>
# autonomy.fsm.scaffold.base

FSM scaffold tools.

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator"></a>
## AbstractFileGenerator Objects

```python
class AbstractFileGenerator(ABC)
```

An abstract class for file generators.

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.__init__"></a>
#### `__`init`__`

```python
 | __init__(ctx: Context, skill_name: str, dfa: DFA) -> None
```

Initialize the abstract file generator.

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.get_file_content"></a>
#### get`_`file`_`content

```python
 | @abstractmethod
 | get_file_content() -> str
```

Get file content.

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.write_file"></a>
#### write`_`file

```python
 | write_file(output_dir: Path) -> None
```

Write the file to output_dir/FILENAME.

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.abci_app_name"></a>
#### abci`_`app`_`name

```python
 | @property
 | abci_app_name() -> str
```

ABCI app class name

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.fsm_name"></a>
#### fsm`_`name

```python
 | @property
 | fsm_name() -> str
```

FSM base name

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.author"></a>
#### author

```python
 | @property
 | author() -> str
```

Author

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.all_rounds"></a>
#### all`_`rounds

```python
 | @property
 | all_rounds() -> List[str]
```

Rounds

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.degenerate_rounds"></a>
#### degenerate`_`rounds

```python
 | @property
 | degenerate_rounds() -> List[str]
```

Degenerate rounds

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.rounds"></a>
#### rounds

```python
 | @property
 | rounds() -> List[str]
```

Non-degenerate rounds

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.behaviours"></a>
#### behaviours

```python
 | @property
 | behaviours() -> List[str]
```

Behaviours

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.payloads"></a>
#### payloads

```python
 | @property
 | payloads() -> List[str]
```

Payloads

<a name="autonomy.fsm.scaffold.base.AbstractFileGenerator.template_kwargs"></a>
#### template`_`kwargs

```python
 | @property
 | template_kwargs() -> Dict[str, str]
```

All keywords for string formatting of templates

