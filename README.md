# python-lambdash
lambdash using Python

inspired by https://github.com/alestic/lambdash (only local and lambda are in Python)

## Shell bootstrap layer 
(https://s3.amazonaws.com/cloudacademylabs-customruntimelab-1nqi07u9duqck/bash-lambda-layer/layer.zip)
python3 pyshell ldd /opt/bin/git
```
        linux-vdso.so.1 =>  (0x00007ffd076e0000)
        libz.so.1 => /lib64/libz.so.1 (0x00007fcfefcf2000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fcfefad6000)
        librt.so.1 => /lib64/librt.so.1 (0x00007fcfef8ce000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fcfef500000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fcfeff08000)
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

