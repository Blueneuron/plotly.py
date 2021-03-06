import _plotly_utils.basevalidators


class AutocolorscaleValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='autocolorscale',
        parent_name='scatter.marker.line',
        **kwargs
    ):
        super(AutocolorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            implied_edits={},
            role='style',
            **kwargs
        )
