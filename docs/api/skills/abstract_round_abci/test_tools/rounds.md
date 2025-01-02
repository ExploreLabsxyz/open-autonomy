<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds"></a>
# packages.valory.skills.abstract`_`round`_`abci.test`_`tools.rounds

Test tools for testing rounds.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.get_participants"></a>
#### get`_`participants

```python
get_participants() -> FrozenSet[str]
```

Participants

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyEvent"></a>
## DummyEvent Objects

```python
class DummyEvent(Enum)
```

Dummy Event

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyTxPayload"></a>
## DummyTxPayload Objects

```python
@dataclass(frozen=True)
class DummyTxPayload(BaseTxPayload)
```

Dummy Transaction Payload.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummySynchronizedData"></a>
## DummySynchronizedData Objects

```python
class DummySynchronizedData(BaseSynchronizedData)
```

Dummy synchronized data for tests.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.get_dummy_tx_payloads"></a>
#### get`_`dummy`_`tx`_`payloads

```python
get_dummy_tx_payloads(participants: FrozenSet[str], value: Any = None, vote: Optional[bool] = False, is_value_none: bool = False, is_vote_none: bool = False) -> List[DummyTxPayload]
```

Returns a list of DummyTxPayload objects.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyRound"></a>
## DummyRound Objects

```python
class DummyRound(AbstractRound)
```

Dummy round.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyRound.end_block"></a>
#### end`_`block

```python
 | end_block() -> Optional[Tuple[BaseSynchronizedData, Enum]]
```

end_block method.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyCollectionRound"></a>
## DummyCollectionRound Objects

```python
class DummyCollectionRound(CollectionRound,  DummyRound)
```

Dummy Class for CollectionRound

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyCollectDifferentUntilAllRound"></a>
## DummyCollectDifferentUntilAllRound Objects

```python
class DummyCollectDifferentUntilAllRound(CollectDifferentUntilAllRound,  DummyRound)
```

Dummy Class for CollectDifferentUntilAllRound

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyCollectSameUntilAllRound"></a>
## DummyCollectSameUntilAllRound Objects

```python
class DummyCollectSameUntilAllRound(CollectSameUntilAllRound,  DummyRound)
```

Dummy Class for CollectSameUntilThresholdRound

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyCollectDifferentUntilThresholdRound"></a>
## DummyCollectDifferentUntilThresholdRound Objects

```python
class DummyCollectDifferentUntilThresholdRound(
    CollectDifferentUntilThresholdRound,  DummyRound)
```

Dummy Class for CollectDifferentUntilThresholdRound

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyCollectSameUntilThresholdRound"></a>
## DummyCollectSameUntilThresholdRound Objects

```python
class DummyCollectSameUntilThresholdRound(CollectSameUntilThresholdRound,  DummyRound)
```

Dummy Class for CollectSameUntilThresholdRound

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyOnlyKeeperSendsRound"></a>
## DummyOnlyKeeperSendsRound Objects

```python
class DummyOnlyKeeperSendsRound(OnlyKeeperSendsRound,  DummyRound)
```

Dummy Class for OnlyKeeperSendsRound

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyVotingRound"></a>
## DummyVotingRound Objects

```python
class DummyVotingRound(VotingRound,  DummyRound)
```

Dummy Class for VotingRound

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.DummyCollectNonEmptyUntilThresholdRound"></a>
## DummyCollectNonEmptyUntilThresholdRound Objects

```python
class DummyCollectNonEmptyUntilThresholdRound(
    CollectNonEmptyUntilThresholdRound,  DummyRound)
```

Dummy Class for `CollectNonEmptyUntilThresholdRound`

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.BaseRoundTestClass"></a>
## BaseRoundTestClass Objects

```python
class BaseRoundTestClass()
```

Base test class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.BaseRoundTestClass.setup"></a>
#### setup

```python
 | setup() -> None
```

Setup test class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.BaseCollectDifferentUntilAllRoundTest"></a>
## BaseCollectDifferentUntilAllRoundTest Objects

```python
class BaseCollectDifferentUntilAllRoundTest(  # pylint: disable=too-few-public-methods
    BaseRoundTestClass)
```

Tests for rounds derived from CollectDifferentUntilAllRound.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.BaseCollectSameUntilAllRoundTest"></a>
## BaseCollectSameUntilAllRoundTest Objects

```python
class BaseCollectSameUntilAllRoundTest(
    BaseRoundTestClass)
```

Tests for rounds derived from CollectSameUntilAllRound.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.BaseCollectSameUntilThresholdRoundTest"></a>
## BaseCollectSameUntilThresholdRoundTest Objects

```python
class BaseCollectSameUntilThresholdRoundTest(  # pylint: disable=too-few-public-methods
    BaseRoundTestClass)
```

Tests for rounds derived from CollectSameUntilThresholdRound.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.BaseOnlyKeeperSendsRoundTest"></a>
## BaseOnlyKeeperSendsRoundTest Objects

```python
class BaseOnlyKeeperSendsRoundTest(  # pylint: disable=too-few-public-methods
    BaseRoundTestClass)
```

Tests for rounds derived from OnlyKeeperSendsRound.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.BaseVotingRoundTest"></a>
## BaseVotingRoundTest Objects

```python
class BaseVotingRoundTest(BaseRoundTestClass)
```

Tests for rounds derived from VotingRound.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.BaseCollectDifferentUntilThresholdRoundTest"></a>
## BaseCollectDifferentUntilThresholdRoundTest Objects

```python
class BaseCollectDifferentUntilThresholdRoundTest(  # pylint: disable=too-few-public-methods
    BaseRoundTestClass)
```

Tests for rounds derived from CollectDifferentUntilThresholdRound.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds.BaseCollectNonEmptyUntilThresholdRound"></a>
## BaseCollectNonEmptyUntilThresholdRound Objects

```python
class BaseCollectNonEmptyUntilThresholdRound(  # pylint: disable=too-few-public-methods
    BaseCollectDifferentUntilThresholdRoundTest)
```

Tests for rounds derived from `CollectNonEmptyUntilThresholdRound`.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds._BaseRoundTestClass"></a>
## `_`BaseRoundTestClass Objects

```python
class _BaseRoundTestClass(BaseRoundTestClass)
```

Base test class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.rounds._BaseRoundTestClass.setup"></a>
#### setup

```python
 | setup() -> None
```

Setup test class.

