def _init():
    global _global_dict
    _global_dict = {}
    _global_dict.setdefault('list_for_vis', [])
    _global_dict.setdefault('batch_number', 0)

def set_value_int(key, value):
    _global_dict[key] = value

def set_value_list(key, value):
    _global_dict.setdefault(key, value)

def get_value(key):
    try:
        return _global_dict[key]
    except:
        print('Get Value'+key+'Failed\r\n')
