from datetime import datetime, timezone

from langgraph.pregel import Pregel

from simple_agent.graph import graph, local_now, read_preference, to_local, update_preference, utc_now


def test_graph_compiles() -> None:
    assert isinstance(graph, Pregel)


def test_utc_now_tool() -> None:
    result = utc_now.invoke({})
    assert isinstance(result, str)
    assert "T" in result

def test_local_now_tool() -> None:
    result = local_now.invoke({"tz_name": "Europe/Paris"})
    assert isinstance(result, str)
    assert result.endswith(("+01:00", "+02:00"))

def test_to_local_summer_and_winter() -> None:
    summer = datetime(2026, 10, 16, 8, 44, tzinfo=timezone.utc)
    winter = datetime(2026, 10, 27, 8, 44, tzinfo=timezone.utc)
    assert to_local(summer, "Europe/Paris") == "2026-10-16T10:44:00+02:00"
    assert to_local(winter, "Europe/Paris") == "2026-10-27T09:44:00+01:00"
