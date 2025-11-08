import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="globe",
        height="750px",
        center=[-100, 40],
        zoom=4,
        sidebar_visible=True,
    )

    url_routes = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/routes.geojson"
    m.add_geojson(
        url_routes,
        layer_name="捷運路線",
        color="#00FF00",
        line_width=3,
        tooltip=True,
    )
    
    m.add_pmtiles(
        building_pmtiles, style=building_style, tooltip=True, fit_bounds=False
    )
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()