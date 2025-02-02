[← Back to Key Concepts](./index.md)

The [Application BlockChain Interface (ABCI)](https://github.com/cometbft/cometbft/blob/main/spec/abci/README.md) defines the boundary between the consensus engine (the blockchain) and an application to be replicated across a number of platforms.
The ABCI lets the application logic communicate with the consensus engine in a transparent way so that all agents' internal state are synchronized. The application to be replicated can be written in any programming language, and it communicates with the consensus engine of each agent through a variety of methods, e.g., Unix or TCP sockets. In our case, we leverage the ABCI to replicate the sate of the [FSM App](./fsm_app_introduction.md) within the agents of an agent service.

The ABCI standard was introduced with the
[CometBFT project](https://docs.cosmos.network/v0.47/core/cometbft) (now part of Cosmos). Nevertheless,
an ABCI App can work with any consensus engine
that is ABCI-compatible, e.g., [Fantom](https://docs.fantom.foundation/).
In the remaining of this section, we will use [CometBFT](https://docs.cometbft.com/) as the consensus engine.

!!! note

    ABCI Apps are only reactive and specify how
    a transaction updates the application state.
    On the other hand, [FSM App](./fsm_app_introduction.md)s rely on the low-level ABCI application layer to replicate the state consistently among different instances,
    but they also exhibit _proactive behaviour_. For example, periodically
    execute some routines, monitor the value of the crypto assets of the final customer, etc.

    In other words, [FSM App](./fsm_app_introduction.md)s rely on the underlying ABCI, but an [FSM App](./fsm_app_introduction.md) **is not** an ABCI App.


## Brief Overview of CometBFT

[CometBFT](https://docs.cometbft.com/) is a software for securely and consistently replicating
an application on many machines. It ensures that the replication is Byzantine fault-tolerant (BFT),
i.e., it has the ability to tolerate machines failing in arbitrary ways, including becoming malicious.

CometBFT consists of two chief technical components:
a blockchain consensus engine, and a generic application interface:

- [CometBFT Core](https://cometbft.com/) is the underlying consensus engine, which ensures that the same transactions are recorded on every machine in the same order.
- The [Application BlockChain Interface (ABCI)](https://github.com/cometbft/cometbft/blob/main/spec/abci/README.md) is the interface that
  enables the transactions to be processed in any programming language.
  Unlike other blockchain and consensus solutions, which come pre-packaged with
  built-in state machines, developers can use [CometBFT](https://docs.cometbft.com/) for
  state machine replication of arbitrary applications written in any programming
  language and development environment.

In the picture below, you can see a simplified diagram showing how [CometBFT](https://docs.cometbft.com/)
modularizes a distributed state-machine replication system by clearly separating the business logic layer (the application)
from the consensus and networking layer (CometBFT Core) through the ABCI layer:

<figure markdown>
  ![](../images/cometbft.svg){align=center}
  <figcaption>Diagram of a CometBFT replicated application</figcaption>
</figure>

A detailed description of the consensus algorithm implemented
by CometBFT is out of the scope of this document.
We refer the reader to the
[CometBFT documentation](https://docs.cometbft.com/v0.37/introduction/)
for the complete details.

## The ABCI Protocol

The interaction between the consensus node and the ABCI App follows the client-server paradigm.
It must be taken into account both the callbacks received by the consensus node, and the proactive execution of transactions that the application wishes to execute.

- On one hand, the application (the server) listens for callbacks coming
from the consensus node (the client), which sends requests
to the ABCI App for different purposes. For example,
check whether a transaction is valid and therefore if it can be added
to the transaction pool, to notify the application that
a block has been validated, or to get information from the
application layer. The application must process and respond appropriately to such callbacks.

- On the other hand, the application can exhibit a proactive behaviour, when it wishes to submit a transaction to the blockchain. For example, it can commit a certain observed value in an external server. This would be the "user role" when interacting with the blockchain.

### Reactive Callbacks from the Consensus Node

The ABCI protocol specifies a number of [method calls](https://github.com/cometbft/cometbft/blob/main/spec/abci/README.md) that follow request-response interactions between the consensus node and the ABCI App. That is, the application will receive a number of callbacks related to events occurring at the consensus layer that are grouped according to their specific functionality as follows:

- Methods related to the consensus protocol: `InitChain`, `BeginBlock`, `DeliverTx`, `EndBlock` and `Commit`.
- Methods related to the mempool, used to validate new transactions before they are shared or included in a block: `CheckTx`.
- Methods for initialization and for queries from the user: `Info` and `Query`.
- Methods for serving and restoring state sync snapshots `ListSnapshots`, `LoadSnapshotChunk`, `OfferSnapshot` and `ApplySnapshotChunk`.

Additionally, there is a `Flush` method that is called on every connection, and an `Echo` method that is just for debugging.

Some requests like `Info` and `InitChain` are proactively made by the consensus node upon genesis. Most of the requests instead depend on the transactions stored in the mempool.

### Proactive Calls to the Blockchain

The ABCI App can submit transactions to the CometBFT blockchain
using the [CometBFT RPC protocol](https://docs.cometbft.com/v0.37/rpc/).
See also the [Protobuf definitions](https://github.com/cometbft/cometbft/blob/main/proto/cometbft/abci/types.proto) of those messages. The application can send a transaction by using the following
CometBFT RPC methods:

- [`broadcast_tx_sync`](https://docs.cometbft.com/v0.37/rpc/#/Tx/broadcast_tx_sync),
  which is blocking until the transaction is considered valid and added to the mempool;
- [`broadcast_tx_async`](https://docs.cometbft.com/v0.37/rpc/#/Tx/broadcast_tx_async),
  which does not wait until the transaction is considered valid and added to the mempool;
- [`broadcast_tx_commit`](https://docs.cometbft.com/v0.37/rpc/#/Tx/broadcast_tx_commit),
  which waits until the transaction is committed into a block and processed by the application.

Note that the above methods take as input a transaction, i.e., a sequence of bytes.
The consensus node does not know the meaning of the content of the transaction,
as its meaning resides in the ABCI App logic. This is a key feature
that makes the application layer and the consensus layer highly decoupled.


A quick overview of the ABCI protocol is depicted in the diagram below. See the complete details [here](https://docs.cometbft.com/v0.37/introduction/what-is-cometbft).

<figure markdown>
![](../images/abci_requests.svg)
<figcaption>Overview of the flow of messages via the ABCI protocol</figcaption>
</figure>

## ABCI Apps and the [Open Autonomy](https://docs.autonolas.network/) framework

The reader might have noticed that we have used the concepts of "reactive callbacks" from the CometBFT blockchain to the ABCI App, and "proactive calls" from the ABCI App to the blockchain.
This is by no means a coincidence with the architecture of an [AEA](./aea.md): the former are associated to reactive Handlers, whereas the latter are associated to proactive Behaviours in an AEA Skill.

Below, we depict sequence diagrams for the three transactions presented above, showing how both the proactive and reactive calls work.
The figure below shows the sequence of actions on the different components on a CometBFT application, e.g., for the request [`broadcast_tx_sync`](https://docs.cometbft.com/v0.37/rpc/#/Tx/broadcast_tx_sync):

<figure markdown>
![](../images/cometbft_transaction.svg)
<figcaption>Sequence of actions to submit a transaction on CometBFT.</figcaption>
</figure>

1. An application behaviour initiates the process by submitting a request, e.g., [`broadcast_tx_sync`](https://docs.cometbft.com/v0.37/rpc/#/Tx/broadcast_tx_sync).
2. The CometBFT nodes handle the transaction and handle any required networking or consensus actions to be done at this stage. This is transparent from the point of view of the application. Each CometBFT node notifies its associated application through the ABCI interface by calling, e.g., `CheckTx` callback method.
3. The applications respond accordingly through the ABCI interface. Again, at this point the CometBFT nodes will handle the networking and consensus layer transparently.
4. Finally, the calling behaviour receives response of the executed transaction (if applies).

A more detailed sequence diagram corresponding to this transaction is as follows:

<figure markdown>
<div class="mermaid">
    sequenceDiagram

        participant Behaviour
        participant CometBFT node
        participant ABCI App

        Behaviour->>CometBFT node: broadcast_tx_sync(tx=0x1234...)
        activate Behaviour
        note over Behaviour: wait until the transaction<br/>is added to the mempool

        CometBFT node->>ABCI App: [Request] CheckTx(tx)
        alt tx is not valid
          ABCI App->>CometBFT node: [Response] CheckTx(tx) = ERROR
          CometBFT node->>Behaviour: ERROR
        else tx is valid
          ABCI App->>CometBFT node: [Response] CheckTx(tx) = OK
          CometBFT node->>CometBFT node: add tx to mempool
          CometBFT node->>Behaviour: OK
        end

        deactivate Behaviour
</div>
<figcaption>Sequence diagram of the ``broadcast_tx_sync`` method</figcaption>
</figure>


Similarly, for the [`broadcast_tx_async`](https://docs.cometbft.com/v0.37/rpc/#/Tx/broadcast_tx_async) and the [`broadcast_tx_commit`](https://docs.cometbft.com/v0.37/rpc/#/Tx/broadcast_tx_commit) transactions we show the corresponding sequence diagrams:


<figure markdown>
<div class="mermaid">
    sequenceDiagram

        participant Behaviour
        participant CometBFT node
        participant ABCI App

        Behaviour->>CometBFT node: broadcast_tx_sync(tx=0x1234...)
        activate Behaviour
        note over Behaviour: behaviour does not wait...
        deactivate Behaviour
</div>
<figcaption>Flow diagram for the ``broadcast_tx_async`` request</figcaption>
</figure>

<figure markdown>
<div class="mermaid">
    sequenceDiagram

        participant Behaviour
        participant CometBFT node
        participant ABCI App

        Behaviour->>CometBFT node: broadcast_tx_commit(tx=0x1234...)
        activate Behaviour
        note over Behaviour: wait until the transaction<br/>is committed to the chain

        CometBFT node->>ABCI App: [Request] CheckTx(tx)
        alt tx is not valid
          ABCI App->>CometBFT node: [Response] CheckTx(tx) = ERROR
          CometBFT node->>Behaviour: ERROR
          note over Behaviour: STOP
        end
        note over Behaviour, ABCI App: tx passed the mempool check
        ABCI App->>CometBFT node: [Response] CheckTx(tx) = OK
        CometBFT node->>CometBFT node: add tx to mempool
        note over CometBFT node: eventually, the tx gets<br/>added to a committed block
        note over CometBFT node: on receipt of such block:
        CometBFT node->>ABCI App: [Request] BeginBlock(...)
        ABCI App->>CometBFT node: [Response] BeginBlock(...)
        loop for tx_i in block
          CometBFT node->>ABCI App: [Request] DeliverTx(tx_i)
          ABCI App->>CometBFT node: [Response] DeliverTx(tx_i)
        end
        CometBFT node->>ABCI App: [Request] EndBlock(...)
        ABCI App->>CometBFT node: [Response] EndBlock(...)

        alt if [Response] DeliverTx(tx) == OK
          CometBFT node->>Behaviour: ERROR
        else
          CometBFT node->>Behaviour: OK
        end
        deactivate Behaviour
</div>
<figcaption>Flow diagram for the ``broadcast_tx_commit`` request</figcaption>
</figure>

Also, the ABCI App state can be queried by means of the
[`abci_query`](https://docs.cometbft.com/v0.37/rpc/#/ABCI/abci_query)
request.
The sender has to provide the `path` parameter (a string) and the `data`
parameter (a string). The actual content will depend on the queries the ABCI App
supports. The consensus node forwards the query through the `Query` request.

<figure markdown>
<div class="mermaid">
    sequenceDiagram

        participant Behaviour
        participant CometBFT node
        participant ABCI App

        Behaviour->>CometBFT node: query(path="/a/b/c", data=0x123...)
        activate Behaviour
        CometBFT node->>ABCI App: [Request] Query(...)
        ABCI App->>CometBFT node: [Response] Query(...)
        CometBFT node->>Behaviour: response(...)
        deactivate Behaviour
</div>
<figcaption>Flow diagram for the ``abci_query`` request</figcaption>
</figure>
