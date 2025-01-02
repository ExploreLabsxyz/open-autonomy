<a name="autonomy.cli.packages"></a>
# autonomy.cli.packages

Override for packages command.

<a name="autonomy.cli.packages.lock_packages"></a>
#### lock`_`packages

```python
@package_manager.command(name="lock")
@click.option(
    "--check",
    is_flag=True,
    help="Check that fingerprints in packages.json match the local packages",
)
@click.option(
    "--skip-missing",
    is_flag=True,
    help="Skip packages missing from the `packages.json` file.",
)
@pass_ctx
lock_packages(ctx: Context, check: bool, skip_missing: bool) -> None
```

Lock local packages.

<a name="autonomy.cli.packages.get_package_manager"></a>
#### get`_`package`_`manager

```python
get_package_manager(packages_dir: Path) -> BasePackageManager
```

Get package manager.

<a name="autonomy.cli.packages._PackageManagerWithServicePatch"></a>
## `_`PackageManagerWithServicePatch Objects

```python
class _PackageManagerWithServicePatch(BasePackageManager)
```

Patch package manager for service component.

<a name="autonomy.cli.packages._PackageManagerWithServicePatch.update_dependencies"></a>
#### update`_`dependencies

```python
 | update_dependencies(package_id: PackageId) -> None
```

Update dependencies.

<a name="autonomy.cli.packages._PackageManagerWithServicePatch.check_dependencies"></a>
#### check`_`dependencies

```python
 | check_dependencies(configuration: PackageConfiguration) -> List[Tuple[PackageId, DepedencyMismatchErrors]]
```

Update dependencies.

<a name="autonomy.cli.packages.PackageManagerV0"></a>
## PackageManagerV0 Objects

```python
class PackageManagerV0(BasePackageManagerV0,  _PackageManagerWithServicePatch)
```

Patch package manager for service component.

<a name="autonomy.cli.packages.PackageManagerV1"></a>
## PackageManagerV1 Objects

```python
class PackageManagerV1(BasePackageManagerV1,  _PackageManagerWithServicePatch)
```

Patch package manager for service component.

