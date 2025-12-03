from fastapi.testclient import TestClient

from app.main import app
from app.domain_noaa_repository import get_noaa_repository


class DummyRepository:
    """
    Simple stand-in for NOAARepository.

    Any method call returns a JSON-serializable payload describing
    which repository method was invoked and with what arguments.
    This lets us assert correct routing and parameter wiring without
    touching the real NOAA API.
    """

    def __getattr__(self, name):
        def _(*args, **kwargs):
            return {"method": name, "args": list(args), "kwargs": kwargs}

        return _


app.dependency_overrides[get_noaa_repository] = lambda: DummyRepository()

client = TestClient(app)


def _assert_method(response, expected_method: str):
    assert response.status_code == 200
    body = response.json()
    assert body["method"] == expected_method
    return body


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


# Alerts ----------------------------------------------------------------------

def test_alerts_active():
    _assert_method(client.get("/alerts/active"), "alerts_active")


def test_alerts_active_area():
    body = _assert_method(client.get("/alerts/active/area/MD"), "alerts_active_area")
    assert body["kwargs"]["area"] == "MD"


def test_alerts_active_count():
    _assert_method(client.get("/alerts/active/count"), "alerts_active_count")


def test_alerts_active_region():
    body = _assert_method(
        client.get("/alerts/active/region/AL"), "alerts_active_region"
    )
    assert body["kwargs"]["region"] == "AL"


def test_alerts_active_zone():
    body = _assert_method(
        client.get("/alerts/active/zone/MDZ001"), "alerts_active_zone"
    )
    assert body["kwargs"]["zone_id"] == "MDZ001"


def test_alerts_query():
    _assert_method(client.get("/alerts"), "alerts_query")


def test_alerts_single():
    body = _assert_method(client.get("/alerts/TEST-ID"), "alerts_single")
    assert body["kwargs"]["id"] == "TEST-ID"


def test_alerts_types():
    _assert_method(client.get("/alerts/types"), "alerts_types")


# Aviation / CWSU & SIGMET ----------------------------------------------------

def test_cwa():
    body = _assert_method(
        client.get("/aviation/cwsus/ZAB/cwas/2020-01-01/101"), "cwa"
    )
    assert body["kwargs"]["cwsu_id"] == "ZAB"
    assert body["kwargs"]["var_date"] == "2020-01-01"
    assert body["kwargs"]["sequence"] == 101


def test_cwas():
    body = _assert_method(client.get("/aviation/cwsus/ZAB/cwas"), "cwas")
    assert body["kwargs"]["cwsu_id"] == "ZAB"


def test_cwsu():
    body = _assert_method(client.get("/aviation/cwsus/ZAB"), "cwsu")
    assert body["kwargs"]["cwsu_id"] == "ZAB"


def test_sigmet():
    body = _assert_method(
        client.get("/aviation/sigmets/KZDC/2020-01-01/0000"), "sigmet"
    )
    assert body["kwargs"]["atsu"] == "KZDC"
    assert body["kwargs"]["var_date"] == "2020-01-01"
    assert body["kwargs"]["time"] == "0000"


def test_sigmet_query():
    _assert_method(client.get("/aviation/sigmets"), "sigmet_query")


def test_sigmets_by_atsu():
    body = _assert_method(client.get("/aviation/sigmets/KZDC"), "sigmets_by_atsu")
    assert body["kwargs"]["atsu"] == "KZDC"


def test_sigmets_by_atsuby_date():
    body = _assert_method(
        client.get("/aviation/sigmets/KZDC/2020-01-01"), "sigmets_by_atsuby_date"
    )
    assert body["kwargs"]["atsu"] == "KZDC"
    assert body["kwargs"]["var_date"] == "2020-01-01"


# Glossary --------------------------------------------------------------------

def test_glossary():
    _assert_method(client.get("/glossary"), "glossary")


# Gridpoints ------------------------------------------------------------------

def test_gridpoint():
    body = _assert_method(
        client.get("/gridpoints/LWX/96,70"), "gridpoint"
    )
    assert body["kwargs"]["wfo"] == "LWX"
    assert body["kwargs"]["x"] == 96
    assert body["kwargs"]["y"] == 70


