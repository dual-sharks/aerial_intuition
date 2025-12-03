from fastapi import APIRouter, Depends, HTTPException

from openapi_client.rest import ApiException

from app.domain_noaa_repository import NOAARepository, get_noaa_repository


router = APIRouter()


# Health ----------------------------------------------------------------------

@router.get("/health", summary="Health check")
def health() -> dict:
    """Simple health endpoint for container orchestration."""
    return {"status": "ok"}


# Alerts ----------------------------------------------------------------------

@router.get("/alerts/active")
def alerts_active(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.alerts_active()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/alerts/active/area/{area}")
def alerts_active_area(
    area: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.alerts_active_area(area=area)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/alerts/active/count")
def alerts_active_count(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.alerts_active_count()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/alerts/active/region/{region}")
def alerts_active_region(
    region: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.alerts_active_region(region=region)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/alerts/active/zone/{zone_id}")
def alerts_active_zone(
    zone_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.alerts_active_zone(zone_id=zone_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/alerts/types")
def alerts_types(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.alerts_types()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/alerts")
def alerts_query(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.alerts_query()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/alerts/{id}")
def alerts_single(
    id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.alerts_single(id=id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Aviation / CWSU & SIGMET ----------------------------------------------------

@router.get("/aviation/cwsus/{cwsu_id}/cwas/{var_date}/{sequence}")
def cwa(
    cwsu_id: str,
    var_date: str,
    sequence: int,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.cwa(cwsu_id=cwsu_id, var_date=var_date, sequence=sequence)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/aviation/cwsus/{cwsu_id}/cwas")
def cwas(
    cwsu_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.cwas(cwsu_id=cwsu_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/aviation/cwsus/{cwsu_id}")
def cwsu(
    cwsu_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.cwsu(cwsu_id=cwsu_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/aviation/sigmets/{atsu}/{var_date}/{time}")
def sigmet(
    atsu: str,
    var_date: str,
    time: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.sigmet(atsu=atsu, var_date=var_date, time=time)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/aviation/sigmets")
def sigmet_query(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.sigmet_query()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/aviation/sigmets/{atsu}")
def sigmets_by_atsu(
    atsu: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.sigmets_by_atsu(atsu=atsu)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/aviation/sigmets/{atsu}/{var_date}")
def sigmets_by_atsuby_date(
    atsu: str,
    var_date: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.sigmets_by_atsuby_date(atsu=atsu, var_date=var_date)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Glossary --------------------------------------------------------------------

@router.get("/glossary")
def glossary(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.glossary()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Gridpoints ------------------------------------------------------------------

@router.get("/gridpoints/{wfo}/{x},{y}")
def gridpoint(
    wfo: str,
    x: int,
    y: int,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.gridpoint(wfo=wfo, x=x, y=y)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/gridpoints/{wfo}/{x},{y}/forecast")
def gridpoint_forecast(
    wfo: str,
    x: int,
    y: int,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.gridpoint_forecast(wfo=wfo, x=x, y=y)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/gridpoints/{wfo}/{x},{y}/forecast/hourly")
def gridpoint_forecast_hourly(
    wfo: str,
    x: int,
    y: int,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.gridpoint_forecast_hourly(wfo=wfo, x=x, y=y)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/gridpoints/{wfo}/{x},{y}/stations")
def gridpoint_stations(
    wfo: str,
    x: int,
    y: int,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.gridpoint_stations(wfo=wfo, x=x, y=y)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Icons -----------------------------------------------------------------------

@router.get("/icons/{icon_set}/{time_of_day}/{first}")
def icons(
    icon_set: str,
    time_of_day: str,
    first: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.icons(icon_set=icon_set, time_of_day=time_of_day, first=first)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/icons/{icon_set}/{time_of_day}/{first}/{second}")
def icons_dual_condition(
    icon_set: str,
    time_of_day: str,
    first: str,
    second: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.icons_dual_condition(
            icon_set=icon_set,
            time_of_day=time_of_day,
            first=first,
            second=second,
        )
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/icons")
def icons_summary(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.icons_summary()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Products --------------------------------------------------------------------

@router.get("/products/types/{type_id}/locations/{location_id}/latest")
def latest_product_type_location(
    type_id: str,
    location_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.latest_product_type_location(type_id=type_id, location_id=location_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/products/locations/{location_id}/types")
def location_products(
    location_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.location_products(location_id=location_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/products/locations")
def product_locations(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.product_locations()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/products/types")
def product_types(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.product_types()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/products/{product_id}")
def product(
    product_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.product(product_id=product_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/products")
def products_query(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.products_query()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/products/types/{type_id}")
def products_type(
    type_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.products_type(type_id=type_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/products/types/{type_id}/locations/{location_id}")
def products_type_location(
    type_id: str,
    location_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.products_type_location(type_id=type_id, location_id=location_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/products/types/{type_id}/locations")
def products_type_locations(
    type_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.products_type_locations(type_id=type_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Stations and observations ---------------------------------------------------

@router.get("/stations/{station_id}")
def obs_station(
    station_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.obs_station(station_id=station_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/stations")
def obs_stations(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.obs_stations()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/stations/{station_id}/observations/latest")
def station_observation_latest(
    station_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.station_observation_latest(station_id=station_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/stations/{station_id}/observations")
def station_observation_list(
    station_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.station_observation_list(station_id=station_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/stations/{station_id}/observations/{time}")
def station_observation_time(
    station_id: str,
    time: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.station_observation_time(station_id=station_id, time=time)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/stations/{station_id}/tafs/{var_date}/{time}")
def taf(
    station_id: str,
    var_date: str,
    time: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.taf(station_id=station_id, var_date=var_date, time=time)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/stations/{station_id}/tafs")
def tafs(
    station_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.tafs(station_id=station_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Offices ---------------------------------------------------------------------

@router.get("/offices/{office_id}")
def office(
    office_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.office(office_id=office_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/offices/{office_id}/headlines/{headline_id}")
def office_headline(
    office_id: str,
    headline_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.office_headline(office_id=office_id, headline_id=headline_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/offices/{office_id}/headlines")
def office_headlines(
    office_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.office_headlines(office_id=office_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Points ----------------------------------------------------------------------

@router.get("/points/{latitude},{longitude}")
def point(
    latitude: float,
    longitude: float,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.point(latitude=latitude, longitude=longitude)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/points/{latitude},{longitude}/radio")
def point_radio(
    latitude: float,
    longitude: float,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.point_radio(latitude=latitude, longitude=longitude)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/points/{latitude},{longitude}/stations")
def point_stations(
    latitude: float,
    longitude: float,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.point_stations(latitude=latitude, longitude=longitude)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Radar -----------------------------------------------------------------------

@router.get("/radar/profilers/{station_id}")
def radar_profiler(
    station_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.radar_profiler(station_id=station_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/radar/queues/{host}")
def radar_queue(
    host: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.radar_queue(host=host)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/radar/servers/{id}")
def radar_server(
    id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.radar_server(id=id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/radar/servers")
def radar_servers(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.radar_servers()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/radar/stations/{station_id}")
def radar_station(
    station_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.radar_station(station_id=station_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/radar/stations/{station_id}/alarms")
def radar_station_alarms(
    station_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.radar_station_alarms(station_id=station_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/radar/stations")
def radar_stations(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.radar_stations()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Satellite thumbnails --------------------------------------------------------

@router.get("/thumbnails/satellite/{area}")
def satellite_thumbnails(
    area: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.satellite_thumbnails(area=area)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


# Zones -----------------------------------------------------------------------

@router.get("/zones/{zone_type}/{zone_id}")
def zone(
    zone_type: str,
    zone_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.zone(zone_type=zone_type, zone_id=zone_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/zones/{zone_type}/{zone_id}/forecast")
def zone_forecast(
    zone_type: str,
    zone_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.zone_forecast(zone_type=zone_type, zone_id=zone_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/zones")
def zone_list(
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.zone_list()
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/zones/{zone_type}")
def zone_list_type(
    zone_type: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.zone_list_type(zone_type=zone_type)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/zones/forecast/{zone_id}/observations")
def zone_obs(
    zone_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.zone_obs(zone_id=zone_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/zones/forecast/{zone_id}/stations")
def zone_stations(
    zone_id: str,
    repo: NOAARepository = Depends(get_noaa_repository),
):
    try:
        return repo.zone_stations(zone_id=zone_id)
    except ApiException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


