<a name="packages.valory.skills.abstract_round_abci.test_tools.base"></a>
# packages.valory.skills.abstract`_`round`_`abci.test`_`tools.base

Tests for valory/abstract_round_abci skill's behaviours.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase"></a>
## FSMBehaviourBaseCase Objects

```python
class FSMBehaviourBaseCase(BaseSkillTestCase,  ABC)
```

Base case for testing FSMBehaviour classes.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.setup_class"></a>
#### setup`_`class

```python
 | @classmethod
 | setup_class(cls, **kwargs: Any) -> None
```

Setup the test class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.setup"></a>
#### setup

```python
 | setup(**kwargs: Any) -> None
```

Set up the test method.

Called each time before a test method is called.

**Arguments**:

- `kwargs`: the keyword arguments passed to _prepare_skill

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.fast_forward_to_behaviour"></a>
#### fast`_`forward`_`to`_`behaviour

```python
 | fast_forward_to_behaviour(behaviour: AbstractRoundBehaviour, behaviour_id: str, synchronized_data: BaseSynchronizedData) -> None
```

Fast forward the FSM to a behaviour.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.mock_ledger_api_request"></a>
#### mock`_`ledger`_`api`_`request

```python
 | mock_ledger_api_request(request_kwargs: Dict, response_kwargs: Dict) -> None
```

Mock http request.

**Arguments**:

- `request_kwargs`: keyword arguments for request check.
- `response_kwargs`: keyword arguments for mock response.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.mock_contract_api_request"></a>
#### mock`_`contract`_`api`_`request

```python
 | mock_contract_api_request(contract_id: str, request_kwargs: Dict, response_kwargs: Dict) -> None
```

Mock http request.

**Arguments**:

- `contract_id`: contract id.
- `request_kwargs`: keyword arguments for request check.
- `response_kwargs`: keyword arguments for mock response.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.mock_http_request"></a>
#### mock`_`http`_`request

```python
 | mock_http_request(request_kwargs: Dict, response_kwargs: Dict) -> None
```

Mock http request.

**Arguments**:

- `request_kwargs`: keyword arguments for request check.
- `response_kwargs`: keyword arguments for mock response.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.mock_signing_request"></a>
#### mock`_`signing`_`request

```python
 | mock_signing_request(request_kwargs: Dict, response_kwargs: Dict) -> None
```

Mock signing request.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.mock_a2a_transaction"></a>
#### mock`_`a2a`_`transaction

```python
 | mock_a2a_transaction() -> None
```

Performs mock a2a transaction.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.end_round"></a>
#### end`_`round

```python
 | end_round(done_event: Enum) -> None
```

Ends round early to cover `wait_for_end` generator.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.teardown_class"></a>
#### teardown`_`class

```python
 | @classmethod
 | teardown_class(cls) -> None
```

Teardown the test class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.FSMBehaviourBaseCase.teardown"></a>
#### teardown

```python
 | teardown(**kwargs: Any) -> None
```

Teardown.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.DummyContext"></a>
## DummyContext Objects

```python
class DummyContext()
```

Dummy Context class for testing shared state initialization.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.DummyContext.params"></a>
## params Objects

```python
class params()
```

Dummy param variable.

<a name="packages.valory.skills.abstract_round_abci.test_tools.base.DummyContext.is_abstract_component"></a>
#### is`_`abstract`_`component

```python
 | @property
 | is_abstract_component() -> bool
```

Mock for is_abstract.

