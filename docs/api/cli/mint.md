<a name="autonomy.cli.mint"></a>
# autonomy.cli.mint

Mint command group definitions.

<a name="autonomy.cli.mint.mint"></a>
#### mint

```python
@click.group("mint")
@pass_ctx
@chain_selection_flag()
@timeout_flag
@retries_flag
@sleep_flag
@dry_run_flag
mint(ctx: Context, chain_type: str, timeout: float, retries: int, sleep: float, dry_run: bool) -> None
```

Mint component on-chain.

<a name="autonomy.cli.mint.protocol"></a>
#### protocol

```python
@mint.command()
@package_path_decorator
@key_path_decorator
@hwi_flag
@password_decorator
@nft_decorator
@owner_flag
@update_flag
@pass_ctx
protocol(ctx: Context, package_path: Path, key: Path, password: Optional[str], nft: Optional[Union[Path, IPFSHash]], owner: Optional[str], update: Optional[int], hwi: bool = False) -> None
```

Mint a protocol component.

<a name="autonomy.cli.mint.contract"></a>
#### contract

```python
@mint.command()
@package_path_decorator
@key_path_decorator
@hwi_flag
@password_decorator
@nft_decorator
@owner_flag
@update_flag
@pass_ctx
contract(ctx: Context, package_path: Path, key: Path, password: Optional[str], nft: Optional[Union[Path, IPFSHash]], owner: Optional[str], update: Optional[int], hwi: bool = False) -> None
```

Mint a contract component.

<a name="autonomy.cli.mint.connection"></a>
#### connection

```python
@mint.command()
@package_path_decorator
@key_path_decorator
@hwi_flag
@password_decorator
@nft_decorator
@owner_flag
@update_flag
@pass_ctx
connection(ctx: Context, package_path: Path, key: Path, password: Optional[str], nft: Optional[Union[Path, IPFSHash]], owner: Optional[str], update: Optional[int], hwi: bool = False) -> None
```

Mint a connection component.

<a name="autonomy.cli.mint.skill"></a>
#### skill

```python
@mint.command()
@package_path_decorator
@key_path_decorator
@hwi_flag
@password_decorator
@nft_decorator
@owner_flag
@update_flag
@pass_ctx
skill(ctx: Context, package_path: Path, key: Path, password: Optional[str], nft: Optional[Union[Path, IPFSHash]], owner: Optional[str], update: Optional[int], hwi: bool = False) -> None
```

Mint a skill component.

<a name="autonomy.cli.mint.agent"></a>
#### agent

```python
@mint.command()
@package_path_decorator
@key_path_decorator
@hwi_flag
@password_decorator
@nft_decorator
@owner_flag
@update_flag
@pass_ctx
agent(ctx: Context, package_path: Path, key: Path, password: Optional[str], nft: Optional[Union[Path, IPFSHash]], owner: Optional[str], update: Optional[int], hwi: bool = False) -> None
```

Mint an agent.

<a name="autonomy.cli.mint.service"></a>
#### service

```python
@mint.command()
@package_path_decorator
@key_path_decorator
@hwi_flag
@password_decorator
@nft_decorator
@owner_flag
@update_flag
@token_flag
@pass_ctx
@click.option(
    "-a",
    "--agent-id",
    type=int,
    help="Canonical agent ID",
    required=True,
)
@click.option(
    "-n",
    "--number-of-slots",
    type=int,
    help="Number of agent instances for the agent",
    required=True,
)
@click.option(
    "-c",
    "--cost-of-bond",
    type=int,
    help="Cost of bond for the agent (Wei)",
    required=True,
)
@click.option(
    "--threshold",
    type=int,
    help="Threshold for the minimum numbers required to run the service",
)
service(ctx: Context, package_path: Path, key: Path, agent_id: int, number_of_slots: int, cost_of_bond: int, threshold: Optional[int], password: Optional[str], nft: Optional[Union[Path, IPFSHash]], owner: Optional[str], update: Optional[int], token: Optional[str], hwi: bool = False) -> None
```

Mint a service

