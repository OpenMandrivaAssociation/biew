%define name	biew
%define version	6.1.0
%define versrc	610
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Console hex viewer/editor and disassembler
License:	GPLv2+
Group:		File tools
URL:		http://biew.sourceforge.net
Source:		%{name}-%{versrc}.tar.bz2
Patch0:		biew-fix-str-fmt.patch
BuildRoot:	%_tmppath/%name-%version-buildroot
ExclusiveArch:	%ix86

%description
BIEW (Binary vIEW) is a free, portable, advanced file viewer with
built-in editor for binary, hexadecimal and disassembler modes.

It contains a highlight Athlon64/Prescott/K7-Athlon/Cyrix-M2 disassembler,
full preview of MZ, NE, PE, LE, LX, DOS.SYS, NLM, ELF, a.out, arch,
coff32, PharLap, rdoff executable formats, a code guider, and lot of
other features, making it invaluable for examining binary code.

Linux, Unix, QNX, BeOS, DOS, Win32, OS/2 versions are available.

%prep
%setup -q -n %{name}-%{versrc}
%patch0 -p0

%build
#we can't use %configure2_5x because we need the mm/xmm registers
./configure --enable-curses --libdir=%{_libdir} --prefix=%_prefix
make TARGET_OS=linux USE_MOUSE=n PREFIX=%_prefix

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}{%{_bindir},%{_datadir}/%{name},%{_mandir}/man1}

install -m 755 biew $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a bin_rc/{xlt,skn,*.hlp} $RPM_BUILD_ROOT%{_datadir}/%{name}
install doc/biew.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/biew_en.txt doc/biew_ru.txt doc/unix.txt doc/release.txt

%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man?/%{name}.1*
