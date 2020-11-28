# How do I netcat from AWS Lambda function to  EC2 instance?
You can use netcat or ncat (from nmap)

First, you need to create layer and attach it to your lambda function.
Layers to use:
        1.nmap (contains ncat): https://github.com/pydemo/pyshell/blob/main/lambda-layer/nmap.zip
        2.netcat: https://github.com/pydemo/pyshell/blob/main/lambda-layer/netcat.zip
    


### Find EC2 IP address
Now, in order to netcat to EC@ instance you need to know it's public IP address.

`python -c "import requests; print(requests.get('http://checkip.amazonaws.com').text.rstrip())"`
```
3.136.154.28
```

### EC2
Start netcat on EC2.
```[ec2-user@ip-172-31-41-217 ~]$ nc -n -vv -k -l -p  22000```


### Lambda
Using pyshell call netcat in shell.
`python3 pyshell.py echo -n \"message from Lambda\"\|/opt/nmap/4.14.181-108.257.amzn1.x86_64/bin/ncat 3.136.154.28 22000`


### EC2
Back to EC@, you'll see message in netcat.
```
Connection from 18.191.97.37 port 22000 [tcp/snapenetio] accepted
message from Lambda
```
