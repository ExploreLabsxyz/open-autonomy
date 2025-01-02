<a name="autonomy.cli.helpers.chain"></a>
# autonomy.cli.helpers.chain

On-chain interaction helpers.

<a name="autonomy.cli.helpers.chain.OnChainHelper"></a>
## OnChainHelper Objects

```python
class OnChainHelper()
```

On-chain interaction helper.

<a name="autonomy.cli.helpers.chain.OnChainHelper.__init__"></a>
#### `__`init`__`

```python
 | __init__(chain_type: ChainType, key: Optional[Path] = None, password: Optional[str] = None, hwi: bool = False, timeout: Optional[float] = None, retries: Optional[int] = None, sleep: Optional[float] = None, dry_run: bool = False) -> None
```

Initialize object.

<a name="autonomy.cli.helpers.chain.OnChainHelper.load_hwi_plugin"></a>
#### load`_`hwi`_`plugin

```python
 | @staticmethod
 | load_hwi_plugin() -> Type[LedgerApi]
```

Load HWI Plugin.

<a name="autonomy.cli.helpers.chain.OnChainHelper.load_crypto"></a>
#### load`_`crypto

```python
 | @staticmethod
 | load_crypto(file: Path, password: Optional[str] = None) -> Crypto
```

Load crypto object.

<a name="autonomy.cli.helpers.chain.OnChainHelper.get_ledger_and_crypto_objects"></a>
#### get`_`ledger`_`and`_`crypto`_`objects

```python
 | @classmethod
 | get_ledger_and_crypto_objects(cls, chain_type: ChainType, key: Optional[Path] = None, password: Optional[str] = None, hwi: bool = False) -> Tuple[LedgerApi, Crypto]
```

Create ledger_api and crypto objects

<a name="autonomy.cli.helpers.chain.OnChainHelper.check_required_enviroment_variables"></a>
#### check`_`required`_`enviroment`_`variables

```python
 | check_required_enviroment_variables(configs: Tuple[ContractConfig, ...]) -> None
```

Check for required enviroment variables when working with the custom chain.

<a name="autonomy.cli.helpers.chain.MintHelper"></a>
## MintHelper Objects

```python
class MintHelper(OnChainHelper)
```

Mint helper.

<a name="autonomy.cli.helpers.chain.MintHelper.__init__"></a>
#### `__`init`__`

```python
 | __init__(chain_type: ChainType, key: Optional[Path] = None, password: Optional[str] = None, hwi: bool = False, update_token: Optional[int] = None, timeout: Optional[float] = None, retries: Optional[int] = None, sleep: Optional[float] = None, subgraph: Optional[str] = None, dry_run: bool = False) -> None
```

Initialize object.

<a name="autonomy.cli.helpers.chain.MintHelper.load_package_configuration"></a>
#### load`_`package`_`configuration

```python
 | load_package_configuration(package_path: Path, package_type: PackageType) -> "MintHelper"
```

Load package configuration.

<a name="autonomy.cli.helpers.chain.MintHelper.load_metadata"></a>
#### load`_`metadata

```python
 | load_metadata() -> "MintHelper"
```

Load metadata when updating a mint.

<a name="autonomy.cli.helpers.chain.MintHelper.verify_nft"></a>
#### verify`_`nft

```python
 | verify_nft(nft: Optional[NFTHashOrPath] = None) -> "MintHelper"
```

Verify NFT image.

<a name="autonomy.cli.helpers.chain.MintHelper.fetch_component_dependencies"></a>
#### fetch`_`component`_`dependencies

```python
 | fetch_component_dependencies() -> "MintHelper"
```

Verify component dependencies.

<a name="autonomy.cli.helpers.chain.MintHelper.verify_service_dependencies"></a>
#### verify`_`service`_`dependencies

```python
 | verify_service_dependencies(agent_id: int) -> "MintHelper"
```

Verify component dependencies.

