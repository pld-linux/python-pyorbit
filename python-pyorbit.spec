
%define		module	pyorbit

Summary:	Python binding for ORBit
Summary(pl):	Wi±zania Pythona do biblioteki ORBit
Name:		python-pyorbit
Version:	2.0.0
Release:	4
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{module}/2.0/%{module}-%{version}.tar.bz2
# Source0-md5:	084d4c51a6778eaceb5dc52e4c91b98a
BuildRequires:	ORBit2-devel >= 2.7.3
BuildRequires:	automake
BuildRequires:	python-devel >= 2.3.2
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python language binding for the ORBit2 CORBA implementation.
It aims to take advantage of new features found in ORBit2 to make
language bindings more efficient.  This includes:
- use of ORBit2 type libraries to generate stubs
- use of the ORBit_small_invoke_stub() call for operation invocation,
  which allows for short circuited invocation on local objects

%description -l pl
Ten pakiet zawiera wi±zania Pythona do ORBit2 - implementacji CORBA.
Jego celem jest wykorzystanie wszystkich nowych mo¿liwo¶ci OBRit2, aby
uczyniæ wi±zania bardziej skutecznymi. Wi±zania umo¿liwiaj±:
- u¿ycie bibliotek typów ORBit2 do generowania szkieletów
- u¿ycie wywo³ania ORBit_small_invoke_stub() do ¿±dania operacji,
  co pozwala na krótkie wywo³ania na lokalnych obiektach.

%package devel
Summary:	Development files for the ORBit Python module
Summary(pt_BR):	Arquivos de desenvolvimento para o módulo ORBit Python
Summary(pl):	Pliki programistyczne dla modu³u Pythona ORBit
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	ORBit2-devel >= 2.7.3
Requires:	python-devel >= 2.3.2

%description devel
This package contains development files needed to develop ORBit Python
based extensions.

%description devel -l pl
Ten pakiet zawiera pliki programistyczne potrzebne do rozwijania
rozszerzeñ bazuj±cych na ORBit Python.

%description devel -l pt_BR
Este pacote contém arquivos de desenvolvimento necessários à criação
de extensões baseadas no ORBit Python.

%prep
%setup -q -n %{module}-%{version}

%build
cp -f /usr/share/automake/config.* .
CPPFLAGS="$(libIDL-config-2 --cflags)"; export CPPFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/{*.la,*.py}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{module}*
%{_pkgconfigdir}/*
