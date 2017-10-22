#!/bin/bash
#Part of PureDarwin Devs post by InsaneDarwin in https://www.pd-devs.org/viewtopic.php?f=10&t=4#p11
sh ./dtrace.sh
sh ./availability.sh
sh ./xnu_prep.sh
sh ./libplatform.sh
sh ./libdispatch.sh
sh ./xnu_build.sh