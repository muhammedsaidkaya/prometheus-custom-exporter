import time
from prometheus_client.core import REGISTRY
from prometheus_client import start_http_server


class API():
    """Creates an HTTP Server that listens on a specified port and gathers/serves the metrics

    Methods:
        - constructor
            Args:
                PORT_NUMBER (int): Specifies which socket the API server will listen on
                metric_inputs (list): Contains information about the metrics to be collected

            Usage Example:
                metric_inputs = [
                    MetricInput(
                        metricName="metricName",
                        helpText="helpText",
                        labels=["labelKey"],
                        metrics=[
                            Metric(labelValues=["labelValue"], value=10)
                        ]
                    )
               ]
                API(8080, metric_inputs).listen()

        - listen: Gathers the metrics
            Args:
            Returns:
    """

    def __init__(self, PORT_NUMBER, metric_inputs):
        self.PORT_NUMBER = PORT_NUMBER
        self.metric_inputs = metric_inputs

    def listen(self):
        start_http_server(self.PORT_NUMBER)
        REGISTRY.register(Collector(self.metric_inputs))
        while True:
            time.sleep(1)


class Collector(object):
    """Gathers the metrics

    Methods:
        - constructor
            Args:
                metric_inputs (list): Contains information about the metrics to be collected

            Usage Example:
                metric_inputs = [
                    MetricInput(
                        metricName="metricName",
                        helpText="helpText",
                        labels=["labelKey"],
                        metrics=[
                            Metric(labelValues=["labelValue"], value=10)
                        ]
                    )

               ]
                Collector(metric_inputs)

        - collect: Creates new GaugeMetricFamily and calls its collect function by metric inputs and yield it
            Args:
            Returns:
    """

    def __init__(self, metric_inputs):
        self.metric_inputs = metric_inputs

    def collect(self):
        for metric_input in self.metric_inputs:
            yield metric_input.get_metric()