<a name="autonomy.cli.helpers.chain.MintHelper.publish_metadata"></a>
#### publish`_`metadata

```python
 | publish_metadata() -> "MintHelper"
```

Publish metadata.

<a name="autonomy.cli.helpers.chain.MintHelper.mint_component"></a>
#### mint`_`component

```python
 | mint_component(owner: Optional[str] = None, component_type: UnitType = UnitType.COMPONENT) -> None
```

Mint component.

<a name="autonomy.cli.helpers.chain.MintHelper.mint_agent"></a>
#### mint`_`agent

```python
 | mint_agent(owner: Optional[str] = None) -> None
```

Mint agent.

<a name="autonomy.cli.helpers.chain.MintHelper.mint_service"></a>
#### mint`_`service

```python
 | mint_service(number_of_slots: int, cost_of_bond: int, threshold: Optional[int] = None, token: Optional[str] = None, owner: Optional[str] = None) -> None
```

Mint service

<a name="autonomy.cli.helpers.chain.MintHelper.update_component"></a>
#### update`_`component

```python
 | update_component(component_type: UnitType = UnitType.COMPONENT) -> None
```

Update component.

<a name="autonomy.cli.helpers.chain.MintHelper.update_agent"></a>
#### update`_`agent

```python
 | update_agent() -> None
```

Update agent.

<a name="autonomy.cli.helpers.chain.MintHelper.update_service"></a>
#### update`_`service

```python
 | update_service(number_of_slots: int, cost_of_bond: int, threshold: Optional[int] = None, token: Optional[str] = None) -> None
```

Update service

<a name="autonomy.cli.helpers.chain.ServiceHelper"></a>
## ServiceHelper Objects

```python
class ServiceHelper(OnChainHelper)
```

Service helper.

<a name="autonomy.cli.helpers.chain.ServiceHelper.__init__"></a>
#### `__`init`__`

```python
 | __init__(service_id: int, chain_type: ChainType, key: Optional[Path] = None, password: Optional[str] = None, hwi: bool = False, timeout: Optional[float] = None, retries: Optional[int] = None, sleep: Optional[float] = None, dry_run: bool = False) -> None
```

Initialize object.

<a name="autonomy.cli.helpers.chain.ServiceHelper.check_is_service_token_secured"></a>
#### check`_`is`_`service`_`token`_`secured

```python
 | check_is_service_token_secured(token: Optional[str] = None) -> "ServiceHelper"
```

Check if service

<a name="autonomy.cli.helpers.chain.ServiceHelper.approve_erc20_usage"></a>
#### approve`_`erc20`_`usage

```python
 | approve_erc20_usage(amount: int, spender: str) -> "ServiceHelper"
```

Approve ERC20 usage.

<a name="autonomy.cli.helpers.chain.ServiceHelper.activate_service"></a>
#### activate`_`service

```python
 | activate_service() -> None
```

Activate on-chain service

<a name="autonomy.cli.helpers.chain.ServiceHelper.register_instance"></a>
#### register`_`instance

```python
 | register_instance(instances: List[str], agent_ids: List[int]) -> None
```

Register agents instances on an activated service

<a name="autonomy.cli.helpers.chain.ServiceHelper.deploy_service"></a>
#### deploy`_`service

```python
 | deploy_service(reuse_multisig: bool = False, fallback_handler: Optional[str] = None) -> None
```

Deploy a service with registration activated

<a name="autonomy.cli.helpers.chain.ServiceHelper.terminate_service"></a>
#### terminate`_`service

```python
 | terminate_service() -> None
```

Terminate a service

<a name="autonomy.cli.helpers.chain.ServiceHelper.unbond_service"></a>
#### unbond`_`service

```python
 | unbond_service() -> None
```

Unbond a service

<a name="autonomy.cli.helpers.chain.print_service_info"></a>
#### print`_`service`_`info

```python
print_service_info(service_id: int, chain_type: ChainType) -> None
```

Print service information

