# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2022 Valory AG
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

"""Tests for valory/transaction settlement skill's payload tools."""
import pytest

from packages.valory.skills.transaction_settlement_abci.payload_tools import (
    PayloadDeserializationError,
    VerificationStatus,
    tx_hist_hex_to_payload,
    tx_hist_payload_to_hex,
)


class TestTxHistPayloadEncodingDecoding:
    """Tests for the transaction history's payload encoding - decoding."""

    @staticmethod
    @pytest.mark.parametrize(
        "verification_status, tx_hash",
        (
            (
                VerificationStatus.VERIFIED,
                "0xb0e6add595e00477cf347d09797b156719dc5233283ac76e4efce2a674fe72d9",
            ),
            (VerificationStatus.ERROR, None),
        ),
    )
    def test_tx_hist_payload_to_hex_and_back(
        verification_status: VerificationStatus, tx_hash: str
    ) -> None:
        """Test `tx_hist_payload_to_hex` and `tx_hist_hex_to_payload` functions."""
        intermediate = tx_hist_payload_to_hex(verification_status, tx_hash)
        verification_status_, tx_hash_ = tx_hist_hex_to_payload(intermediate)
        assert verification_status == verification_status_
        assert tx_hash == tx_hash_

    @staticmethod
    def test_invalid_tx_hash_during_serialization() -> None:
        """Test encoding when transaction hash is invalid."""
        with pytest.raises(ValueError):
            tx_hist_payload_to_hex(VerificationStatus.VERIFIED, "")

    @staticmethod
    @pytest.mark.parametrize(
        "payload",
        ("0000000000000000000000000000000000000000000000000000000000000007", ""),
    )
    def test_invalid_payloads_during_deserialization(payload: str) -> None:
        """Test decoding payload is invalid."""
        with pytest.raises(PayloadDeserializationError):
            tx_hist_hex_to_payload(payload)
