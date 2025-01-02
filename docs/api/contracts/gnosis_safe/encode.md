<a name="packages.valory.contracts.gnosis_safe.encode"></a>
# packages.valory.contracts.gnosis`_`safe.encode

ETH encoder.

<a name="packages.valory.contracts.gnosis_safe.encode.encode"></a>
#### encode

```python
encode(typ: t.Any, arg: t.Any) -> bytes
```

Encode by type.

<a name="packages.valory.contracts.gnosis_safe.encode.to_string"></a>
#### to`_`string

```python
to_string(value: t.Union[bytes, str, int]) -> bytes
```

Convert to byte string.

<a name="packages.valory.contracts.gnosis_safe.encode.sha3_256"></a>
#### sha3`_`256

```python
sha3_256(x: bytes) -> bytes
```

Calculate SHA3-256 hash.

<a name="packages.valory.contracts.gnosis_safe.encode.sha3"></a>
#### sha3

```python
sha3(seed: t.Union[bytes, str, int]) -> bytes
```

Calculate SHA3-256 hash.

<a name="packages.valory.contracts.gnosis_safe.encode.scan_bin"></a>
#### scan`_`bin

```python
scan_bin(v: str) -> bytes
```

Scan bytes.

<a name="packages.valory.contracts.gnosis_safe.encode.create_struct_definition"></a>
#### create`_`struct`_`definition

```python
create_struct_definition(name: str, schema: t.List[t.Dict[str, str]]) -> str
```

Create method struction defintion.

<a name="packages.valory.contracts.gnosis_safe.encode.find_dependencies"></a>
#### find`_`dependencies

```python
find_dependencies(name: str, types: t.Dict[str, t.Any], dependencies: t.Set) -> None
```

Find dependencies.

<a name="packages.valory.contracts.gnosis_safe.encode.create_schema"></a>
#### create`_`schema

```python
create_schema(name: str, types: t.Dict) -> str
```

Create schema.

<a name="packages.valory.contracts.gnosis_safe.encode.create_schema_hash"></a>
#### create`_`schema`_`hash

```python
create_schema_hash(name: str, types: t.Dict) -> bytes
```

Create schema hash.

<a name="packages.valory.contracts.gnosis_safe.encode.encode_value"></a>
#### encode`_`value

```python
encode_value(data_type: str, value: t.Any, types: t.Dict) -> bytes
```

Encode value.

<a name="packages.valory.contracts.gnosis_safe.encode.encode_data"></a>
#### encode`_`data

```python
encode_data(name: str, data: t.Dict[str, t.Dict[str, str]], types: t.Dict) -> bytes
```

Encode data.

<a name="packages.valory.contracts.gnosis_safe.encode.create_struct_hash"></a>
#### create`_`struct`_`hash

```python
create_struct_hash(name: str, data: t.Dict[str, t.Dict[str, str]], types: t.Dict) -> bytes
```

Create struct hash.

<a name="packages.valory.contracts.gnosis_safe.encode.encode_typed_data"></a>
#### encode`_`typed`_`data

```python
encode_typed_data(data: t.Dict[str, t.Any]) -> bytes
```

Encode typed data.

