<a name="autonomy.analyse.service"></a>
# autonomy.analyse.service

Tools for analysing the service for deployment readiness

<a name="autonomy.analyse.service.CustomSchemaValidationError"></a>
## CustomSchemaValidationError Objects

```python
class CustomSchemaValidationError(SchemaValidationError)
```

Custom schema validation error to report all errors at once.

<a name="autonomy.analyse.service.CustomSchemaValidationError.__init__"></a>
#### `__`init`__`

```python
 | __init__(extra_properties: Optional[List[str]] = None, missing_properties: Optional[List[str]] = None, not_having_enough_properties: Optional[List[str]] = None, **kwargs: Any, ,) -> None
```

Initialize object.

<a name="autonomy.analyse.service.CustomSchemaValidator"></a>
## CustomSchemaValidator Objects

```python
class CustomSchemaValidator(Draft4Validator)
```

Custom schema validator to report all missing fields at once.

<a name="autonomy.analyse.service.CustomSchemaValidator.validate"></a>
#### validate

```python
 | validate(*args: Any, **kwargs: Any) -> None
```

Validate and raise all errors at once.

<a name="autonomy.analyse.service.ServiceValidationFailed"></a>
## ServiceValidationFailed Objects

```python
class ServiceValidationFailed(Exception)
```

Raise when service validation fails.

<a name="autonomy.analyse.service.ServiceAnalyser"></a>
## ServiceAnalyser Objects

```python
class ServiceAnalyser()
```

Tools to analyse a service

<a name="autonomy.analyse.service.ServiceAnalyser.__init__"></a>
#### `__`init`__`

```python
 | __init__(service_config: Service, abci_skill_id: PublicId, is_on_chain_check: bool = False, logger: Optional[logging.Logger] = None, skip_warnings: bool = False) -> None
```

Initialise object.

<a name="autonomy.analyse.service.ServiceAnalyser.check_on_chain_state"></a>
#### check`_`on`_`chain`_`state

```python
 | check_on_chain_state(ledger_api: LedgerApi, chain_type: ChainType, token_id: int) -> None
```

Check on-chain state of a service.

<a name="autonomy.analyse.service.ServiceAnalyser.check_agent_dependencies_published"></a>
#### check`_`agent`_`dependencies`_`published

```python
 | check_agent_dependencies_published(agent_config: AgentConfig, ipfs_pins: Set[str]) -> None
```

Check if the agent package is published or not

<a name="autonomy.analyse.service.ServiceAnalyser.cross_verify_overrides"></a>
#### cross`_`verify`_`overrides

```python
 | cross_verify_overrides(agent_config: AgentConfig, skill_config: SkillConfig) -> None
```

Cross verify overrides between service config and agent config

<a name="autonomy.analyse.service.ServiceAnalyser.validate_override_env_vars"></a>
#### validate`_`override`_`env`_`vars

```python
 | @classmethod
 | validate_override_env_vars(cls, overrides: Union[OrderedDict, dict], validate_env_var_name: bool = False, json_path: Optional[List[str]] = None) -> List[str]
```

Validate environment variables.

<a name="autonomy.analyse.service.ServiceAnalyser.validate_agent_override_env_vars"></a>
#### validate`_`agent`_`override`_`env`_`vars

```python
 | validate_agent_override_env_vars(agent_config: AgentConfig) -> None
```

Check if all of the overrides are defined as a env vars in the agent config

<a name="autonomy.analyse.service.ServiceAnalyser.validate_service_override_env_vars"></a>
#### validate`_`service`_`override`_`env`_`vars

```python
 | validate_service_override_env_vars() -> None
```

Check if all of the overrides are defined as a env vars in the agent config

<a name="autonomy.analyse.service.ServiceAnalyser.validate_override"></a>
#### validate`_`override

```python
 | validate_override(component_id: ComponentId, override: Dict, has_multiple_overrides: bool) -> None
```

Validate override

<a name="autonomy.analyse.service.ServiceAnalyser.validate_skill_config"></a>
#### validate`_`skill`_`config

```python
 | validate_skill_config(skill_config: SkillConfig) -> None
```

Check required overrides.

<a name="autonomy.analyse.service.ServiceAnalyser.validate_agent_overrides"></a>
#### validate`_`agent`_`overrides

```python
 | validate_agent_overrides(agent_config: AgentConfig) -> None
```

Check required overrides.

<a name="autonomy.analyse.service.ServiceAnalyser.validate_service_overrides"></a>
#### validate`_`service`_`overrides

```python
 | validate_service_overrides() -> None
```

Check required overrides.

