#!/bin/bash
#Part of PureDarwin Devs post by InsaneDarwin in https://www.pd-devs.org/viewtopic.php?f=10&t=4#p11
cd libdispatch
mkdir -p BUILD.hdrs/obj BUILD.hdrs/sym BUILD.hdrs/dst
sudo xcodebuild install -project libdispatch.xcodeproj -target libfirehose_kernel -sdk macosx ARCHS='x86_64 i386' SRCROOT=$PWD OBJROOT=$PWD/obj SYMROOT=$PWD/sym DSTROOT=$PWD/dst
sudo ditto $PWD/dst/usr/local `xcrun -sdk macosx -show-sdk-path`/usr/local
cd ..