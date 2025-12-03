from functools import lru_cache

import openapi_client
from openapi_client.api.default_api import DefaultApi


class NOAARepository:
    """
    Domain-oriented repository that wraps the generated DefaultApi client.

    This isolates the rest of the application from direct knowledge of the
    underlying HTTP client and allows you to evolve the domain layer without
    touching FastAPI routes.
    """

    def __init__(self, api: DefaultApi) -> None:
        self._api = api

    # Alerts -----------------------------------------------------------------

    def alerts_active(self, **kwargs):
        return self._api.alerts_active(**kwargs)

    def alerts_active_area(self, area: str):
        return self._api.alerts_active_area(area=area)

    def alerts_active_count(self):
        return self._api.alerts_active_count()

    def alerts_active_region(self, region: str):
        return self._api.alerts_active_region(region=region)

    def alerts_active_zone(self, zone_id: str):
        return self._api.alerts_active_zone(zone_id=zone_id)

    def alerts_query(self, **kwargs):
        return self._api.alerts_query(**kwargs)

    def alerts_single(self, id: str):
        return self._api.alerts_single(id=id)

    def alerts_types(self):
        return self._api.alerts_types()

    # Aviation / CWSU & SIGMET -----------------------------------------------

    def cwa(self, cwsu_id: str, var_date: str, sequence: int):
        return self._api.cwa(cwsu_id=cwsu_id, var_date=var_date, sequence=sequence)

    def cwas(self, cwsu_id: str):
        return self._api.cwas(cwsu_id=cwsu_id)

    def cwsu(self, cwsu_id: str):
        return self._api.cwsu(cwsu_id=cwsu_id)

    def sigmet(self, atsu: str, var_date: str, time: str):
        return self._api.sigmet(atsu=atsu, var_date=var_date, time=time)

    def sigmet_query(self, **kwargs):
        return self._api.sigmet_query(**kwargs)

    def sigmets_by_atsu(self, atsu: str):
        return self._api.sigmets_by_atsu(atsu=atsu)

    def sigmets_by_atsuby_date(self, atsu: str, var_date: str):
        return self._api.sigmets_by_atsuby_date(atsu=atsu, var_date=var_date)

    # Glossary ----------------------------------------------------------------

    def glossary(self):
        return self._api.glossary()

    # Gridpoints --------------------------------------------------------------

    def gridpoint(self, wfo: str, x: int, y: int):
        return self._api.gridpoint(wfo=wfo, x=x, y=y)

    def gridpoint_forecast(self, wfo: str, x: int, y: int):
        return self._api.gridpoint_forecast(wfo=wfo, x=x, y=y)

    def gridpoint_forecast_hourly(self, wfo: str, x: int, y: int):
        return self._api.gridpoint_forecast_hourly(wfo=wfo, x=x, y=y)

    def gridpoint_stations(self, wfo: str, x: int, y: int):
        return self._api.gridpoint_stations(wfo=wfo, x=x, y=y)

    # Icons -------------------------------------------------------------------

    def icons(self, icon_set: str, time_of_day: str, first: str):
        return self._api.icons(set=icon_set, time_of_day=time_of_day, first=first)

    def icons_dual_condition(
        self, icon_set: str, time_of_day: str, first: str, second: str
    ):
        return self._api.icons_dual_condition(
            set=icon_set, time_of_day=time_of_day, first=first, second=second
        )

    def icons_summary(self):
        return self._api.icons_summary()

    # Products ----------------------------------------------------------------

    def latest_product_type_location(self, type_id: str, location_id: str):
        return self._api.latest_product_type_location(
            type_id=type_id, location_id=location_id
        )

    def location_products(self, location_id: str):
        return self._api.location_products(location_id=location_id)

    def product(self, product_id: str):
        return self._api.product(product_id=product_id)

    def product_locations(self):
        return self._api.product_locations()

    def product_types(self):
        return self._api.product_types()

    def products_query(self, **kwargs):
        return self._api.products_query(**kwargs)

    def products_type(self, type_id: str):
        return self._api.products_type(type_id=type_id)

    def products_type_location(self, type_id: str, location_id: str):
        return self._api.products_type_location(type_id=type_id, location_id=location_id)

    def products_type_locations(self, type_id: str):
        return self._api.products_type_locations(type_id=type_id)

    # Stations & observations -------------------------------------------------

    def obs_station(self, station_id: str):
        return self._api.obs_station(station_id=station_id)

    def obs_stations(self, **kwargs):
        return self._api.obs_stations(**kwargs)

    def station_observation_latest(self, station_id: str):
        return self._api.station_observation_latest(station_id=station_id)

    def station_observation_list(self, station_id: str, **kwargs):
        return self._api.station_observation_list(station_id=station_id, **kwargs)

    def station_observation_time(self, station_id: str, time: str):
        return self._api.station_observation_time(station_id=station_id, time=time)

    def taf(self, station_id: str, var_date: str, time: str):
        return self._api.taf(station_id=station_id, var_date=var_date, time=time)

    def tafs(self, station_id: str):
        return self._api.tafs(station_id=station_id)

    # Offices -----------------------------------------------------------------

    def office(self, office_id: str):
        return self._api.office(office_id=office_id)

    def office_headline(self, office_id: str, headline_id: str):
        return self._api.office_headline(office_id=office_id, headline_id=headline_id)

    def office_headlines(self, office_id: str):
        return self._api.office_headlines(office_id=office_id)

    # Points ------------------------------------------------------------------

    def point(self, latitude: float, longitude: float):
        return self._api.point(latitude=latitude, longitude=longitude)

    def point_radio(self, latitude: float, longitude: float):
        return self._api.point_radio(latitude=latitude, longitude=longitude)

    def point_stations(self, latitude: float, longitude: float):
        return self._api.point_stations(latitude=latitude, longitude=longitude)

    # Radar -------------------------------------------------------------------

    def radar_profiler(self, station_id: str):
        return self._api.radar_profiler(station_id=station_id)

    def radar_queue(self, host: str):
        return self._api.radar_queue(host=host)

    def radar_server(self, server_id: str):
        return self._api.radar_server(id=server_id)

    def radar_servers(self):
        return self._api.radar_servers()

    def radar_station(self, station_id: str):
        return self._api.radar_station(station_id=station_id)

    def radar_station_alarms(self, station_id: str):
        return self._api.radar_station_alarms(station_id=station_id)

    def radar_stations(self):
        return self._api.radar_stations()

    # Satellite thumbnails ----------------------------------------------------

    def satellite_thumbnails(self, area: str):
        return self._api.satellite_thumbnails(area=area)

    # Zones -------------------------------------------------------------------

    def zone(self, zone_type: str, zone_id: str):
        return self._api.zone(type=zone_type, zone_id=zone_id)

    def zone_forecast(self, zone_type: str, zone_id: str):
        return self._api.zone_forecast(type=zone_type, zone_id=zone_id)

    def zone_list(self, **kwargs):
        return self._api.zone_list(**kwargs)

    def zone_list_type(self, zone_type: str):
        return self._api.zone_list_type(type=zone_type)

    def zone_obs(self, zone_id: str):
        return self._api.zone_obs(zone_id=zone_id)

    def zone_stations(self, zone_id: str):
        return self._api.zone_stations(zone_id=zone_id)


NOAA_BASE_URL = "https://api.weather.gov"


@lru_cache
def get_noaa_api() -> DefaultApi:
    configuration = openapi_client.Configuration(host=NOAA_BASE_URL)
    api_client = openapi_client.ApiClient(configuration)
    return DefaultApi(api_client)


@lru_cache
def get_noaa_repository() -> NOAARepository:
    """
    FastAPI-friendly singleton repository provider.

    Use this with `Depends(get_noaa_repository)` in your route functions.
    """

    return NOAARepository(get_noaa_api())


