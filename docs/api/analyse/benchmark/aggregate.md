<a name="autonomy.analyse.benchmark.aggregate"></a>
# autonomy.analyse.benchmark.aggregate

Tools for aggregating benchmark results.

<a name="autonomy.analyse.benchmark.aggregate.BlockTypes"></a>
## BlockTypes Objects

```python
class BlockTypes()
```

Block types.

<a name="autonomy.analyse.benchmark.aggregate.read_benchmark_data"></a>
#### read`_`benchmark`_`data

```python
read_benchmark_data(path: Path, block_type: str = BlockTypes.ALL, period: int = -1) -> Dict[str, Dict[str, List[Dict]]]
```

Returns logs.

<a name="autonomy.analyse.benchmark.aggregate.add_statistic"></a>
#### add`_`statistic

```python
add_statistic(name: str, aggregator: Callable, behaviours: List[str], behaviour_history: Dict[str, List[float]]) -> str
```

Add a stastic column.

<a name="autonomy.analyse.benchmark.aggregate.add_statistics"></a>
#### add`_`statistics

```python
add_statistics(behaviours: List[str], behaviour_history: Dict[str, List[float]]) -> str
```

Add statistics.

<a name="autonomy.analyse.benchmark.aggregate.create_table_data"></a>
#### create`_`table`_`data

```python
create_table_data(data: Dict[str, List[Dict]], blocks: Tuple[str, ...]) -> Tuple[List[str], List[str], Dict[str, Dict]]
```

Create table data.

<a name="autonomy.analyse.benchmark.aggregate.create_agent_table"></a>
#### create`_`agent`_`table

```python
create_agent_table(agent: str, data: Dict[str, List[Dict]], blocks: Tuple[str, ...]) -> str
```

Create agent table.

<a name="autonomy.analyse.benchmark.aggregate.aggregate"></a>
#### aggregate

```python
aggregate(path: Path, block_type: str, period: int, output: Path) -> None
```

Benchmark Aggregator.

