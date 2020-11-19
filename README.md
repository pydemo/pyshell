# python lambdash
lambdash using Python

inspired by https://github.com/alestic/lambdash (only local and lambda are in Python)


## SSH port
```
 sudo netstat -tnlp | grep :22
```



## ifconfig

python3 pyshell.py /opt/net-tools/4.14.181-108.257.amzn1.x86_64/ifconfig
```
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536  metric 1
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 91  bytes 12819 (12.5 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 91  bytes 12819 (12.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

telemetry1_sb: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500  metric 1
        inet 169.254.79.130  netmask 255.255.255.252  broadcast 0.0.0.0
        ether 46:9d:7b:26:13:e4  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

vinternal_1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500  metric 1
        inet 169.254.76.1  netmask 255.255.254.0  broadcast 0.0.0.0
        ether 22:8e:ab:10:23:69  txqueuelen 1000  (Ethernet)
        RX packets 5  bytes 414 (414.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 6  bytes 386 (386.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

vtarget_1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500  metric 1
        inet 169.254.79.1  netmask 255.255.255.255  broadcast 0.0.0.0
        ether 0e:c5:e3:3e:bc:57  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```


## netstat

python3 pyshell.py /opt/net-tools/4.14.181-108.257.amzn1.x86_64/netstat
```
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 localhost:54516         localhost:etlservicemgr ESTABLISHED
tcp        0    480 localhost:etlservicemgr localhost:54516         ESTABLISHED
udp        0      0 169.254.79.1:41732      169.254.79:sieve-filter ESTABLISHED
Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node   Path
```


## python path

time python3 pyshell.py python -c \\"import sys\\;print\\(sys.executable\\)\\"
```
/var/lang/bin/python

real    0m0.597s
user    0m0.131s
sys     0m0.010s
```

## env
python3 pyshell.py env
```
AWS_LAMBDA_FUNCTION_VERSION=$LATEST
AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEFwaCXVzLWVhc3QtMiJGMEQCIGqupJNWmbhomsM2ilNOfPrN6CEjwBJgDRVAbkSn1mtEAiBP2ZlDkhylpmsxK2taUB/75+b0pEc9IAVSXm97Lz02XSrPAQjF//////////8BEAAaDDg4NzUyNzE0NjU3NSIMt6FZ5yxxSgFdYgP2KqMBbVi48qd6bS/DdITn118dnaLP4gmyswzWNf4sbQEETN/jebDDKzrJFDDl7d3qdEL3mMqbnFIOMldRfiC51TGYFJ/Zov9pqyG+nOD9We6xob4pohxyIUShKp9E8JOrCDAENhnbPrwvNh6K4Q666fZgZAe2fG2MGt1PmTVr/t7Bsu2pwZFGqp5eIYR46DaykkIEQletoJCIUtY2XISjqTqhDMvjIzD5zrv9BTrhAcXmRSO8T+uDGcswkfumYlmlad1TqnmNG0lC9HLsCAr0k2XkTlrPkGD5P77vtbkOCubzLNiwOrUHD64ohsP8c+rfX3hJk6u9bgj7dDsUmHdbkFP0gBW1WiNB9kVfc6Js/wTQkNoXV6ECSNC4rhIzURPXGipvcdV49uBOu9MjKm6J6aGjqSWJVA+Ewew6SV6Ju4JUJMJHXYhE5R/vWxcTlG68sRHnxRO2VkmYlQ/MLYoyOAfcsQnFq6XB5G36JWQiQOOe9YSwelneyYcAKLxgz5KolVtfMJTkrNDx399laW1Brg==
LAMBDA_TASK_ROOT=/var/task
LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
AWS_LAMBDA_LOG_GROUP_NAME=/aws/lambda/pyshell
AWS_LAMBDA_RUNTIME_API=127.0.0.1:9001
AWS_LAMBDA_LOG_STREAM_NAME=2020/11/13/[$LATEST]0a3947147feb414c882589c8037ffcc5
AWS_EXECUTION_ENV=AWS_Lambda_python3.7
AWS_XRAY_DAEMON_ADDRESS=169.254.79.2:2000
AWS_LAMBDA_FUNCTION_NAME=pyshell
PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
AWS_DEFAULT_REGION=us-east-2
PWD=/var/task
AWS_SECRET_ACCESS_KEY=vFjMR3NKengJXoHl4JgNc5L8s28abgoWGgBllfoh
LAMBDA_RUNTIME_DIR=/var/runtime
LANG=en_US.UTF-8
AWS_REGION=us-east-2
TZ=:UTC
AWS_ACCESS_KEY_ID=ASIA45JF5QRHTWVRD2NB
SHLVL=1
_AWS_XRAY_DAEMON_ADDRESS=169.254.79.2
_AWS_XRAY_DAEMON_PORT=2000
_X_AMZN_TRACE_ID=Root=1-5faee7a0-799d88587267d6e515923c39;Parent=345c2385132090ea;Sampled=0
AWS_XRAY_CONTEXT_MISSING=LOG_ERROR
_HANDLER=lambda_function.lambda_handler
AWS_LAMBDA_FUNCTION_MEMORY_SIZE=128
_=/usr/bin/env
```







