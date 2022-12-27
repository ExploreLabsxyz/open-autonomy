Tools for analysing and verifying agent services.

This command group consists of a number of functionalities to analyse and verify agent services, including {{fsm_app}} skill consistency checks. See the appropriate subcommands for more information.



## `autonomy analyse docstrings `

Analyse {{fsm_app}} skill docstring definitions.

This command verifies that the [`AbciApp` class](../../key_concepts/abci_app_class.md) docstring is follows a standard format.

??? example

    The docstring corresponding to the [Hello World agent service](../../demos/hello_world_demo.md) is


    ```python
    """HelloWorldAbciApp

    Initial round: RegistrationRound

    Initial states: {RegistrationRound}

    Transition states:
        0. RegistrationRound
            - done: 1.
        1. CollectRandomnessRound
            - done: 2.
            - no majority: 1.
            - round timeout: 1.
        2. SelectKeeperRound
            - done: 3.
            - no majority: 0.
            - round timeout: 0.
        3. PrintMessageRound
            - done: 4.
            - round timeout: 0.
        4. ResetAndPauseRound
            - done: 1.
            - no majority: 0.
            - reset timeout: 0.

    Final states: {}

    Timeouts:
        round timeout: 30.0
        reset timeout: 30.0
    """
    ```

### Usage
```bash
autonomy analyse docstrings [OPTIONS]
```

### Options
`--update`
:   Update docstrings if required.

`--help`
:   Show the help message and exit.

### Examples
To analyse all the {{fsm_app}} skill docstrings within the local registry, run the following command in the directory containing the registry:

```bash
autonomy analyse docstrings
```


To update/fix the {{fsm_app}} skill docstrings, run the following command:
```bash
autonomy analyse docstrings --update
```

## `autonomy analyse fsm-specs`

Verify the {{fsm_app}} against its specification or generate the {{fsm_app}} specification file.

### Usage

```bash
Usage: autonomy analyse fsm-specs [OPTIONS]
```

### Options

```
--package PATH
```
:   Path to the package containing the {{fsm_app}} skill.

```
--app-class ABCI_APP_CLASS
```
:   Name of the `AbciApp` class of the {{fsm_app}}.

```
--update
```
:    Update/create the {{fsm_app}} definition file if check fails.

```
--yaml
```
:    YAML file (default).

```
--json
```
:    JSON file.

```
--mermaid
```
:    Mermaid file.

```
--help
```
:    Show the help message and exit.


### Examples
Analyse the {{fsm_app}} specification for the `hello_world_abci`:
```bash
autonomy analyse fsm-specs --package ./packages/valory/skills/hello_world_abci
```

Update/create the {{fsm_app}} specification for the `hello_world_abci` in YAML format:
```bash
autonomy analyse fsm-specs --package ./packages/valory/skills/hello_world_abci --app-class HelloWorldAbciApp --update
```

Export the {{fsm_app}} specification for the `hello_world_abci` in Mermaid format:
```bash
autonomy analyse fsm-specs --package ./packages/valory/skills/hello_world_abci --app-class HelloWorldAbciApp --update --mermaid
```

Analyse all the {{fsm_app}} specifications in a local registry. This command must be executed
in a directory containing the local registry:
```bash
autonomy analyse fsm-specs
```

## `autonomy analyse handlers`

Verify existence of handler definitions.

This command verifies that all the {{fsm_app}} skills in a local registry (except the explicitly excluded ones) have defined the specified handlers.

### Usage
``` bash
autonomy analyse handlers [OPTIONS]
```

### Options
`-h, --common-handlers HANDLER_NAME`
:   Specify which handlers to check. E.g., `-h handler_a` `-h handler_b` `-h handler_c`.

`-i, --ignore SKILL_NAME`
:   Specify which skills to skip. E.g., `-i skill_0`, `-i skill_1`, `-i skill_2`.

`--help`
:   Show the help message and exit.


### Examples

Ensure that handlers `http` and `signing` are defined in all the {{fsm_app}} skills in a local registry, except the skills `excluded_skill_1` and `excluded_skill_2`:

```bash
autonomy analyse handlers -h http -h signing -i excluded_skill_1 -i excluded_skill_2
```

## `autonomy analyse logs`
Parse logs of an agent service.

### Usage
```bash
autonomy analyse logs [OPTIONS] FILE
```
### Options
`--help`
:   Show the help message and exit.

### Examples
!!! info
    This section will be added soon.


## `autonomy analyse benchmarks`

Aggregate benchmark results from agent service deployments.

This tool requires the benchmark data generated from service agent's runtime.
By default the tool will aggregate the output for all the periods and block types but you can restrict the aggregation to a specific period and/or a specific block type.

### Usage
```bash
autonomy analyse benchmarks [OPTIONS] PATH
```

### Options
`-b, --block-type [local|consensus|total|all]`
:   Block type.

`-d, --period PERIOD_NUM`
:   Period.

`-o, --output FILE`
:   Output file name.

`--help`
:  Show the help message and exit.


### Examples

This example assumes you have completed the [quick start guide](../../guides/quick_start.md) and that you have run the [Hello World agent service](../../demos/hello_world_demo.md) for a few periods before cancelling its execution. The benchmark data will be stored in the folder `abci_build/persistent_data/benchmarks`.

To aggregate the data of all periods, execute:
```bash
autonomy analyse benchmarks ./abci_build/persistent_data/benchmarks
```