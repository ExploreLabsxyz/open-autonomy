<a name="packages.valory.skills.registration_abci.behaviours"></a>
# packages.valory.skills.registration`_`abci.behaviours

This module contains the behaviours for the 'registration_abci' skill.

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationBaseBehaviour"></a>
## RegistrationBaseBehaviour Objects

```python
class RegistrationBaseBehaviour(BaseBehaviour,  ABC)
```

Agent registration to the FSM App.

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationBaseBehaviour.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Do the action.

Steps:
- Build a registration transaction.
- Send the transaction and wait for it to be mined.
- Wait until ABCI application transitions to the next round.
- Go to the next behaviour (set done event).

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour"></a>
## RegistrationStartupBehaviour Objects

```python
class RegistrationStartupBehaviour(RegistrationBaseBehaviour)
```

Agent registration to the FSM App.

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.initial_tm_configs"></a>
#### initial`_`tm`_`configs

```python
 | @property
 | initial_tm_configs() -> Dict[str, Dict[str, Any]]
```

A mapping of the other agents' addresses to their initial Tendermint configuration.

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.initial_tm_configs"></a>
#### initial`_`tm`_`configs

```python
 | @initial_tm_configs.setter
 | initial_tm_configs(configs: Dict[str, Dict[str, Any]]) -> None
```

A mapping of the other agents' addresses to their initial Tendermint configuration.

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.LogMessages"></a>
## LogMessages Objects

```python
class LogMessages(Enum)
```

Log messages used in RegistrationStartupBehaviour

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.LogMessages.__str__"></a>
#### `__`str`__`

```python
 | __str__() -> str
```

For ease of use in formatted string literals

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.tendermint_parameter_url"></a>
#### tendermint`_`parameter`_`url

```python
 | @property
 | tendermint_parameter_url() -> str
```

Tendermint URL for obtaining and updating parameters

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.is_correct_contract"></a>
#### is`_`correct`_`contract

```python
 | is_correct_contract(service_registry_address: str) -> Generator[None, None, bool]
```

Contract deployment verification.

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.get_agent_instances"></a>
#### get`_`agent`_`instances

```python
 | get_agent_instances(service_registry_address: str, on_chain_service_id: int) -> Generator[None, None, Dict[str, Any]]
```

Get service info available on-chain

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.get_addresses"></a>
#### get`_`addresses

```python
 | get_addresses() -> Generator
```

Get addresses of agents registered for the service

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.get_tendermint_configuration"></a>
#### get`_`tendermint`_`configuration

```python
 | get_tendermint_configuration() -> Generator[None, None, bool]
```

Make HTTP GET request to obtain agent's local Tendermint node parameters

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.request_tendermint_info"></a>
#### request`_`tendermint`_`info

```python
 | request_tendermint_info() -> Generator[None, None, bool]
```

Request Tendermint info from other agents

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.format_genesis_data"></a>
#### format`_`genesis`_`data

```python
 | format_genesis_data(collected_agent_info: Dict[str, Any]) -> Dict[str, Any]
```

Format collected agent info for genesis update

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.request_update"></a>
#### request`_`update

```python
 | request_update() -> Generator[None, None, bool]
```

Make HTTP POST request to update agent's local Tendermint node

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.wait_for_block"></a>
#### wait`_`for`_`block

```python
 | wait_for_block(timeout: float) -> Generator[None, None, bool]
```

Wait for a block to be received in the specified timeout.

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationStartupBehaviour.async_act"></a>
#### async`_`act

```python
 | async_act() -> Generator
```

Do the action.

Steps:
1. Collect personal Tendermint configuration
2. Make Service Registry contract call to retrieve addresses
   of the other agents registered on-chain for the service.
3. Request Tendermint configuration from registered agents.
   This is done over the Agent Communication Network using
   the p2p_libp2p_client connection.
4. Update Tendermint configuration via genesis.json with the
   information of the other validators (agents).
5. Restart Tendermint to establish the validator network.

<a name="packages.valory.skills.registration_abci.behaviours.RegistrationBehaviour"></a>
## RegistrationBehaviour Objects

```python
class RegistrationBehaviour(RegistrationBaseBehaviour)
```

Agent registration to the FSM App.

<a name="packages.valory.skills.registration_abci.behaviours.AgentRegistrationRoundBehaviour"></a>
## AgentRegistrationRoundBehaviour Objects

```python
class AgentRegistrationRoundBehaviour(AbstractRoundBehaviour)
```

This behaviour manages the consensus stages for the registration.

