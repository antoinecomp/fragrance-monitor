import dash_core_components as dcc
import dash_html_components as html

from server import app #, auth, server
from pages import header, attributes, similarity

server = app.server

app.layout = html.Div(
    [
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),

        # Header
        header.layout(),

        dcc.Tabs(
            [
                dcc.Tab(
                    label='Similarité description/commentaires',
                    value='Similarity',
                    children=similarity.layout()
                ),
                dcc.Tab(
                    label='Distribution des attributs dans les description & commentaires',
                    value='Attributes',
                    children=attributes.layout()
                ),
                # dcc.Tab(
                #     label='Markets worldwide',
                #     value='Markets',
                #     children=markets.layout()
                # ),
                # dcc.Tab(
                #     label='Geography',
                #     value='Geography',
                #     children=imap.layout()
                # )
            ]
        )
    ]
)



if __name__ == "__main__":
    app.run_server(debug=False, port=8051)