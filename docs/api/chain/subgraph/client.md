<a name="autonomy.chain.subgraph.client"></a>
# autonomy.chain.subgraph.client

Subgraph client.

<a name="autonomy.chain.subgraph.client.Unit"></a>
## Unit Objects

```python
class Unit(TypedDict)
```

Unit container.

<a name="autonomy.chain.subgraph.client.UnitContainer"></a>
## UnitContainer Objects

```python
class UnitContainer(TypedDict)
```

Unit container

<a name="autonomy.chain.subgraph.client.SubgraphClient"></a>
## SubgraphClient Objects

```python
class SubgraphClient()
```

Subgraph helper class.

<a name="autonomy.chain.subgraph.client.SubgraphClient.__init__"></a>
#### `__`init`__`

```python
 | __init__(url: Optional[str] = None) -> None
```

Initialize object

<a name="autonomy.chain.subgraph.client.SubgraphClient.get_component_by_token"></a>
#### get`_`component`_`by`_`token

```python
 | get_component_by_token(token_id: int, package_type: PackageType) -> UnitContainer
```

Get component by package hash

<a name="autonomy.chain.subgraph.client.SubgraphClient.get_record_by_package_hash"></a>
#### get`_`record`_`by`_`package`_`hash

```python
 | get_record_by_package_hash(package_hash: str) -> UnitContainer
```

Get component by package hash

<a name="autonomy.chain.subgraph.client.SubgraphClient.get_record_by_package_id"></a>
#### get`_`record`_`by`_`package`_`id

```python
 | get_record_by_package_id(package_id: PackageId) -> UnitContainer
```

Get component by package hash

