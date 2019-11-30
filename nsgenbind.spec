Summary:	Tool to generate DOM bindings
Summary(pl.UTF-8):	Narzędzie do generowania wiązań DOM
Name:		nsgenbind
Version:	0.7
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
# Source0-md5:	71e3d304d6314cb810a035d1931776c9
URL:		http://www.netsurf-browser.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	netsurf-buildsystem >= 1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a tool to generate JavaScript to DOM bindings from W3C webidl
files and a binding configuration file.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzie do generowania wiązań JavaScriptu do DOM
z plików W3C webidl oraz pliku konfiguracyjnego wiązań.

%prep
%setup -q

%build
export AR="%{__ar}"
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"

%{__make} \
	PREFIX=%{_prefix} \
	Q=

%install
rm -rf $RPM_BUILD_ROOT

export AR="%{__ar}"
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	Q=

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/nsgenbind
