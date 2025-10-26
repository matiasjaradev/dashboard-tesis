from dash import Dash, html


app = Dash()


app.layout = html.Div(
    className="main-div"
)



if __name__ == "__main__": 
 app.run(port=10000)