[← Back to Developer Tools](../index.md)

# Debugging Using Tenderly


[Tenderly](https://tenderly.co/) is a _comprehensive Ethereum Developer Platform for real-time monitoring, alerting, debugging, and simulating Smart Contracts_. When debugging transactions and contract calls, it can be useful to help us understand what is going on with the execution. [This guide](https://docs.tenderly.co/monitoring/how-to-use-tenderly-debugger) contains a more detailed explanation on Tenderly, but for the basics:

- Create a Tenderly account and project.

- Set your Tenderly username and project name at `tenderly.yaml` (`exports/ganache/project_slug`) and at your `hardhat.config.js` module exports:

    ```
    tenderly: {
      username: "username",
      project: "projectname"
    }
    ```

- Login to Tenderly using your username and password or an access token:
    ```
    tenderly login
    ```

- Run your Hardhat deployment and export your transactions with:
    ```
    tenderly export <transaction_hash>
    ```
- You'll see a link to your Tenderly dashboard where you can inspect the full transaction stack trace.
- During testing, you will need to pause Hardhat's execution before it ends to export the transaction.
- Optionally, there's the possibility of pushing your contract's source to verify and debug it. More on that in the [Tenderly documentation](https://docs.tenderly.co/debugger/how-to-use-tenderly-debugger).
