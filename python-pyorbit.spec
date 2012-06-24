
%include	/usr/lib/rpm/macros.python

%define		module	pyorbit

Summary:	Python binding for ORBit
Summary(pl):	Wi�zania Pythona do biblioteki ORBit
Name:		python-pyorbit
Version:	1.99.1
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/pyorbit/1.99/%{module}-%{version}.tar.gz
BuildRequires:	ORBit2-devel >= 2.5.0
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

%package devel
Summary:	Development files for the ORBit Python module
Summary(pt_BR):	Arquivos de desenvolvimento para o m�dulo ORBit Python
Summary(pl):	Developerskie pliki dla modu�u Pythona ORBit
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
Requires:	python-devel >= 2.1
Requires:	ORBit-devel >= 2.5.0

%description devel
This package contains development files needed to develop ORBit Python
based extensions.

%description devel -l pl
Ten pakiet zawiera pliki developerskie potrzebne do rozwijania
rozszerze� bazuj�cych na ORBit Python.

%description devel -l pt_BR
Este pacote cont�m arquivos de desenvolvimento necess�rios � cria��o
de extens�es baseadas no ORBit Python.

%prep
%setup -q -n %{module}-%{version}

%build
CPPFLAGS="$(libIDL-config --cflags)"; export CPPFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{py_sitedir}/*.so
%attr(755,root,root) %{py_sitedir}/*.la

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*
%{_includedir}/%{module}*
