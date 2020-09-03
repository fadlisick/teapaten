import pytest

from paten import Paten
from paten.error import ArgumentNameInvalidError


def test_http_trigger():
    app = Paten("pytest")

    @app.http_trigger("req", methods=["GET"], route="/pytest")
    @app.out_queue("arg_name", queue_name="example-queue")
    @app.out_http()
    def example(req, arg_name):
        pass


def test_http_trigger_name_error():
    app = Paten("pytest")

    with pytest.raises(ArgumentNameInvalidError):
        @app.http_trigger("req", methods=["GET"], route="/pytest")
        @app.out_http()
        def example(req_different_name):
            pass

    with pytest.raises(ArgumentNameInvalidError):
        @app.http_trigger("req", methods=["GET"], route="/pytest")
        @app.out_queue("arg_name", queue_name="example-queue")
        @app.out_http()
        def example(req, arg_name_different):
            pass


def test_timer_trigger():
    app = Paten("pytest")

    @app.timer_trigger("timer", schedule="0 0 19 * * *")
    def example(timer):
        pass


def test_timer_trigger_name_error():
    app = Paten("pytest")

    with pytest.raises(ArgumentNameInvalidError):
        @app.timer_trigger("timer", schedule="0 0 19 * * *")
        def example(timer_name_different):
            pass


def test_queue_trigger():
    app = Paten("pytest")

    @app.queue_trigger("msg", queue_name="example-queue")
    def example(msg):
        pass


def test_queue_trigger_name_error():
    app = Paten("pytest")

    with pytest.raises(ArgumentNameInvalidError):
        @app.queue_trigger("msg", queue_name="example-queue")
        def example(msg_name_different):
            pass
