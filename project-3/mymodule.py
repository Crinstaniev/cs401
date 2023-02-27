from collections import deque


def handler(input: dict, context: object) -> dict[str, any]:
    cpu_percent_keys = [
        key for key in input.keys() if key.startswith("cpu_percent")]
    cpu_percents = [input[key] for key in cpu_percent_keys]

    if not context.env.get("ma"):
        context.env['ma'] = deque(
            [cpu_percents for _ in range(10)], maxlen=10)

    return dict(
        timestamp=input["timestamp"],
        cpu_percentages_ma=list(context.env['ma']),
        cpu_freq_current=input["cpu_freq_current"],
        n_pids=input["n_pids"],
        virtual_memory_used=input["virtual_memory-used"],
        virtual_memory_free=input["virtual_memory-free"],
    )
