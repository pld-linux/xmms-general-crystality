Summary:	Realtime plugin for remastering mp3 sound
Summary(pl):	Wtyczka poprawiaj±ca jako¶æ odtwarzania plików mp3
Name:		xmms-general-crystality
Version:	0.92
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://fanthom.math.put.poznan.pl/~gyver/crystality/crystality-plugin-%{version}.tar.gz
# Source0-md5:	960d69bc3b0c90f4aca2631b35417c73
Patch0:		%{name}-Makefile.patch
URL:            http://fanthom.math.put.poznan.pl/~gyver/crystality/
BuildRequires:	xmms-devel >= 1.2.0
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	crystality-plugin

%define		_xmms_plugin_dir	%(xmms-config --general-plugin-dir)

%description
This plugin does mainly four things: 
- adds some sounds in very high frequency range,
- adds some even harmonic distortions,
- adds simple, but nice 3D echo,
- extends stereo.

%description -l pl
Ta wtyczka wykonuje spe³nia g³ównie cztery zadania:
- dodaje d¼wiêki w bardzo wysokim zakresie czêstotliwo¶ci,
- dodaje pewne harmoniczne zniekszta³cenia,
- dodaje prosty efekt echa 3D,
- rozszerzone stereo.

%prep
%setup -q -n crystality-plugin-%{version}
%patch0 -p1

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_xmms_plugin_dir}}

#%%{__make} install \
#	XMMS_PLUGIN=$RPM_BUILD_ROOT%{_libdir}/xmms/General
#	STDIO_PLUGIN=$RPM_BUILD_ROOT%{__bindir}/crystality-stdio
install libcrystality.so $RPM_BUILD_ROOT%{_xmms_plugin_dir}/libcrystality.so
install crystality-stdio $RPM_BUILD_ROOT%{_bindir}/crystality-stdio

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_xmms_plugin_dir}/*
