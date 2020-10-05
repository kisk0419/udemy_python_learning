"""
Tempfile
"""

import tempfile

# 自動削除されるtempfile
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 削除されないtempfile
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('##hello')
        f.seek(0)
        print(f.read())

# 自動削除されるtemp directory
with tempfile.TemporaryDirectory() as td:
    print(td)
