from flask import Flask
from flask import render_template
import numpy as np

app = Flask(__name__)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route("/bar")
def bar():
    bar_labels = labels
    bar_values = values
    return render_template('bar_chart.html',
                           title='Bitcoin Monthly Price in USD',
                           max=17000,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/line')
def line():
    x = np.arange(10)
    y = x ** 2
    return render_template('line.html',
                           title='A line plot', x=x, y=y,
                           legend="y=x^2")


@app.route('/scatter')
def scatter():
    rng = np.random.RandomState(0)
    x = rng.randn(100)
    y = rng.randn(100)
    return render_template('scatter.html',
                           title='Scatter plot ', x=x, y=y, zip=zip,
                           legend='Random data')


@app.route('/pie')
def pie():
    return render_template('pie_chart.html',
                           title='Bitcoin Monthly Price in USD',
                           max=17000,
                           set=zip(values, labels, colors))


if __name__ == "__main__":
    app.run(debug=True)
