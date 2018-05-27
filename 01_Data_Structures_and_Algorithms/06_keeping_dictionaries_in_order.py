from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

'''
default dictionary in python3.6+ is also ordered...
we have to use OrderedDict only when we need guarantee the dict to be ordered
across other implementations of Python
'''

print(json.dumps(d))
