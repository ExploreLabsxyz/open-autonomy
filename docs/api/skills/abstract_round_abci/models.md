<a name="packages.valory.skills.abstract_round_abci.models"></a>
# packages.valory.skills.abstract`_`round`_`abci.models

This module contains the core models for all the ABCI apps.

<a name="packages.valory.skills.abstract_round_abci.models.FrozenMixin"></a>
## FrozenMixin Objects

```python
class FrozenMixin()
```

Mixin for classes to enforce read-only attributes.

<a name="packages.valory.skills.abstract_round_abci.models.FrozenMixin.__delattr__"></a>
#### `__`delattr`__`

```python
 | __delattr__(*args: Any) -> None
```

Override __delattr__ to make object immutable.

<a name="packages.valory.skills.abstract_round_abci.models.FrozenMixin.__setattr__"></a>
#### `__`setattr`__`

```python
 | __setattr__(*args: Any) -> None
```

Override __setattr__ to make object immutable.

<a name="packages.valory.skills.abstract_round_abci.models.TypeCheckMixin"></a>
## TypeCheckMixin Objects

```python
class TypeCheckMixin()
```

Mixin for data classes & models to enforce attribute types on construction.

<a name="packages.valory.skills.abstract_round_abci.models.TypeCheckMixin.__post_init__"></a>
#### `__`post`_`init`__`

```python
 | __post_init__() -> None
```

Check that the type of the provided attributes is correct.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisBlock"></a>
## GenesisBlock Objects

```python
@dataclass(frozen=True)
class GenesisBlock(TypeCheckMixin)
```

A dataclass to store the genesis block.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisBlock.to_json"></a>
#### to`_`json

```python
 | to_json() -> Dict[str, str]
```

Get a GenesisBlock instance as a json dictionary.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisEvidence"></a>
## GenesisEvidence Objects

```python
@dataclass(frozen=True)
class GenesisEvidence(TypeCheckMixin)
```

A dataclass to store the genesis evidence.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisEvidence.to_json"></a>
#### to`_`json

```python
 | to_json() -> Dict[str, str]
```

Get a GenesisEvidence instance as a json dictionary.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisValidator"></a>
## GenesisValidator Objects

```python
@dataclass(frozen=True)
class GenesisValidator(TypeCheckMixin)
```

A dataclass to store the genesis validator.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisValidator.to_json"></a>
#### to`_`json

```python
 | to_json() -> Dict[str, List[str]]
```

Get a GenesisValidator instance as a json dictionary.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisConsensusParams"></a>
## GenesisConsensusParams Objects

```python
@dataclass(frozen=True)
class GenesisConsensusParams(TypeCheckMixin)
```

A dataclass to store the genesis consensus parameters.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisConsensusParams.from_json_dict"></a>
#### from`_`json`_`dict

```python
 | @classmethod
 | from_json_dict(cls, json_dict: dict) -> "GenesisConsensusParams"
```

Get a GenesisConsensusParams instance from a json dictionary.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisConsensusParams.to_json"></a>
#### to`_`json

```python
 | to_json() -> Dict[str, Any]
```

Get a GenesisConsensusParams instance as a json dictionary.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisConfig"></a>
## GenesisConfig Objects

```python
@dataclass(frozen=True)
class GenesisConfig(TypeCheckMixin)
```

A dataclass to store the genesis configuration.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisConfig.from_json_dict"></a>
#### from`_`json`_`dict

```python
 | @classmethod
 | from_json_dict(cls, json_dict: dict) -> "GenesisConfig"
```

Get a GenesisConfig instance from a json dictionary.

<a name="packages.valory.skills.abstract_round_abci.models.GenesisConfig.to_json"></a>
#### to`_`json

```python
 | to_json() -> Dict[str, Any]
```

Get a GenesisConfig instance as a json dictionary.

<a name="packages.valory.skills.abstract_round_abci.models.BaseParams"></a>
## BaseParams Objects

```python
class BaseParams(
    Model,  FrozenMixin,  TypeCheckMixin)
```

Parameters.

<a name="packages.valory.skills.abstract_round_abci.models.BaseParams.__init__"></a>
#### `__`init`__`

```python
 | __init__(*args: Any, **kwargs: Any) -> None
```

Initialize the parameters object.

The genesis configuration should be a dictionary with the following format:
genesis_time: str
chain_id: str
consensus_params:
block:
max_bytes: str
max_gas: str
time_iota_ms: str
evidence:
max_age_num_blocks: str
max_age_duration: str
max_bytes: str
validator:
pub_key_types: List[str]
version: dict
voting_power: str

