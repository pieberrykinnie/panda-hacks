from unittest.mock import MagicMock, patch

from main import minimal_planner_flow


def test_minimal_planner_flow() -> None:
    """Test the minimal planner flow returns a string (mocked OpenAI)."""
    with patch("main.get_openai_client") as mock_client:
        mock_instance = MagicMock()
        mock_instance.invoke.return_value = MagicMock(content="mocked response")
        mock_client.return_value = mock_instance
        result = minimal_planner_flow("test prompt")
        assert result == "mocked response"