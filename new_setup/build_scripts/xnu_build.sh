#!/bin/bash
#Part of PureDarwin Devs post by InsaneDarwin in https://www.pd-devs.org/viewtopic.php?f=10&t=4#p11
cd xnu
make SDKROOT=macosx ARCH_CONFIGS=X86_64 KERNEL_CONFIGS=RELEASE
