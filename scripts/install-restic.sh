#!/bin/bash
if [ -f /etc/redhat-release ] ; then
    yum install yum-plugin-copr
    yum copr enable copart/restic
    yum install restic
elif [ -f /etc/debian_version ] ; then
    apt-get install restic
fi