**Arguments**:

- `args`: positional arguments
- `kwargs`: keyword arguments

<a name="packages.valory.skills.abstract_round_abci.models._MetaSharedState"></a>
## `_`MetaSharedState Objects

```python
class _MetaSharedState(ABCMeta)
```

A metaclass that validates SharedState's attributes.

<a name="packages.valory.skills.abstract_round_abci.models._MetaSharedState.__new__"></a>
#### `__`new`__`

```python
 | __new__(mcs, name: str, bases: Tuple, namespace: Dict, **kwargs: Any) -> Type
```

Initialize the class.

<a name="packages.valory.skills.abstract_round_abci.models.SharedState"></a>
## SharedState Objects

```python
class SharedState(Model,  ABC, metaclass=_MetaSharedState)
```

Keep the current shared state of the skill.

<a name="packages.valory.skills.abstract_round_abci.models.SharedState.__init__"></a>
#### `__`init`__`

```python
 | __init__(*args: Any, *, skill_context: SkillContext, **kwargs: Any, ,) -> None
```

Initialize the state.

<a name="packages.valory.skills.abstract_round_abci.models.SharedState.setup_slashing"></a>
#### setup`_`slashing

```python
 | setup_slashing(validator_to_agent: Dict[str, str]) -> None
```

Initialize the structures required for slashing.

<a name="packages.valory.skills.abstract_round_abci.models.SharedState.get_validator_address"></a>
#### get`_`validator`_`address

```python
 | get_validator_address(agent_address: str) -> str
```

Get the validator address of an agent.

<a name="packages.valory.skills.abstract_round_abci.models.SharedState.acn_container"></a>
#### acn`_`container

```python
 | acn_container() -> Dict[str, Any]
```

Create a container for ACN results, i.e., a mapping from others' addresses to `None`.

<a name="packages.valory.skills.abstract_round_abci.models.SharedState.setup"></a>
#### setup

```python
 | setup() -> None
```

Set up the model.

<a name="packages.valory.skills.abstract_round_abci.models.SharedState.round_sequence"></a>
#### round`_`sequence

```python
 | @property
 | round_sequence() -> RoundSequence
```

Get the round_sequence.

<a name="packages.valory.skills.abstract_round_abci.models.SharedState.synchronized_data"></a>
#### synchronized`_`data

```python
 | @property
 | synchronized_data() -> BaseSynchronizedData
```

Get the latest synchronized_data if available.

<a name="packages.valory.skills.abstract_round_abci.models.SharedState.get_acn_result"></a>
#### get`_`acn`_`result

```python
 | get_acn_result() -> Any
```

Get the majority of the ACN deliverables.

<a name="packages.valory.skills.abstract_round_abci.models.Requests"></a>
## Requests Objects

```python
class Requests(Model,  FrozenMixin)
```

Keep the current pending requests.

<a name="packages.valory.skills.abstract_round_abci.models.Requests.__init__"></a>
#### `__`init`__`

```python
 | __init__(*args: Any, **kwargs: Any) -> None
```

Initialize the state.

<a name="packages.valory.skills.abstract_round_abci.models.UnexpectedResponseError"></a>
## UnexpectedResponseError Objects

```python
class UnexpectedResponseError(Exception)
```

Exception class for unexpected responses from Apis.

<a name="packages.valory.skills.abstract_round_abci.models.ResponseInfo"></a>
## ResponseInfo Objects

```python
@dataclass
class ResponseInfo(TypeCheckMixin)
```

A dataclass to hold all the information related to the response.

<a name="packages.valory.skills.abstract_round_abci.models.ResponseInfo.from_json_dict"></a>
#### from`_`json`_`dict

```python
 | @classmethod
 | from_json_dict(cls, kwargs: Dict) -> "ResponseInfo"
```

Initialize a response info object from kwargs.

<a name="packages.valory.skills.abstract_round_abci.models.RetriesInfo"></a>
## RetriesInfo Objects

```python
@dataclass
class RetriesInfo(TypeCheckMixin)
```

A dataclass to hold all the information related to the retries.

<a name="packages.valory.skills.abstract_round_abci.models.RetriesInfo.from_json_dict"></a>
#### from`_`json`_`dict

```python
 | @classmethod
 | from_json_dict(cls, kwargs: Dict) -> "RetriesInfo"
```

Initialize a retries info object from kwargs.

<a name="packages.valory.skills.abstract_round_abci.models.RetriesInfo.suggested_sleep_time"></a>
#### suggested`_`sleep`_`time

