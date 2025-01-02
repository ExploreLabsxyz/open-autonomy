<a name="packages.valory.skills.registration_abci.rounds"></a>
# packages.valory.skills.registration`_`abci.rounds

This module contains the data classes for common apps ABCI application.

<a name="packages.valory.skills.registration_abci.rounds.Event"></a>
## Event Objects

```python
class Event(Enum)
```

Event enumeration for the price estimation demo.

<a name="packages.valory.skills.registration_abci.rounds.FinishedRegistrationRound"></a>
## FinishedRegistrationRound Objects

```python
class FinishedRegistrationRound(DegenerateRound)
```

A round representing that agent registration has finished

<a name="packages.valory.skills.registration_abci.rounds.RegistrationStartupRound"></a>
## RegistrationStartupRound Objects

```python
class RegistrationStartupRound(CollectSameUntilAllRound)
```

A round in which the agents get registered.

This round waits until all agents have registered.

<a name="packages.valory.skills.registration_abci.rounds.RegistrationStartupRound.params"></a>
#### params

```python
 | @property
 | params() -> BaseParams
```

Return the params.

<a name="packages.valory.skills.registration_abci.rounds.RegistrationStartupRound.end_block"></a>
#### end`_`block

```python
 | end_block() -> Optional[Tuple[BaseSynchronizedData, Event]]
```

Process the end of the block.

<a name="packages.valory.skills.registration_abci.rounds.RegistrationRound"></a>
## RegistrationRound Objects

```python
class RegistrationRound(CollectSameUntilThresholdRound)
```

A round in which the agents get registered.

This rounds waits until the threshold of agents has been reached
and then a further x block confirmations.

<a name="packages.valory.skills.registration_abci.rounds.RegistrationRound.end_block"></a>
#### end`_`block

```python
 | end_block() -> Optional[Tuple[BaseSynchronizedData, Event]]
```

Process the end of the block.

<a name="packages.valory.skills.registration_abci.rounds.AgentRegistrationAbciApp"></a>
## AgentRegistrationAbciApp Objects

```python
class AgentRegistrationAbciApp(AbciApp[Event])
```

AgentRegistrationAbciApp

Initial round: RegistrationStartupRound

Initial states: {RegistrationRound, RegistrationStartupRound}

Transition states:
    0. RegistrationStartupRound
        - done: 2.
    1. RegistrationRound
        - done: 2.
        - no majority: 1.
    2. FinishedRegistrationRound

Final states: {FinishedRegistrationRound}

Timeouts:
    round timeout: 30.0

