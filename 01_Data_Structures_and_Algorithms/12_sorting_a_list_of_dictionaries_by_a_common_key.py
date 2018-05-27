from operator import itemgetter
from pprint import pprint

rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]

row_by_uid = sorted(rows, key=itemgetter('uid'))
pprint(row_by_uid)

row_by_lf_name = sorted(rows, key=itemgetter('lname', 'fname'))
pprint(row_by_lf_name)
