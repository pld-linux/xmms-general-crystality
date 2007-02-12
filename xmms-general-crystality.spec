Summary:	Realtime XMMS plugin for remastering MP3 sound
Summary(pl.UTF-8):	Wtyczka dla XMMS-a poprawiająca jakość odtwarzania plików MP3
Name:		xmms-general-crystality
Version:	0.92
Release:	4
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://fanthom.math.put.poznan.pl/~gyver/crystality/crystality-plugin-%{version}.tar.gz
# Source0-md5:	960d69bc3b0c90f4aca2631b35417c73
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-gcc33.patch
URL:		http://fanthom.math.put.poznan.pl/~gyver/crystality/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.0
Requires:	xmms
Obsoletes:	crystality-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin does mainly four things:
- adds some sounds in very high frequency range,
- adds some even harmonic distortions,
- adds simple, but nice 3D echo,
- extends stereo.

%description -l pl.UTF-8
Ta wtyczka wykonuje głównie cztery zadania:
- dodaje dźwięki w bardzo wysokim zakresie częstotliwości,
- dodaje pewne harmoniczne zniekształcenia,
- dodaje prosty efekt echa 3D,
- rozszerzone stereo.

%prep
%setup -q -n crystality-plugin-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{xmms_general_plugindir}}

#%%{__make} install \
#	XMMS_PLUGIN=$RPM_BUILD_ROOT%{_libdir}/xmms/General
#	STDIO_PLUGIN=$RPM_BUILD_ROOT%{__bindir}/crystality-stdio
install libcrystality.so $RPM_BUILD_ROOT%{xmms_general_plugindir}
install crystality-stdio $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{xmms_general_plugindir}/*
