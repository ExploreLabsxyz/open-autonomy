<a name="autonomy.cli.hash"></a>
# autonomy.cli.hash

Override for hash command.

<a name="autonomy.cli.hash.hash_group"></a>
#### hash`_`group

```python
@click.group(name="hash")
hash_group() -> None
```

Hashing utils.

<a name="autonomy.cli.hash.generate_all"></a>
#### generate`_`all

```python
@hash_group.command(name="all")
@click.option(
    "--packages-dir",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default=Path("packages/"),
)
@click.option("--vendor", type=str)
@click.option("--no-wrap", is_flag=True)
generate_all(packages_dir: Path, vendor: Optional[str], no_wrap: bool) -> None
```

Generate IPFS hashes.

