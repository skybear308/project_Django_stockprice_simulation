from django.views import generic
from django.views import View
from django.utils import timezone
from django.shortcuts import render

# Sequence related
import numpy as np
import pandas as pd

# plotly
from plotly.offline import plot
from plotly.graph_objs import Scatter
from plotly.tools import FigureFactory as FF

import plotly.graph_objs as go
import datetime

class IndexView(generic.TemplateView):
    template_name = 'chart/index.html'

    def get(self, request, **kwargs):

        ############################
        # candlestick: random number generation

        idx = pd.date_range('2015/01/01', '2015/12/31 23:59', freq='T')
        dn = np.random.randint(2, size=len(idx))*2-1
        rnd_walk = np.cumprod(np.exp(dn*0.0002))*100
        df = pd.Series(rnd_walk, index=idx).resample('B').ohlc()

        ############################
        # Moving average: random number generation

        d1 = datetime.date(2015,1,1)
        d1_list = []

        for i in range(0,365):
            temp = d1 + datetime.timedelta(i)
            d1_list.append(temp)

        X = np.random.randint(80,140,365)
        trace = go.Scatter(x = d1_list, y = X, mode = 'lines', name = 'Moving average line')
        trace_op = go.Scatter(x = d1_list, y = X, mode = 'lines', opacity=0.0, name = '　　　　　')

        ############################

        # plotly configuration
        fig = FF.create_candlestick(df.open, df.high, df.low, df.close, dates=df.index)
        fig.update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            yaxis=dict(
                title = 'Stock price',
            ),
        )
        fig.add_trace(trace)

        fig2 = FF.create_candlestick(df.open, df.high, df.low, df.close, dates=df.index)
        fig2.update_layout(
            height=150,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis = dict(
                title = '',
            ),
        )
        fig2.add_trace(trace_op)

        plot_div = plot(
            fig,
            output_type='div',
            config=dict(
                displayModeBar=True,
            )
        )
        plot_div2 = plot(fig2, output_type='div', config=dict(displayModeBar=False))

        context = {
            'plot_div': plot_div,
            'plot_div2': plot_div2,
        }
        return self.render_to_response(context)


