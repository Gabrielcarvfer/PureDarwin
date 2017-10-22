#!/bin/bash
#Part of PureDarwin Devs post by InsaneDarwin in https://www.pd-devs.org/viewtopic.php?f=10&t=4#p11
cd libplatform
sudo ditto $PWD/include `xcrun -sdk macosx -show-sdk-path`/usr/local/include   
cd ..