```python
 | @property
 | suggested_sleep_time() -> float
```

The suggested amount of time to sleep.

<a name="packages.valory.skills.abstract_round_abci.models.TendermintRecoveryParams"></a>
## TendermintRecoveryParams Objects

```python
@dataclass(frozen=True)
class TendermintRecoveryParams(TypeCheckMixin)
```

A dataclass to hold all parameters related to agent <-> tendermint recovery procedures.

This must be frozen so that we make sure it does not get edited.

<a name="packages.valory.skills.abstract_round_abci.models.TendermintRecoveryParams.__hash__"></a>
#### `__`hash`__`

```python
 | __hash__() -> int
```

Hash the object.

<a name="packages.valory.skills.abstract_round_abci.models.ApiSpecs"></a>
## ApiSpecs Objects

```python
class ApiSpecs(Model,  FrozenMixin,  TypeCheckMixin)
```

A model that wraps APIs to get cryptocurrency prices.

<a name="packages.valory.skills.abstract_round_abci.models.ApiSpecs.__init__"></a>
#### `__`init`__`

```python
 | __init__(*args: Any, **kwargs: Any) -> None
```

Initialize ApiSpecsModel.

<a name="packages.valory.skills.abstract_round_abci.models.ApiSpecs.get_spec"></a>
#### get`_`spec

```python
 | get_spec() -> Dict
```

Returns dictionary containing api specifications.

<a name="packages.valory.skills.abstract_round_abci.models.ApiSpecs.process_response"></a>
#### process`_`response

```python
 | process_response(response: HttpMessage) -> Any
```

Process response from api.

<a name="packages.valory.skills.abstract_round_abci.models.ApiSpecs.increment_retries"></a>
#### increment`_`retries

```python
 | increment_retries() -> None
```

Increment the retries counter.

<a name="packages.valory.skills.abstract_round_abci.models.ApiSpecs.reset_retries"></a>
#### reset`_`retries

```python
 | reset_retries() -> None
```

Reset the retries counter.

<a name="packages.valory.skills.abstract_round_abci.models.ApiSpecs.is_retries_exceeded"></a>
#### is`_`retries`_`exceeded

```python
 | is_retries_exceeded() -> bool
```

Check if the retries amount has been exceeded.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkBlockTypes"></a>
## BenchmarkBlockTypes Objects

```python
class BenchmarkBlockTypes(Enum)
```

Benchmark block types.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkBlock"></a>
## BenchmarkBlock Objects

```python
class BenchmarkBlock()
```

Benchmark

This class represents logic to measure the code block using a
context manager.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkBlock.__init__"></a>
#### `__`init`__`

```python
 | __init__(block_type: str) -> None
```

Benchmark for single round.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkBlock.__enter__"></a>
#### `__`enter`__`

```python
 | __enter__() -> None
```

Enter context.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkBlock.__exit__"></a>
#### `__`exit`__`

```python
 | __exit__(*args: List, **kwargs: Dict) -> None
```

Exit context

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkBehaviour"></a>
## BenchmarkBehaviour Objects

```python
class BenchmarkBehaviour()
```

BenchmarkBehaviour

This class represents logic to benchmark a single behaviour.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkBehaviour.__init__"></a>
#### `__`init`__`

```python
 | __init__() -> None
```

Initialize Benchmark behaviour object.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkBehaviour.local"></a>
#### local

```python
 | local() -> BenchmarkBlock
```

Measure local block.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkBehaviour.consensus"></a>
#### consensus

```python
 | consensus() -> BenchmarkBlock
```

Measure consensus block.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkTool"></a>
## BenchmarkTool Objects

```python
class BenchmarkTool(Model,  TypeCheckMixin,  FrozenMixin)
```

BenchmarkTool

Tool to benchmark ABCI apps.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkTool.__init__"></a>
#### `__`init`__`

```python
 | __init__(*args: Any, **kwargs: Any) -> None
```

Benchmark tool for rounds behaviours.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkTool.measure"></a>
#### measure

```python
 | measure(behaviour: str) -> BenchmarkBehaviour
```

Measure time to complete round.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkTool.data"></a>
#### data

```python
 | @property
 | data() -> List
```

Returns formatted data.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkTool.save"></a>
#### save

```python
 | save(period: int = 0, reset: bool = True) -> None
```

Save logs to a file.

<a name="packages.valory.skills.abstract_round_abci.models.BenchmarkTool.reset"></a>
#### reset

```python
 | reset() -> None
```

Reset benchmark data