def test_gridpoint_forecast():
    _assert_method(
        client.get("/gridpoints/LWX/96,70/forecast"),
        "gridpoint_forecast",
    )


def test_gridpoint_forecast_hourly():
    _assert_method(
        client.get("/gridpoints/LWX/96,70/forecast/hourly"),
        "gridpoint_forecast_hourly",
    )


def test_gridpoint_stations():
    _assert_method(
        client.get("/gridpoints/LWX/96,70/stations"),
        "gridpoint_stations",
    )


# Icons -----------------------------------------------------------------------

def test_icons():
    body = _assert_method(
        client.get("/icons/default/day/skc"),
        "icons",
    )
    assert body["kwargs"]["icon_set"] == "default"
    assert body["kwargs"]["time_of_day"] == "day"
    assert body["kwargs"]["first"] == "skc"


def test_icons_dual_condition():
    body = _assert_method(
        client.get("/icons/default/day/skc/ra"),
        "icons_dual_condition",
    )
    assert body["kwargs"]["icon_set"] == "default"
    assert body["kwargs"]["second"] == "ra"


def test_icons_summary():
    _assert_method(client.get("/icons"), "icons_summary")


# Products --------------------------------------------------------------------

def test_latest_product_type_location():
    body = _assert_method(
        client.get("/products/types/AFD/locations/LWX/latest"),
        "latest_product_type_location",
    )
    assert body["kwargs"]["type_id"] == "AFD"
    assert body["kwargs"]["location_id"] == "LWX"


def test_location_products():
    body = _assert_method(
        client.get("/products/locations/LWX/types"),
        "location_products",
    )
    assert body["kwargs"]["location_id"] == "LWX"


def test_product():
    body = _assert_method(
        client.get("/products/AFDLWX"),
        "product",
    )
    assert body["kwargs"]["product_id"] == "AFDLWX"


def test_product_locations():
    _assert_method(client.get("/products/locations"), "product_locations")


def test_product_types():
    _assert_method(client.get("/products/types"), "product_types")


def test_products_query():
    _assert_method(client.get("/products"), "products_query")


def test_products_type():
    body = _assert_method(
        client.get("/products/types/AFD"),
        "products_type",
    )
    assert body["kwargs"]["type_id"] == "AFD"


def test_products_type_location():
    body = _assert_method(
        client.get("/products/types/AFD/locations/LWX"),
        "products_type_location",
    )
    assert body["kwargs"]["type_id"] == "AFD"
    assert body["kwargs"]["location_id"] == "LWX"


def test_products_type_locations():
    body = _assert_method(
        client.get("/products/types/AFD/locations"),
        "products_type_locations",
    )
    assert body["kwargs"]["type_id"] == "AFD"


# Stations and observations ---------------------------------------------------

def test_obs_station():
    body = _assert_method(client.get("/stations/KDCA"), "obs_station")
    assert body["kwargs"]["station_id"] == "KDCA"


def test_obs_stations():
    _assert_method(client.get("/stations"), "obs_stations")


def test_station_observation_latest():
    body = _assert_method(
        client.get("/stations/KDCA/observations/latest"),
        "station_observation_latest",
    )
    assert body["kwargs"]["station_id"] == "KDCA"


def test_station_observation_list():
    body = _assert_method(
        client.get("/stations/KDCA/observations"),
        "station_observation_list",
    )
    assert body["kwargs"]["station_id"] == "KDCA"


def test_station_observation_time():
    body = _assert_method(
        client.get("/stations/KDCA/observations/2020-01-01T00:00:00Z"),
        "station_observation_time",
    )
    assert body["kwargs"]["station_id"] == "KDCA"
    assert body["kwargs"]["time"] == "2020-01-01T00:00:00Z"


def test_taf():
    body = _assert_method(
        client.get("/stations/KDCA/tafs/2020-01-01/0000"),
        "taf",
    )
    assert body["kwargs"]["station_id"] == "KDCA"


