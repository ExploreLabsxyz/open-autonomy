# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2024 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Localhost Deployment Generator."""
import json
import shutil
import subprocess  # nosec
import typing as t
from pathlib import Path

from aea.configurations.constants import (
    DEFAULT_LEDGER,
    LEDGER,
    PRIVATE_KEY,
    PRIVATE_KEY_PATH_SCHEMA,
)
from aea.helpers.io import open_file
from aea.helpers.yaml_utils import yaml_load_all

from autonomy.deploy.base import BaseDeploymentGenerator
from autonomy.deploy.constants import DEFAULT_ENCODING
from autonomy.deploy.generators.localhost.utils import check_tendermint_version


class HostDeploymentGenerator(BaseDeploymentGenerator):
    """Localhost deployment."""

    output_name: str = "agent.json"
    deployment_type: str = "localhost"

    def generate_config_tendermint(self) -> "HostDeploymentGenerator":
        """Generate tendermint configuration."""
        tmhome = str(self.build_dir / "node")
        tendermint_executable = check_tendermint_version()
        # if executable found, setup its configs
        subprocess.run(  # pylint: disable=subprocess-run-check # nosec
            args=[
                tendermint_executable,
                "--home",
                tmhome,
                "init",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # TODO: Dynamic port allocation
        params = {
            "TMHOME": tmhome,
            "TMSTATE": str(self.build_dir / "tm_state"),
            "P2P_LADDR": "tcp://localhost:26656",
            "RPC_LADDR": "tcp://localhost:26657",
            "PROXY_APP": "tcp://localhost:26658",
            "CREATE_EMPTY_BLOCKS": "true",
            "USE_GRPC": "false",
        }
        (self.build_dir / "tendermint.json").write_text(
            json.dumps(params, indent=2),
            encoding="utf-8",
        )

        return self

    def generate(
        self,
        image_version: t.Optional[str] = None,
        use_hardhat: bool = False,
        use_acn: bool = False,
    ) -> "HostDeploymentGenerator":
        """Generate agent and tendermint configurations"""
        agent = self.service_builder.generate_agent(agent_n=0)
        self.output = json.dumps(
            {key: f"{value}" for key, value in agent.items()}, indent=2
        )
        (self.build_dir / self.output_name).write_text(
            json.dumps(self.output, indent=2),
            encoding="utf-8",
        )

        return self

    def _populate_keys(self) -> None:
        """Populate the keys directory"""
        kp, *_ = t.cast(t.List[t.Dict[str, str]], self.service_builder.keys)
        key = kp[PRIVATE_KEY]
        ledger = kp.get(LEDGER, DEFAULT_LEDGER)
        keys_file = self.build_dir / PRIVATE_KEY_PATH_SCHEMA.format(ledger)
        keys_file.write_text(key, encoding=DEFAULT_ENCODING)

    def _populate_keys_multiledger(self) -> None:
        """Populate the keys directory with multiple set of keys"""

    def populate_private_keys(self) -> "HostDeploymentGenerator":
        """Populate the private keys to the build directory for host mapping."""
        if self.service_builder.multiledger:
            self._populate_keys_multiledger()
        else:
            self._populate_keys()
        return self

    def write_config(self) -> "BaseDeploymentGenerator":
        """Write output to build dir"""
        super().write_config()
        # copy private keys
        with open_file("aea-config.yaml", "r", encoding="utf-8") as fp:
            aea_config = yaml_load_all(fp)
        for path in aea_config[0].get("private_key_paths", {}).values():
            if Path(path).exists():
                shutil.copy(path, self.build_dir)

        # copy config and vendor
        shutil.copy("aea-config.yaml", self.build_dir)
        shutil.copytree("vendor", self.build_dir / "vendor")
        return self
