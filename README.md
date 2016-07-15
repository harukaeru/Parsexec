<i>some.md</i>
<pre><code class="lang-python">This is Test Code
```
print(4)
print(1 + 2)
print(datetime.today())
```
</code></pre>

<i>import_classes.py</i>
```python
from datetime import datetime
datetime
```

```sh
$ ./parse_source_print.py some.txt
----- Out -----
data: 4
class: <class 'int'>
data: 3
class: <class 'int'>
data: 2016-07-15 12:33:18.638318
class: <class 'datetime.datetime'>
----- source -----
from datetime import datetime
print(4)
print(1 + 2)
print(datetime.today())

```
