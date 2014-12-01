Summary:	Tool to generate DOM bindings
Summary(pl.UTF-8):	Narzędzie do generowania wiązań DOM
Name:		nsgenbind
Version:	0.1.1
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
# Source0-md5:	18a4163c670be326775f7f05c60dc7bc
URL:		http://www.netsurf-browser.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	netsurf-buildsystem >= 1.2
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
CFLAGS="%{rpmcflags}"
LDFLAGS="%{rpmldflags}"
export CFLAGS
export LDFLAGS

%{__make} \
	PREFIX=%{_prefix} \
	Q=

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	Q=

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README doc/example.bnd
%attr(755,root,root) %{_bindir}/nsgenbind
