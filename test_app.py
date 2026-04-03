def test_header_present(dash_duo):
    from dash_gui import app

    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Sales Visualizer"
def test_graph_present(dash_duo):
    from dash_gui import app
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    from dash_gui import app
    dash_duo.start_server(app)

    region = dash_duo.find_element("#region-picker")
    assert region is not None