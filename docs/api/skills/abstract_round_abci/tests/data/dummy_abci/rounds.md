<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds"></a>
# packages.valory.skills.abstract`_`round`_`abci.tests.data.dummy`_`abci.rounds

This package contains the rounds of DummyAbciApp.

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.Event"></a>
## Event Objects

```python
class Event(Enum)
```

DummyAbciApp Events

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.SynchronizedData"></a>
## SynchronizedData Objects

```python
class SynchronizedData(BaseSynchronizedData)
```

Class to represent the synchronized data.

This data is replicated by the tendermint application.

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.DummyMixinRound"></a>
## DummyMixinRound Objects

```python
class DummyMixinRound(AbstractRound,  ABC)
```

DummyMixinRound

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.DummyMixinRound.synchronized_data"></a>
#### synchronized`_`data

```python
 | @property
 | synchronized_data() -> SynchronizedData
```

Return the synchronized data.

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.DummyStartingRound"></a>
## DummyStartingRound Objects

```python
class DummyStartingRound(CollectSameUntilAllRound,  DummyMixinRound)
```

DummyStartingRound

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.DummyStartingRound.end_block"></a>
#### end`_`block

```python
 | end_block() -> Optional[Tuple[BaseSynchronizedData, Event]]
```

Process the end of the block.

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.DummyRandomnessRound"></a>
## DummyRandomnessRound Objects

```python
class DummyRandomnessRound(CollectSameUntilThresholdRound,  DummyMixinRound)
```

DummyRandomnessRound

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.DummyKeeperSelectionRound"></a>
## DummyKeeperSelectionRound Objects

```python
class DummyKeeperSelectionRound(CollectSameUntilThresholdRound,  DummyMixinRound)
```

DummyKeeperSelectionRound

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.DummyFinalRound"></a>
## DummyFinalRound Objects

```python
class DummyFinalRound(OnlyKeeperSendsRound,  DummyMixinRound)
```

DummyFinalRound

<a name="packages.valory.skills.abstract_round_abci.tests.data.dummy_abci.rounds.DummyAbciApp"></a>
## DummyAbciApp Objects

```python
class DummyAbciApp(AbciApp[Event])
```

DummyAbciApp

