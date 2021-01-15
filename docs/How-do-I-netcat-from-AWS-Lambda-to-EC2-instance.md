# How do I netcat from AWS Lambda function to  EC2 instance?
You can use netcat or ncat (from nmap)

First, you need to create layer and attach it to your lambda function.

### Layers to use:
        nmap (contains ncat): https://github.com/pydemo/pyshell/blob/main/lambda-layer/nmap.zip
        or
        netcat: https://github.com/pydemo/pyshell/blob/main/lambda-layer/netcat.zip
    


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

```
################################################################################
Ncat: Version 7.91 ( https://nmap.org/ncat )
NCAT DEBUG: Using system default trusted CA certificates and those in /home/ec2-user/build/nmap/share/ncat/ca-bundle.crt.
NCAT DEBUG: Unable to load trusted CA certificates from /home/ec2-user/build/nmap/share/ncat/ca-bundle.crt: error:02001002:system library:fopen:No such file or directory
libnsock nsock_iod_new2(): nsock_iod_new (IOD #1)
libnsock nsock_connect_tcp(): TCP connection requested to 3.138.189.76:22000 (IOD #1) EID 8
libnsock nsock_trace_handler_callback(): Callback: CONNECT SUCCESS for EID 8 [3.138.189.76:22000]
Ncat: Connected to 3.138.189.76:22000.
libnsock nsock_iod_new2(): nsock_iod_new (IOD #2)
libnsock nsock_read(): Read request from IOD #1 [3.138.189.76:22000] (timeout: -1ms) EID 18
libnsock nsock_readbytes(): Read request for 0 bytes from IOD #2 [peer unspecified] EID 26
libnsock nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 26 [peer unspecified] (19 bytes): message from Lambda
libnsock nsock_write(): Write request for 19 bytes to IOD #1 EID 35 [3.138.189.76:22000]
libnsock nsock_trace_handler_callback(): Callback: WRITE SUCCESS for EID 35 [3.138.189.76:22000]
libnsock nsock_readbytes(): Read request for 0 bytes from IOD #2 [peer unspecified] EID 42
libnsock nsock_trace_handler_callback(): Callback: READ EOF for EID 42 [peer unspecified]
libnsock nsock_trace_handler_callback(): Callback: READ EOF for EID 18 [3.138.189.76:22000]
Ncat: 19 bytes sent, 0 bytes received in 0.16 seconds.
libnsock nsock_iod_delete(): nsock_iod_delete (IOD #1)
libnsock nsock_iod_delete(): nsock_iod_delete (IOD #2)
################################################################################
```

### EC2
Back to EC2, you'll see message in ncat.
```
Ncat: Version 7.50 ( https://nmap.org/ncat )
Ncat: Listening on :::22000
Ncat: Listening on 0.0.0.0:22000
Ncat: Connection from 3.136.22.99.
Ncat: Connection from 3.136.22.99:50082.
message from LambdaNCAT DEBUG: Closing fd 5.

```
