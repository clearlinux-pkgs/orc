#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x032D3D833A0BA62A (bilboed@bilboed.com)
#
Name     : orc
Version  : 0.4.28
Release  : 13
URL      : https://gstreamer.freedesktop.org/src/orc/orc-0.4.28.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/orc/orc-0.4.28.tar.xz
Source99 : https://gstreamer.freedesktop.org/src/orc/orc-0.4.28.tar.xz.asc
Summary  : Library of Optimized Inner Loops Runtime Compiler
Group    : Development/Tools
License  : BSD-3-Clause
Requires: orc-bin
Requires: orc-lib
Requires: orc-doc
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : meson
BuildRequires : ninja
BuildRequires : python3

%description
ORC - The Oil Runtime Compiler
==============================
(and OIL stands for Optimized Inner Loops)

%package bin
Summary: bin components for the orc package.
Group: Binaries

%description bin
bin components for the orc package.


%package dev
Summary: dev components for the orc package.
Group: Development
Requires: orc-lib
Requires: orc-bin
Provides: orc-devel

%description dev
dev components for the orc package.


%package dev32
Summary: dev32 components for the orc package.
Group: Default
Requires: orc-lib32
Requires: orc-bin
Requires: orc-dev

%description dev32
dev32 components for the orc package.


%package doc
Summary: doc components for the orc package.
Group: Documentation

%description doc
doc components for the orc package.


%package lib
Summary: lib components for the orc package.
Group: Libraries

%description lib
lib components for the orc package.


%package lib32
Summary: lib32 components for the orc package.
Group: Default

%description lib32
lib32 components for the orc package.


%prep
%setup -q -n orc-0.4.28
pushd ..
cp -a orc-0.4.28 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511214700
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1511214700
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/orc-bugreport
/usr/bin/orcc

%files dev
%defattr(-,root,root,-)
/usr/include/orc-0.4/orc-test/orcarray.h
/usr/include/orc-0.4/orc-test/orcprofile.h
/usr/include/orc-0.4/orc-test/orcrandom.h
/usr/include/orc-0.4/orc-test/orctest.h
/usr/include/orc-0.4/orc/orc-stdint.h
/usr/include/orc-0.4/orc/orc.h
/usr/include/orc-0.4/orc/orcarm.h
/usr/include/orc-0.4/orc/orcbytecode.h
/usr/include/orc-0.4/orc/orcbytecodes.h
/usr/include/orc-0.4/orc/orccode.h
/usr/include/orc-0.4/orc/orccompiler.h
/usr/include/orc-0.4/orc/orcconstant.h
/usr/include/orc-0.4/orc/orccpu.h
/usr/include/orc-0.4/orc/orccpuinsn.h
/usr/include/orc-0.4/orc/orcdebug.h
/usr/include/orc-0.4/orc/orcemulateopcodes.h
/usr/include/orc-0.4/orc/orcexecutor.h
/usr/include/orc-0.4/orc/orcfunctions.h
/usr/include/orc-0.4/orc/orcinstruction.h
/usr/include/orc-0.4/orc/orcinternal.h
/usr/include/orc-0.4/orc/orclimits.h
/usr/include/orc-0.4/orc/orcmips.h
/usr/include/orc-0.4/orc/orcmmx.h
/usr/include/orc-0.4/orc/orcneon.h
/usr/include/orc-0.4/orc/orconce.h
/usr/include/orc-0.4/orc/orcopcode.h
/usr/include/orc-0.4/orc/orcparse.h
/usr/include/orc-0.4/orc/orcpowerpc.h
/usr/include/orc-0.4/orc/orcprogram.h
/usr/include/orc-0.4/orc/orcrule.h
/usr/include/orc-0.4/orc/orcsse.h
/usr/include/orc-0.4/orc/orctarget.h
/usr/include/orc-0.4/orc/orcutils.h
/usr/include/orc-0.4/orc/orcvariable.h
/usr/include/orc-0.4/orc/orcx86.h
/usr/include/orc-0.4/orc/orcx86insn.h
/usr/lib64/liborc-0.4.so
/usr/lib64/liborc-test-0.4.so
/usr/lib64/pkgconfig/orc-0.4.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/liborc-0.4.so
/usr/lib32/liborc-test-0.4.so
/usr/lib32/pkgconfig/32orc-0.4.pc
/usr/lib32/pkgconfig/orc-0.4.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/orc/ch01.html
/usr/share/gtk-doc/html/orc/ch02.html
/usr/share/gtk-doc/html/orc/ch03.html
/usr/share/gtk-doc/html/orc/ch04.html
/usr/share/gtk-doc/html/orc/ch05.html
/usr/share/gtk-doc/html/orc/home.png
/usr/share/gtk-doc/html/orc/index.html
/usr/share/gtk-doc/html/orc/left-insensitive.png
/usr/share/gtk-doc/html/orc/left.png
/usr/share/gtk-doc/html/orc/orc-ARM.html
/usr/share/gtk-doc/html/orc/orc-MMX.html
/usr/share/gtk-doc/html/orc/orc-Orc.html
/usr/share/gtk-doc/html/orc/orc-OrcCompiler.html
/usr/share/gtk-doc/html/orc/orc-OrcDebug.html
/usr/share/gtk-doc/html/orc/orc-OrcExecutor.html
/usr/share/gtk-doc/html/orc/orc-OrcOpcode.html
/usr/share/gtk-doc/html/orc/orc-OrcProgram.html
/usr/share/gtk-doc/html/orc/orc-OrcRule.html
/usr/share/gtk-doc/html/orc/orc-PowerPC.html
/usr/share/gtk-doc/html/orc/orc-SSE.html
/usr/share/gtk-doc/html/orc/orc-Utility-functions.html
/usr/share/gtk-doc/html/orc/orc-building.html
/usr/share/gtk-doc/html/orc/orc-concepts.html
/usr/share/gtk-doc/html/orc/orc-misc.html
/usr/share/gtk-doc/html/orc/orc-opcodes.html
/usr/share/gtk-doc/html/orc/orc-program.html
/usr/share/gtk-doc/html/orc/orc-runninging.html
/usr/share/gtk-doc/html/orc/orc-tutorial.html
/usr/share/gtk-doc/html/orc/orc-x86.html
/usr/share/gtk-doc/html/orc/orc.devhelp2
/usr/share/gtk-doc/html/orc/right-insensitive.png
/usr/share/gtk-doc/html/orc/right.png
/usr/share/gtk-doc/html/orc/style.css
/usr/share/gtk-doc/html/orc/up-insensitive.png
/usr/share/gtk-doc/html/orc/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/liborc-0.4.so.0
/usr/lib64/liborc-0.4.so.0.28.0
/usr/lib64/liborc-test-0.4.so.0
/usr/lib64/liborc-test-0.4.so.0.28.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/liborc-0.4.so.0
/usr/lib32/liborc-0.4.so.0.28.0
/usr/lib32/liborc-test-0.4.so.0
/usr/lib32/liborc-test-0.4.so.0.28.0
