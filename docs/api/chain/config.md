<a name="autonomy.chain.config"></a>
# autonomy.chain.config

On-chain tools configurations.

<a name="autonomy.chain.config.ChainType"></a>
## ChainType Objects

```python
class ChainType(Enum)
```

Chain types.

<a name="autonomy.chain.config.ChainType.id"></a>
#### id

```python
 | @property
 | id() -> Optional[int]
```

Chain ID

<a name="autonomy.chain.config.ChainType.rpc"></a>
#### rpc

```python
 | @property
 | rpc() -> Optional[str]
```

RPC String

<a name="autonomy.chain.config.ChainType.rpc_env_name"></a>
#### rpc`_`env`_`name

```python
 | @property
 | rpc_env_name() -> str
```

RPC Environment variable name

<a name="autonomy.chain.config.ContractConfig"></a>
## ContractConfig Objects

```python
@dataclass
class ContractConfig()
```

Contract config class.

<a name="autonomy.chain.config.ChainConfig"></a>
## ChainConfig Objects

```python
@dataclass
class ChainConfig()
```

Chain config

<a name="autonomy.chain.config.ChainConfigs"></a>
## ChainConfigs Objects

```python
class ChainConfigs()
```

Name space for chain configs.

<a name="autonomy.chain.config.ChainConfigs.get"></a>
#### get

```python
 | @classmethod
 | get(cls, chain_type: ChainType) -> ChainConfig
```

Return chain config for given chain type.

<a name="autonomy.chain.config.ChainConfigs.get_rpc_env_var"></a>
#### get`_`rpc`_`env`_`var

```python
 | @classmethod
 | get_rpc_env_var(cls, chain_type: ChainType) -> Optional[str]
```

Return chain config for given chain type.

<a name="autonomy.chain.config.ContractConfigs"></a>
## ContractConfigs Objects

```python
class ContractConfigs()
```

A namespace for contract configs.

<a name="autonomy.chain.config.ContractConfigs.get"></a>
#### get

```python
 | @classmethod
 | get(cls, name: str) -> ContractConfig
```

Return chain config for given chain type.

