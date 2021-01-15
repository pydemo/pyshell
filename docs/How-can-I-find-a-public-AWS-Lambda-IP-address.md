# How can I find a public AWS Lambda IP address?

## Python lambda example
You can do it using Python

```Python
import requests
print(requests.get('http://checkip.amazonaws.com').text.rstrip())
```

Example output:

18.224.38.103


## Test it using pyshell
You can test it using pyshell without authoring another lambda.

```Python
python3 pySend.py python3 -c \"import sys\; sys.path.append\(\'/opt/python/lib/python3.7/si te-packages\'\)\;\\
import requests\; print\(requests.get\(\'http\://checkip.amazonaws.com\'\).text.rstrip\(\)\)\"
```
