<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app"></a>
# packages.valory.skills.abstract`_`round`_`abci.test`_`tools.abci`_`app

ABCI App test tools.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app._ConcreteRound"></a>
## `_`ConcreteRound Objects

```python
class _ConcreteRound(AbstractRound,  ABC)
```

ConcreteRound

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app._ConcreteRound.end_block"></a>
#### end`_`block

```python
 | end_block() -> Union[None, Tuple[MagicMock, MagicMock]]
```

End block.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app._ConcreteRound.check_payload"></a>
#### check`_`payload

```python
 | check_payload(payload: BaseTxPayload) -> None
```

Check payload.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app._ConcreteRound.process_payload"></a>
#### process`_`payload

```python
 | process_payload(payload: BaseTxPayload) -> None
```

Process payload.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteRoundA"></a>
## ConcreteRoundA Objects

```python
class ConcreteRoundA(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteRoundA.end_block"></a>
#### end`_`block

```python
 | end_block() -> Tuple[MagicMock, MagicMock]
```

End block.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteRoundB"></a>
## ConcreteRoundB Objects

```python
class ConcreteRoundB(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteRoundC"></a>
## ConcreteRoundC Objects

```python
class ConcreteRoundC(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteBackgroundRound"></a>
## ConcreteBackgroundRound Objects

```python
class ConcreteBackgroundRound(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteBackgroundSlashingRound"></a>
## ConcreteBackgroundSlashingRound Objects

```python
class ConcreteBackgroundSlashingRound(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteTerminationRoundA"></a>
## ConcreteTerminationRoundA Objects

```python
class ConcreteTerminationRoundA(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteTerminationRoundB"></a>
## ConcreteTerminationRoundB Objects

```python
class ConcreteTerminationRoundB(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteTerminationRoundC"></a>
## ConcreteTerminationRoundC Objects

```python
class ConcreteTerminationRoundC(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteSlashingRoundA"></a>
## ConcreteSlashingRoundA Objects

```python
class ConcreteSlashingRoundA(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteSlashingRoundB"></a>
## ConcreteSlashingRoundB Objects

```python
class ConcreteSlashingRoundB(_ConcreteRound)
```

Dummy instantiation of the AbstractRound class.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteEvents"></a>
## ConcreteEvents Objects

```python
class ConcreteEvents(Enum)
```

Defines dummy events to be used for testing purposes.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.ConcreteEvents.__str__"></a>
#### `__`str`__`

```python
 | __str__() -> str
```

Get the string representation of the event.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.TerminationAppTest"></a>
## TerminationAppTest Objects

```python
class TerminationAppTest(AbciApp[ConcreteEvents])
```

A dummy Termination abci for testing purposes.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.SlashingAppTest"></a>
## SlashingAppTest Objects

```python
class SlashingAppTest(AbciApp[ConcreteEvents])
```

A dummy Slashing abci for testing purposes.

<a name="packages.valory.skills.abstract_round_abci.test_tools.abci_app.AbciAppTest"></a>
## AbciAppTest Objects

```python
class AbciAppTest(AbciApp[ConcreteEvents])
```

A dummy AbciApp for testing purposes.

