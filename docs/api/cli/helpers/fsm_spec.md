<a name="autonomy.cli.helpers.fsm_spec"></a>
# autonomy.cli.helpers.fsm`_`spec

FSM spec helpers.

<a name="autonomy.cli.helpers.fsm_spec.import_and_validate_app_class"></a>
#### import`_`and`_`validate`_`app`_`class

```python
import_and_validate_app_class(module_path: Path, app_class: str) -> ModuleType
```

Import and validate rounds.py module.

<a name="autonomy.cli.helpers.fsm_spec.update_one"></a>
#### update`_`one

```python
update_one(package_path: Path, app_class: Optional[str] = None, spec_format: str = FSMSpecificationLoader.OutputFormats.YAML) -> None
```

Update FSM specification for one package.

<a name="autonomy.cli.helpers.fsm_spec.check_one"></a>
#### check`_`one

```python
check_one(package_path: Path, app_class: Optional[str] = None, spec_format: str = FSMSpecificationLoader.OutputFormats.YAML) -> None
```

Check for one.

<a name="autonomy.cli.helpers.fsm_spec.check_all"></a>
#### check`_`all

```python
check_all(packages_dir: Path, spec_format: str = FSMSpecificationLoader.OutputFormats.YAML) -> None
```

Check all the available definitions.