## Python venv
python3 pyshell python3 -m venv /tmp/test
```
real    0m44.041s
user    0m0.242s
sys     0m0.025s
```
## Python venv size

python3 pyshell du -csh --block-size=1M /tmp/test
```
13      /tmp/test
13      total
```



## Shell bootstrap layer 
python3 pyshell ldd /opt/bin/git
(https://s3.amazonaws.com/cloudacademylabs-customruntimelab-1nqi07u9duqck/bash-lambda-layer/layer.zip)

```
        linux-vdso.so.1 =>  (0x00007ffd076e0000)
        libz.so.1 => /lib64/libz.so.1 (0x00007fcfefcf2000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fcfefad6000)
        librt.so.1 => /lib64/librt.so.1 (0x00007fcfef8ce000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fcfef500000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fcfeff08000)
```

## AWS Lambda Libc version
python3 pyshell /lib64/libc.so.6 --version
```
GNU C Library (GNU libc) stable release version 2.17, by Roland McGrath et al.
Copyright (C) 2012 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
Compiled by GNU CC version 4.8.5 20150623 (Red Hat 4.8.5-28).
Compiled on a Linux 3.2.5 system on 2020-02-11.
Available extensions:
        The C stubs add-on version 2.1.2.
        crypt add-on version 2.1 by Michael Glad and others
        GNU Libidn by Simon Josefsson
        Native POSIX Threads Library by Ulrich Drepper et al
        BIND-8.2.3-T5B
        RT using linux kernel aio
libc ABIs: UNIQUE IFUNC
For bug reporting instructions, please see:
<http://www.gnu.org/software/libc/bugs.html>.
```


## Number of processors
time python3 pyshell nproc
```
2
```
## Top running processes
python3 pyshell ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
```
PID  PPID CMD                         %MEM %CPU
    1     0 /var/rapid/init --enable-ex  3.4  0.0
    7     1 /var/lang/bin/python3.7 /va  9.1  0.0
   30     7 ps -eo pid,ppid,cmd,%mem,%c  1.1  0.0
```

## Lambda Linux realease (cat /etc/os-release)
python3 pyshell cat /etc/os-release
```
NAME="Amazon Linux AMI"
VERSION="2018.03"
ID="amzn"
ID_LIKE="rhel fedora"
VERSION_ID="2018.03"
PRETTY_NAME="Amazon Linux AMI 2018.03"
ANSI_COLOR="0;33"
CPE_NAME="cpe:/o:amazon:linux:2018.03:ga"
HOME_URL="http://aws.amazon.com/amazon-linux-ami/"
VARIANT_ID="202010122208-al2018.03.416.0"
```
## uname -r
python3 pyshell uname -r
```
4.14.193-110.317.amzn2.x86_64
```
## cat /proc/version
python3 pyshell cat /proc/version
```
Linux version 4.14.193-110.317.amzn2.x86_64 (mockbuild@ip-10-0-1-32) 
(gcc version 7.3.1 20180712 (Red Hat 7.3.1-9) (GCC)) #1 SMP Fri Sep 11 23:37:26 UTC 2020
```
## cat /proc/cpuinfo
python3 pyshell cat /proc/cpuinfo
```
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 62
model name      : Intel(R) Xeon(R) Processor @ 2.50GHz
stepping        : 4
microcode       : 0x1
cpu MHz         : 2500.010
cache size      : 36608 KB
physical id     : 0
siblings        : 2
core id         : 0
cpu cores       : 2
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust smep erms smap xsaveopt arat md_clear arch_capabilities
bugs            : spectre_v1 spectre_v2 spec_store_bypass swapgs
bogomips        : 5000.02
clflush size    : 64
cache_alignment : 64
address sizes   : 46 bits physical, 48 bits virtual
power management:

processor       : 1
vendor_id       : GenuineIntel
cpu family      : 6
model           : 62
model name      : Intel(R) Xeon(R) Processor @ 2.50GHz
stepping        : 4
microcode       : 0x1
cpu MHz         : 2500.010
cache size      : 36608 KB
physical id     : 0
siblings        : 2
core id         : 1
cpu cores       : 2
apicid          : 1
initial apicid  : 1
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust smep erms smap xsaveopt arat md_clear arch_capabilities
bugs            : spectre_v1 spectre_v2 spec_store_bypass swapgs
bogomips        : 5000.02
clflush size    : 64
cache_alignment : 64
address sizes   : 46 bits physical, 48 bits virtual
power management:
```

## ps -ef
python3 pyshell ps -ef
```
UID        PID  PPID  C STIME TTY          TIME CMD
994          1     0  0 16:41 ?        00:00:00 /var/rapid/init --enable-extensions --bootstrap /var/runtime/bootstrap
994          7     1  0 16:41 ?        00:00:00 /var/lang/bin/python3.7 /var/runtime/bootstrap
994         24     7  0 16:50 ?        00:00:00 ps -ef
```


##  df -h


ubuntu@ip-172-31-45-165:~/lambdash$ time python3 pylambdash df -h
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       7.8G  6.6G  1.3G  85% /
/dev/vdb        1.5G   31M  1.4G   3% /dev
/dev/vdd        526M  872K  514M   1% /tmp
/dev/vdc         22M   22M     0 100% /opt
```

