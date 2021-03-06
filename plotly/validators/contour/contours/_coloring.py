import _plotly_utils.basevalidators


class ColoringValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='coloring', parent_name='contour.contours', **kwargs
    ):
        super(ColoringValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            values=['fill', 'heatmap', 'lines', 'none'],
            **kwargs
        )