def test_tafs():
    body = _assert_method(
        client.get("/stations/KDCA/tafs"),
        "tafs",
    )
    assert body["kwargs"]["station_id"] == "KDCA"


# Offices ---------------------------------------------------------------------

def test_office():
    body = _assert_method(client.get("/offices/LWX"), "office")
    assert body["kwargs"]["office_id"] == "LWX"


def test_office_headline():
    body = _assert_method(
        client.get("/offices/LWX/headlines/1"),
        "office_headline",
    )
    assert body["kwargs"]["office_id"] == "LWX"
    assert body["kwargs"]["headline_id"] == "1"


def test_office_headlines():
    body = _assert_method(
        client.get("/offices/LWX/headlines"),
        "office_headlines",
    )
    assert body["kwargs"]["office_id"] == "LWX"


# Points ----------------------------------------------------------------------

def test_point():
    body = _assert_method(
        client.get("/points/38.99,-77.01"),
        "point",
    )
    assert body["kwargs"]["latitude"] == 38.99
    assert body["kwargs"]["longitude"] == -77.01


def test_point_radio():
    _assert_method(
        client.get("/points/38.99,-77.01/radio"),
        "point_radio",
    )


def test_point_stations():
    _assert_method(
        client.get("/points/38.99,-77.01/stations"),
        "point_stations",
    )


# Radar -----------------------------------------------------------------------

def test_radar_profiler():
    body = _assert_method(
        client.get("/radar/profilers/KDCA"),
        "radar_profiler",
    )
    assert body["kwargs"]["station_id"] == "KDCA"


def test_radar_queue():
    body = _assert_method(
        client.get("/radar/queues/example-host"),
        "radar_queue",
    )
    assert body["kwargs"]["host"] == "example-host"


def test_radar_server():
    body = _assert_method(
        client.get("/radar/servers/1"),
        "radar_server",
    )
    assert body["kwargs"]["id"] == "1"


def test_radar_servers():
    _assert_method(client.get("/radar/servers"), "radar_servers")


def test_radar_station():
    body = _assert_method(
        client.get("/radar/stations/KDCA"),
        "radar_station",
    )
    assert body["kwargs"]["station_id"] == "KDCA"


def test_radar_station_alarms():
    body = _assert_method(
        client.get("/radar/stations/KDCA/alarms"),
        "radar_station_alarms",
    )
    assert body["kwargs"]["station_id"] == "KDCA"


def test_radar_stations():
    _assert_method(client.get("/radar/stations"), "radar_stations")


# Satellite thumbnails --------------------------------------------------------

def test_satellite_thumbnails():
    body = _assert_method(
        client.get("/thumbnails/satellite/conus"),
        "satellite_thumbnails",
    )
    assert body["kwargs"]["area"] == "conus"


# Zones -----------------------------------------------------------------------

def test_zone():
    body = _assert_method(
        client.get("/zones/forecast/MDZ001"),
        "zone",
    )
    assert body["kwargs"]["zone_type"] == "forecast"
    assert body["kwargs"]["zone_id"] == "MDZ001"


def test_zone_forecast():
    body = _assert_method(
        client.get("/zones/forecast/MDZ001/forecast"),
        "zone_forecast",
    )
    assert body["kwargs"]["zone_type"] == "forecast"
    assert body["kwargs"]["zone_id"] == "MDZ001"


def test_zone_list():
    _assert_method(client.get("/zones"), "zone_list")


def test_zone_list_type():
    body = _assert_method(
        client.get("/zones/forecast"),
        "zone_list_type",
    )
    assert body["kwargs"]["zone_type"] == "forecast"


def test_zone_obs():
    body = _assert_method(
        client.get("/zones/forecast/MDZ001/observations"),
        "zone_obs",
    )
    assert body["kwargs"]["zone_id"] == "MDZ001"


def test_zone_stations():
    body = _assert_method(
        client.get("/zones/forecast/MDZ001/stations"),
        "zone_stations",
    )
    assert body["kwargs"]["zone_id"] == "MDZ001"


