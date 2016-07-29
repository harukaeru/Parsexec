# Parsexec
## Install
```sh
$ pip install git+https://github.com/harukaeru/Parsexec.git
```

## Usage
<i>some.md</i>
<pre><code class="lang-python">This is Test Code
```
print(4)
print(1 + 2)
print(datetime.today())
```
</code></pre>

<i>~/.import_classes.py</i>
```python
from datetime import datetime
datetime
```

```sh
$ parsexec some.md
----- PrintOut -----
data: 4
type: <class 'int'>
data: 3
type: <class 'int'>
data: 2016-07-29 12:21:29.902603
type: <class 'datetime.datetime'>
----- source -----
from datetime import datetime
print(4)
print(1 + 2)
print(datetime.today())
```
