class BaiduMapChartBuilder:
    def __init__(self):
        self.chart_config = {
            "title": {},
            "tooltip": {"trigger": "item"},
            "bmap": {"mapStyle": {"styleJson": []}},
            "series": []
        }

    def set_title(self, text, subtext, sublink, left):
        self.chart_config["title"] = {
            "text": text,
            "subtext": subtext,
            "sublink": sublink,
            "left": left
        }
        return self

    def set_tooltip(self, trigger):
        self.chart_config["tooltip"]["trigger"] = trigger
        return self

    def set_bmap(self, center, zoom, roam, map_style):
        self.chart_config["bmap"]["center"] = center
        self.chart_config["bmap"]["zoom"] = zoom
        self.chart_config["bmap"]["roam"] = roam
        self.chart_config["bmap"]["mapStyle"]["styleJson"] = map_style
        return self

    def add_scatter_series(self, name, data, symbol_size, encode_value, label_formatter, label_position, label_show, emphasis_show):
        scatter_series = {
            "name": name,
            "type": "scatter",
            "coordinateSystem": "bmap",
            "data": list(data[:5]),  # Convert slice to list
            "symbolSize": symbol_size,
            "encode": {"value": encode_value},
            "label": {
                "formatter": label_formatter,
                "position": label_position,
                "show": label_show
            },
            "emphasis": {"label": {"show": emphasis_show}}
        }
        self.chart_config["series"].append(scatter_series)
        return self

    def add_effect_scatter_series(self, name, data, symbol_size, encode_value, show_effect_on, ripple_effect_brush_type, label_formatter, label_position, label_show, item_style, emphasis_scale, zlevel):
        effect_scatter_series = {
            "name": name,
            "type": "effectScatter",
            "coordinateSystem": "bmap",
            "data": data,
            "symbolSize": symbol_size,
            "encode": {"value": encode_value},
            "showEffectOn": show_effect_on,
            "rippleEffect": {"brushType": ripple_effect_brush_type},
            "label": {
                "formatter": label_formatter,
                "position": label_position,
                "show": label_show
            },
            "itemStyle": {"shadowBlur": item_style["shadowBlur"], "shadowColor": item_style["shadowColor"]},
            "emphasis": {"scale": emphasis_scale},
            "zlevel": zlevel
        }
        self.chart_config["series"].append(effect_scatter_series)
        return self

    def build(self):
        return self.chart_config