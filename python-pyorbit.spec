%include	/usr/lib/rpm/macros.python

%define		module	pyorbit

Summary:	Python binding for ORBit
Summary(pl):	Wi�zania Pythona do biblioteki ORBit
Name:		python-pyorbit
Version:	1.99.7
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/pyorbit/1.99/%{module}-%{version}.tar.bz2
# Source0-md5:	d8ea2fad04442a37b3ab320d47292f25
BuildRequires:	ORBit2-devel >= 2.7.3
BuildRequires:	python-devel >= 2.2.1
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
Ten pakiet zawiera wi�zania Pythona do ORBit2 - implementacji CORBA.
Jego celem jest wykorzystanie wszystkich nowych mo�liwo�ci OBRit2, aby
uczyni� wi�zania bardziej skutecznymi. Wi�zania umo�liwiaj�:
- u�ycie bibliotek typ�w ORBit2 do generowania szkielet�w
- u�ycie wywo�ania ORBit_small_invoke_stub() do ��dania operacji,
  co pozwala na kr�tkie wywo�ania na lokalnych obiektach.

%package devel
Summary:	Development files for the ORBit Python module
Summary(pt_BR):	Arquivos de desenvolvimento para o m�dulo ORBit Python
Summary(pl):	Pliki programistyczne dla modu�u Pythona ORBit
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
Requires:	ORBit2-devel >= 2.5.0
Requires:	python-devel >= 2.1

%description devel
This package contains development files needed to develop ORBit Python
based extensions.

%description devel -l pl
Ten pakiet zawiera pliki programistyczne potrzebne do rozwijania
rozszerze� bazuj�cych na ORBit Python.

%description devel -l pt_BR
Este pacote cont�m arquivos de desenvolvimento necess�rios � cria��o
de extens�es baseadas no ORBit Python.

%prep
%setup -q -n %{module}-%{version}

%build
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
