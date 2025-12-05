"""Integration tests for IRIS vector database."""

import os

import pytest

from configs.middleware.vdb.iris_config import IrisVectorConfig
from core.rag.datasource.vdb.iris.iris_vector import IrisVector
from tests.integration_tests.vdb.test_vector_store import (
    AbstractVectorTest,
    setup_mock_redis,
)


class IrisVectorTest(AbstractVectorTest):
    """Test suite for IRIS vector store implementation."""

    def __init__(self):
        """Initialize IRIS vector test with configuration from environment."""
        super().__init__()
        self.vector = IrisVector(
            collection_name=self.collection_name,
            config=IrisVectorConfig(
                IRIS_HOST=os.environ.get("IRIS_HOST", "localhost"),
                IRIS_SUPER_SERVER_PORT=int(os.environ.get("IRIS_SUPER_SERVER_PORT", 1972)),
                IRIS_USER=os.environ.get("IRIS_USER", "_SYSTEM"),
                IRIS_PASSWORD=os.environ.get("IRIS_PASSWORD", "Dify@1234"),
                IRIS_DATABASE=os.environ.get("IRIS_DATABASE", "USER"),
                IRIS_SCHEMA=os.environ.get("IRIS_SCHEMA", "dify"),
                IRIS_CONNECTION_URL=os.environ.get("IRIS_CONNECTION_URL"),
                IRIS_MIN_CONNECTION=int(os.environ.get("IRIS_MIN_CONNECTION", 1)),
                IRIS_MAX_CONNECTION=int(os.environ.get("IRIS_MAX_CONNECTION", 3)),
            ),
        )


@pytest.mark.skipif(
    not os.environ.get("IRIS_HOST"),
    reason="IRIS_HOST environment variable not set",
)
def test_iris_vector(setup_mock_redis) -> None:
    """Run all IRIS vector store tests.

    Args:
        setup_mock_redis: Pytest fixture for mock Redis setup
    """
    IrisVectorTest().run_all_tests()
