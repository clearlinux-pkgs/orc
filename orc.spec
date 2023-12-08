#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0x5D2EEE6F6F349D7C (tim@centricular.com)
#
Name     : orc
Version  : 0.4.34
Release  : 40
URL      : https://gstreamer.freedesktop.org/src/orc/orc-0.4.34.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/orc/orc-0.4.34.tar.xz
Source1  : https://gstreamer.freedesktop.org/src/orc/orc-0.4.34.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: orc-bin = %{version}-%{release}
Requires: orc-lib = %{version}-%{release}
Requires: orc-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
ORC - The Oil Runtime Compiler
==============================
(and OIL stands for Optimized Inner Loops)

%package bin
Summary: bin components for the orc package.
Group: Binaries
Requires: orc-license = %{version}-%{release}

%description bin
bin components for the orc package.


%package dev
Summary: dev components for the orc package.
Group: Development
Requires: orc-lib = %{version}-%{release}
Requires: orc-bin = %{version}-%{release}
Provides: orc-devel = %{version}-%{release}
Requires: orc = %{version}-%{release}

%description dev
dev components for the orc package.


%package dev32
Summary: dev32 components for the orc package.
Group: Default
Requires: orc-lib32 = %{version}-%{release}
Requires: orc-bin = %{version}-%{release}
Requires: orc-dev = %{version}-%{release}

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
Requires: orc-license = %{version}-%{release}

%description lib
lib components for the orc package.


%package lib32
Summary: lib32 components for the orc package.
Group: Default
Requires: orc-license = %{version}-%{release}

%description lib32
lib32 components for the orc package.


%package license
Summary: license components for the orc package.
Group: Default

%description license
license components for the orc package.


%prep
%setup -q -n orc-0.4.34
cd %{_builddir}/orc-0.4.34
pushd ..
cp -a orc-0.4.34 build32
popd
pushd ..
cp -a orc-0.4.34 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702042687
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../build32;
meson test -C builddir --print-errorlogs || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
mkdir -p %{buildroot}/usr/share/package-licenses/orc
cp %{_builddir}/orc-%{version}/COPYING %{buildroot}/usr/share/package-licenses/orc/91117211918b830ec63d6b8ef8c4dbd95f286c99 || :
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/orc-bugreport
/V3/usr/bin/orcc
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
/usr/lib64/pkgconfig/orc-test-0.4.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/liborc-0.4.so
/usr/lib32/liborc-test-0.4.so
/usr/lib32/pkgconfig/32orc-0.4.pc
/usr/lib32/pkgconfig/32orc-test-0.4.pc
/usr/lib32/pkgconfig/orc-0.4.pc
/usr/lib32/pkgconfig/orc-test-0.4.pc

%files doc
%defattr(0644,root,root,0755)
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
/V3/usr/lib64/liborc-0.4.so.0.34.0
/V3/usr/lib64/liborc-test-0.4.so.0.34.0
/usr/lib64/liborc-0.4.so.0
/usr/lib64/liborc-0.4.so.0.34.0
/usr/lib64/liborc-test-0.4.so.0
/usr/lib64/liborc-test-0.4.so.0.34.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/liborc-0.4.so.0
/usr/lib32/liborc-0.4.so.0.34.0
/usr/lib32/liborc-test-0.4.so.0
/usr/lib32/liborc-test-0.4.so.0.34.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/orc/91117211918b830ec63d6b8ef8c4dbd95f286c99
