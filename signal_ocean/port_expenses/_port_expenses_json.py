from typing import cast, Mapping, Any, List

from .models import PortExpenses, CanalExpenses


def parse_port_expenses(json: Mapping[str, Any]) -> PortExpenses:
    return PortExpenses(
        cast(int, json.get("portId")),
        cast(int, json.get("portCanal")),
        cast(int, json.get("towage")),
        cast(int, json.get("berth")),
        cast(int, json.get("portDues")),
        cast(int, json.get("lighthouse")),
        cast(int, json.get("mooring")),
        cast(int, json.get("pilotage")),
        cast(int, json.get("quay")),
        cast(int, json.get("anchorage")),
        cast(int, json.get("agencyFees")),
        cast(int, json.get("other")),
        cast(int, json.get("suezDues")),
        cast(int, json.get("totalCost")),
        cast(int, json.get("miscellaneousDues")),
        cast(int, json.get("isEstimated")),
        cast(int, json.get("canalDues")),
        cast(int, json.get("berthDues")),
        cast(int, json.get("lighthouseDues")),
        cast(int, json.get("mooringUnmooring")),
        cast(int, json.get("quayDues")),
        cast(int, json.get("anchorageDues")),
        cast(List[int], json.get("portAgents")),
    )


def parse_canal_expenses(json: Mapping[str, Any]) -> CanalExpenses:
    return CanalExpenses(
        cast(int, json.get("totalCost"))
    )