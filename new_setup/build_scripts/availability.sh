#!/bin/bash
#Part of PureDarwin Devs post by InsaneDarwin in https://www.pd-devs.org/viewtopic.php?f=10&t=4#p11
cd AvailabilityVersions 
mkdir -p dst 
make install SRCROOT=$PWD DSTROOT=$PWD/dst
sudo ditto $PWD/dst/usr/local `xcrun -sdk macosx -show-sdk-path`/usr/local
cd ..