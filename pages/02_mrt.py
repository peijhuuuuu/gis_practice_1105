import solara
import leafmap.leafmap as leafmap

def create_map():
    m = leafmap.Map(
        center=[25.0330, 121.5654],
        zoom=12,
        basemap="CartoDB.DarkMatter",
    )

    url_routes = "https://raw.githubusercontent.com/peijhuuuuu/gis_practice_1105/refs/heads/main/data/routes.geojson"
    url_stations = ""

    # 路線樣式
    style_routes = {
        "layers": [
            {
                "id": "routes",
                "source": "routes",
                "type": "line",
                "paint": {
                    "line-color": "#00FF00",
                    "line-width": 3,
                },
            }
        ]
    }

    # 站點樣式
    style_stations = {
        "layers": [
            {
                "id": "stations",
                "source": "stations",
                "type": "circle",
                "paint": {
                    "circle-color": "#FF0000",
                    "circle-radius": 6,
                },
            }
        ]
    }

    m.add_geojson(url_routes, style=style_routes)
    m.add_geojson(url_stations, style=style_stations)

    return m

@solara.component
def Page():
    return create_map() 
