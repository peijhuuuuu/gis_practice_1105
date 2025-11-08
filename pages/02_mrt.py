import solara
import leafmap.maplibregl as leafmap


def create_map():
    m = leafmap.Map(
        center=[121.55555, 25.08722],
        zoom=16,
        style="positron",
        height="750px",
        sidebar_visible=True,
    )

    # 加入底圖
    m.add_basemap("CartoDB.DarkMatter")

    # 加入 GeoJSON 圖層
    m.add_geojson(
        "https://raw.githubusercontent.com/peijhuuuuu/gis_practice_1105/refs/heads/main/data/routes.geojson",
        name="Routes",
    )

    m.add_geojson(
        "https://raw.githubusercontent.com/peijhuuuuu/gis_practice_1105/refs/heads/main/data/stations.geojson",
        name="Stations",
    )

    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
