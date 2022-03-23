import dash_bootstrap_components as dbc
from dash import html, dcc, dash, callback, Output, Input
from dash.exceptions import PreventUpdate

from read_data import read_data

data = read_data()

departamentos = data['departamento'].unique()
municipios = data['municipio'].unique()
puestos = data['puesto'].unique()

departamento_to_municipios = {}
for i, d in enumerate(departamentos):
    dpt = data.loc[data['departamento'] == departamentos[i]]
    mnps = dpt['municipio'].unique()
    #
    departamento_to_municipios[departamentos[i]] = list(mnps)

# municipios_to_puestos = {}
# for i, d in enumerate(departamentos):
#     dpt = data.loc[data['departamento'] == departamentos[i]]
#     mnps = dpt['municipio'].unique()
#     municipios_to_puestos[departamentos[i]] = list(mnps)
#
#     for key, value in municipios_to_puestos.items():
#         mnp = data.loc[data['municipio'] == municipios[i]]
#         psts = mnp['puesto'].unique()
#         municipios_to_puestos[municipios[i]] = list(psts)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],)

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="departamento",
                        options=departamentos,
                        # value="uncased",
                    ),
                    md=2,
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="municipio",
                    ),
                    md=2,
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="puesto",
                    ),
                    md=2,
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="mesa",
                        # options=[{"label": "uncased", "value": "uncased"}],
                        # value="uncased",
                    ),
                    md=2,
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="partido",
                        # options=[{"label": "uncased", "value": "uncased"}],
                        # value="uncased",
                    ),
                    md=2,
                ),
            ]
        ),
    ]
)
app.layout = layout


@callback(Output("municipio", "options"), Input("departamento", "value"))
def update_dropdown_departamento_options(dropdown_departamento):
    if dropdown_departamento is None:
        raise PreventUpdate
    options = departamento_to_municipios[dropdown_departamento]
    return [{'label':o.capitalize(),'value':o} for o in options]


if __name__ == "__main__":
    app.run_server(debug=True, port=8477)