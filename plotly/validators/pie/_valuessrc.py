import _plotly_utils.basevalidators


class ValuessrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(self, plotly_name='valuessrc', parent_name='pie', **kwargs):
        super(ValuessrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )