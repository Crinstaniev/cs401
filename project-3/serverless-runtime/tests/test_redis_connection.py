from importlib.machinery import SourceFileLoader


def test_redis_connection():
    Input = SourceFileLoader(
        'input', 'severless-runtime/utils/input.py').load_module().Input
    input = Input('67.159.94.11', 6379)
    metrics = input.fetch_metrics()
    print(type(metrics))
    print(metrics)
