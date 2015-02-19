%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define versrc 610

Summary:	Console hex viewer/editor and disassembler
Name:		biew
Version:	6.1.0
Release:	5
License:	GPLv2+
Group:		File tools
Url:		http://biew.sourceforge.net
Source0:	%{name}-%{versrc}.tar.bz2
#patch0 sent upstream (Kharec)
Patch0:		biew610-fix-str-fmt.patch
ExclusiveArch:	%{ix86}

BuildRequires:	gcc-c++, gcc, gcc-cpp

%description
BIEW (Binary vIEW) is a free, portable, advanced file viewer with
built-in editor for binary, hexadecimal and disassembler modes.

It contains a highlight Athlon64/Prescott/K7-Athlon/Cyrix-M2 disassembler,
full preview of MZ, NE, PE, LE, LX, DOS.SYS, NLM, ELF, a.out, arch,
coff32, PharLap, rdoff executable formats, a code guider, and lot of
other features, making it invaluable for examining binary code.

Linux, Unix, QNX, BeOS, DOS, Win32, OS/2 versions are available.

%files
%doc doc/biew_en.txt doc/biew_ru.txt doc/unix.txt doc/release.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man?/%{name}.1*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{versrc}
%patch0 -p0

%build
export CC=gcc
export CXX=g++
#we can't use %configure2_5x because we need the mm/xmm registers
CFLAGS="%{optflags} -mmmx -msse"
CXXFLAGS="%{optflags} -mmmx -msse"
./configure --enable-curses --libdir=%{_libdir} --prefix=%{_prefix}
make TARGET_OS=linux USE_MOUSE=n PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1

install -m 755 %{name} %{buildroot}%{_bindir}/%{name}
cp -a bin_rc/{xlt,skn,*.hlp} %{buildroot}%{_datadir}/%{name}
install -m 0644 doc/biew.1 %{buildroot}%{_mandir}/man1

