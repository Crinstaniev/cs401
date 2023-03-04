import json

def fetch_data_from_redis(r):
    res = r.get('zz229-proj3-output').decode('utf-8')
    res = json.loads(res)
    timestamp = res['timestamp']
    cpu_percent_ma = res['cpu_percent_ma']
    cpu_percent_history = res['cpu_percent_history']
    cpu_freq_current = res['cpu_freq_current']
    n_pids = res['n_pids']
    virtual_memory_used = res['virtual_memory_used']
    virtual_memory_free = res['virtual_memory_free']
    return dict(
        timestamp=timestamp,
        cpu_percent_history=cpu_percent_history,
        cpu_percent_ma=cpu_percent_ma,
        cpu_freq_current=cpu_freq_current,
        n_pids=n_pids,
        virtual_memory_used=virtual_memory_used,
        virtual_memory_free=virtual_memory_free
    )
