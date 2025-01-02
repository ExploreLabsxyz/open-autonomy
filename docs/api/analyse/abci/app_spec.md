<a name="autonomy.analyse.abci.app_spec"></a>
# autonomy.analyse.abci.app`_`spec

Generates the specification for a given ABCI app in YAML/JSON/Mermaid format.

<a name="autonomy.analyse.abci.app_spec.validate_fsm_spec"></a>
#### validate`_`fsm`_`spec

```python
validate_fsm_spec(data: Dict) -> None
```

Validate FSM specificaiton file.

<a name="autonomy.analyse.abci.app_spec.DFASpecificationError"></a>
## DFASpecificationError Objects

```python
class DFASpecificationError(Exception)
```

Simple class to raise errors when parsing a DFA.

<a name="autonomy.analyse.abci.app_spec.FSMSpecificationLoader"></a>
## FSMSpecificationLoader Objects

```python
class FSMSpecificationLoader()
```

FSM specification loader utilities.

<a name="autonomy.analyse.abci.app_spec.FSMSpecificationLoader.OutputFormats"></a>
## OutputFormats Objects

```python
class OutputFormats()
```

Output formats.

<a name="autonomy.analyse.abci.app_spec.FSMSpecificationLoader.from_yaml"></a>
#### from`_`yaml

```python
 | @staticmethod
 | from_yaml(file: Path) -> Dict
```

Load from yaml.

<a name="autonomy.analyse.abci.app_spec.FSMSpecificationLoader.from_json"></a>
#### from`_`json

```python
 | @staticmethod
 | from_json(file: Path) -> Dict
```

Load from json.

<a name="autonomy.analyse.abci.app_spec.FSMSpecificationLoader.load"></a>
#### load

```python
 | @classmethod
 | load(cls, file: Path, spec_format: str = OutputFormats.YAML) -> Dict
```

Load FSM specification.

<a name="autonomy.analyse.abci.app_spec.FSMSpecificationLoader.dump_json"></a>
#### dump`_`json

```python
 | @staticmethod
 | dump_json(dfa: "DFA", file: Path) -> None
```

Dump to a json file.

<a name="autonomy.analyse.abci.app_spec.FSMSpecificationLoader.dump_yaml"></a>
#### dump`_`yaml

```python
 | @staticmethod
 | dump_yaml(dfa: "DFA", file: Path) -> None
```

Dump to a yaml file.

<a name="autonomy.analyse.abci.app_spec.FSMSpecificationLoader.dump_mermaid"></a>
#### dump`_`mermaid

```python
 | @staticmethod
 | dump_mermaid(dfa: "DFA", file: Path) -> None
```

Dumps this DFA spec. to a file in Mermaid format.

<a name="autonomy.analyse.abci.app_spec.FSMSpecificationLoader.dump"></a>
#### dump

```python
 | @classmethod
 | dump(cls, dfa: "DFA", file: Path, spec_format: str = OutputFormats.YAML) -> None
```

Dumps this DFA spec. to a file in YAML/JSON/Mermaid format.

<a name="autonomy.analyse.abci.app_spec.DFA"></a>
## DFA Objects

```python
class DFA()
```

Simple specification of a deterministic finite automaton (DFA).

<a name="autonomy.analyse.abci.app_spec.DFA.__init__"></a>
#### `__`init`__`

```python
 | __init__(label: str, states: Set[str], default_start_state: str, start_states: Set[str], final_states: Set[str], alphabet_in: Set[str], transition_func: Dict[Tuple[str, str], str])
```

Initialize DFA object.

<a name="autonomy.analyse.abci.app_spec.DFA.validate_naming_conventions"></a>
#### validate`_`naming`_`conventions

```python
 | validate_naming_conventions() -> None
```

Validate state names to see if they follow the naming conventions below

- A round name should end with `Round`
- ABCI app class name should end with `AbciApp`

<a name="autonomy.analyse.abci.app_spec.DFA.is_transition_func_total"></a>
#### is`_`transition`_`func`_`total

```python
 | is_transition_func_total() -> bool
```

Outputs True if the transition function of the DFA is total.

A transition function is total when it explicitly defines all the transitions
for all the possible pairs (state, input_symbol). By convention, when a transition
(state, input_symbol) is not defined for a certain input_symbol, it will be
automatically regarded as a self-transition to the same state.

**Returns**:

True if the transition function is total. False otherwise.

<a name="autonomy.analyse.abci.app_spec.DFA.get_transitions"></a>
#### get`_`transitions

```python
 | get_transitions(input_sequence: List[str]) -> List[str]
```

Runs the DFA given the input sequence of symbols, and outputs the list of state transitions.

<a name="autonomy.analyse.abci.app_spec.DFA.parse_transition_func"></a>
#### parse`_`transition`_`func

```python
 | parse_transition_func() -> Dict[str, Dict[str, str]]
```

Parse the transition function from the spec to a nested dictionary.

<a name="autonomy.analyse.abci.app_spec.DFA.__eq__"></a>
#### `__`eq`__`

```python
 | __eq__(other: object) -> bool
```

Compares two DFAs

<a name="autonomy.analyse.abci.app_spec.DFA.generate"></a>
#### generate

```python
 | generate() -> Dict[str, Any]
```

Retrieves an exportable representation for YAML/JSON dump of this DFA.

<a name="autonomy.analyse.abci.app_spec.DFA.load"></a>
#### load

```python
 | @classmethod
 | load(cls, file: Path, spec_format: str = FSMSpecificationLoader.OutputFormats.YAML) -> "DFA"
```

Loads a DFA JSON specification from file.

<a name="autonomy.analyse.abci.app_spec.DFA.abci_to_dfa"></a>
#### abci`_`to`_`dfa

```python
 | @classmethod
 | abci_to_dfa(cls, abci_app_cls: Any, label: str = "") -> "DFA"
```

Translates an AbciApp class into a DFA.

<a name="autonomy.analyse.abci.app_spec.check_unreferenced_events"></a>
#### check`_`unreferenced`_`events

```python
check_unreferenced_events(abci_app_cls: Any) -> List[str]
```

Checks for unreferenced events in the AbciApp.

Checks that events defined in the AbciApp transition function are referenced
in the source code of the corresponding rounds or their superclasses. Note that
the function simply checks references in the "raw" source code of the rounds and
their (non builtin) superclasses. Therefore, it does not do any kind of static
analysis on the source code, nor checks for actual reachability of a return
statement returning such events.

**Arguments**:

- `abci_app_cls`: AbciApp to check unreferenced events.

**Returns**:

List of error strings

