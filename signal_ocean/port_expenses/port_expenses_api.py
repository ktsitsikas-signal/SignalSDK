# noqa: D100

from datetime import datetime
from typing import Optional

from .. import Connection
from .._internals import QueryString
from .models import PortExpenses, CanalExpenses
from ._port_expenses_json import parse_port_expenses, parse_canal_expenses


class PortExpensesAPI:
    """Represents Signal's Port Expenses API."""

    def __init__(self, connection: Optional[Connection] = None):
        """Initializes the Port Expenses API.

        Args:
            connection: API connection configuration. If not provided, the
                default connection method is used.
        """
        #TODO: Remove api_host and bearer_auth once API is public
        self.__connection = connection or \
                            Connection(api_host="https://voyagesapidev.signalocean.com",
                                       bearer_auth=True)

    def get_port_expenses(
        self, imo: int, port_id: int) -> PortExpenses:
        """Retrieves port expenses.

        Args:
            imo: The vessel's IMO number.
            port_id: ID of the port to retrieve the expenses for.

        Returns:
            The port expenses or None if a port with given ID does not exist or
            a vessel with the given IMO number does not exist.
        """
        query_string: QueryString = {
            "imo": '{}'.format(imo),
            "portId": '{}'.format(port_id),
        }

        response = self.__connection._make_post_request(
            "api/v1/PortExpenses/Port", query_string
        )
        response.raise_for_status()
        response_json = response.json()
        return_object = parse_port_expenses(response_json) if response_json else None

        return return_object

    def get_canal_expenses(
        self, canal: int, imo: int, open_port_id: int, load_port_id: int,
            discharge_port_id: int, ballast_speed: float, laden_speed: float,
            operation_status: int, formula_calculation_date: datetime,
            open_date: datetime, load_sail_date: datetime,
            cargo_type: Optional[str] = None) -> CanalExpenses:
        """Retrieves canal expenses.

        Args:
            TODO: Bring here the corresponding API documentation once available

        Returns:
            The canal expenses or None if expenses can be provided for the
            given parameters.
        """
        query_string: QueryString = {
            "canal": '{}'.format(canal),
            "imo": '{}'.format(imo),
            "openPortId": '{}'.format(open_port_id),
            "loadPortId": '{}'.format(load_port_id),
            "dischargePortId": '{}'.format(discharge_port_id),
            "ballastSpeed": '{}'.format(ballast_speed),
            "ladenSpeed": '{}'.format(laden_speed),
            "operationStatus": '{}'.format(operation_status),
            "formulaCalculationDate": formula_calculation_date.isoformat(),
            "openDate": open_date.isoformat(),
            "loadSailDate": load_sail_date.isoformat(),
            "cargoType": cargo_type
        }

        response = self.__connection._make_post_request(
            "api/v1/PortExpenses/Canal", query_string
        )

        #FIXME: This is to temporarily handle the internal error that occurs
        # in the API for unmatched parameters
        if response.status_code == 500:
            return None

        response.raise_for_status()

        #FIXME: Change this to response_json = response.json() once API is updated
        response_json = {"totalCost": response.json()}

        return_object = parse_canal_expenses(response_json) if response_json else None

        return return_object
