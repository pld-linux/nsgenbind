#
Summary:	Tool to generate dom bindings
Name:		nsgenbind
Version:	0.0.1
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
# Source0-md5:	1b40fc743358b1331f1fe723a3e931bc
Patch0:		bison.patch
URL:		http://www.netsurf-browser.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	netsurf-buildsystem
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a tool to generate javascript to dom bindings from w3c webidl
files and a binding configuration file.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
LDFLAGS="%{rpmldflags}"
export CFLAGS
export LDFLAGS

%{__make} PREFIX=%{_prefix} Q=''

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	Q=''

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/nsgenbind
