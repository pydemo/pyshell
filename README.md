# python-lambdash
lambdash using Python


inspired by https://github.com/alestic/lambdash (only in Python)

##  ls -all /

```
ubuntu@ip-172-31-45-165:~/lambdash$ time python3 pylambdash ls -all /
total 76
dr-xr-xr-x 21 root         root 4096 Oct 12 22:10 .
dr-xr-xr-x 21 root         root 4096 Oct 12 22:10 ..
dr-xr-xr-x  2 root         root 4096 Oct 12 22:12 bin
dr-xr-xr-x  2 root         root 4096 Jan  6  2012 boot
drwxr-xr-x  2 root         root 4096 Nov 10 14:35 dev
drwxr-xr-x 50 root         root 4096 Oct 12 22:12 etc
drwxr-xr-x  2 root         root 4096 Jan  6  2012 home
dr-xr-xr-x  5 root         root 4096 Oct 12 22:11 lib
dr-xr-xr-x  5 root         root 4096 Oct 12 22:12 lib64
drwxr-xr-x  2 root         root 4096 Jan  6  2012 media
drwxr-xr-x  2 root         root 4096 Jan  6  2012 mnt
drwxr-xr-x  7 root         root  122 Nov 10 03:32 opt
dr-xr-xr-x 68 root         root    0 Nov 10 14:42 proc
dr-xr-x---  2 root         root 4096 Jan  6  2012 root
dr-xr-xr-x  2 root         root 4096 Oct 12 22:12 sbin
drwxr-xr-x  2 root         root 4096 Jan  6  2012 selinux
drwxr-xr-x  2 root         root 4096 Jan  6  2012 srv
drwxr-xr-x  2 root         root 4096 Jan  6  2012 sys
drwx------  2 sbx_user1051  991 4096 Nov 10 14:42 tmp
drwxr-xr-x 13 root         root 4096 Oct 12 22:10 usr
drwxr-xr-x 24 root         root 4096 Oct 12 22:12 var
```

##  df -h

```
ubuntu@ip-172-31-45-165:~/lambdash$ time python3 pyshell df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       7.8G  6.6G  1.3G  85% /
/dev/vdb        1.5G   31M  1.4G   3% /dev
/dev/vdd        526M  872K  514M   1% /tmp
/dev/vdc         22M   22M     0 100% /opt
```

