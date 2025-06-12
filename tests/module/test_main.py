import pytest
from unittest.mock import patch, MagicMock
from source import main


# Helper to reset global game_state after each test
@pytest.fixture(autouse=True)
def reset_game_state():
    original_game_state = main.game_state
    yield
    main.game_state = original_game_state


# ---------- handle_input ----------
@patch("source.main.pygame.event.get")
def test_handle_input_calls_controller(mock_event_get):
    fake_event1 = MagicMock()
    fake_event2 = MagicMock()
    mock_event_get.return_value = [fake_event1, fake_event2]

    mock_controller = MagicMock()
    mock_game_state = MagicMock()
    mock_game_state.controller = mock_controller
    main.game_state = mock_game_state

    main.handle_input()

    mock_controller.handle_input.assert_any_call(fake_event1, mock_game_state)
    mock_controller.handle_input.assert_any_call(fake_event2, mock_game_state)
    assert mock_controller.handle_input.call_count == 2


# ---------- route_cmds ----------
def test_route_cmds_executes_all_commands_and_clears_queue():
    mock_cmd1 = MagicMock()
    mock_cmd2 = MagicMock()

    mock_game_state = MagicMock()
    mock_command_queue = MagicMock()
    mock_command_queue.__iter__.return_value = [mock_cmd1, mock_cmd2]
    mock_game_state.command_queue = mock_command_queue
    main.game_state = mock_game_state

    main.route_cmds()

    mock_cmd1.resolve_target.assert_called_once_with(mock_game_state)
    mock_cmd2.resolve_target.assert_called_once_with(mock_game_state)
    mock_game_state.command_queue.clear.assert_called_once()

# ---------- update_game_state ----------
def test_update_game_state_calls_update_on_all_objects():
    mock_obj1 = MagicMock()
    mock_obj2 = MagicMock()

    mock_game_state = MagicMock()
    mock_game_state.obj_in_grid = [mock_obj1, mock_obj2]
    main.game_state = mock_game_state

    main.update_game_state()

    mock_obj1.update_state.assert_called_once_with(mock_game_state)
    mock_obj2.update_state.assert_called_once_with(mock_game_state)


# ---------- draw_screen ----------
@patch("source.main.pygame.display.flip")
def test_draw_screen_calls_draw_on_grid_and_objects(mock_flip):
    mock_grid = MagicMock()
    mock_screen = MagicMock()

    mock_obj1 = MagicMock()
    mock_obj2 = MagicMock()

    mock_game_state = MagicMock()
    mock_game_state.obj_in_grid = [mock_obj1, mock_obj2]
    main.game_state = mock_game_state
    main.grid = mock_grid
    main.screen = mock_screen

    main.draw_screen()

    mock_grid.draw.assert_called_once_with(mock_screen)
    mock_obj1.draw.assert_called_once_with(mock_screen)
    mock_obj2.draw.assert_called_once_with(mock_screen)
    mock_flip.assert_called_once()
