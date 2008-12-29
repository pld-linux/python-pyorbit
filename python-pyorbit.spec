%define		module	pyorbit

Summary:	Python binding for ORBit
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki ORBit
Name:		python-pyorbit
Version:	2.24.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pyorbit/2.24/%{module}-%{version}.tar.bz2
# Source0-md5:	574593815e75ee6e98062c75d6d1581f
# http://bugzilla.gnome.org/show_bug.cgi?id=565967
Patch0:		%{name}-libtool.patch
BuildRequires:	ORBit2-devel >= 1:2.14.6
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	python-devel >= 1:2.4.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	ORBit2 >= 1:2.14.6
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python language binding for the ORBit2 CORBA implementation.
It aims to take advantage of new features found in ORBit2 to make
language bindings more efficient. This includes:
- use of ORBit2 type libraries to generate stubs
- use of the ORBit_small_invoke_stub() call for operation invocation,
  which allows for short circuited invocation on local objects

%description -l pl.UTF-8
Ten pakiet zawiera wiązania Pythona do ORBit2 - implementacji CORBA.
Jego celem jest wykorzystanie wszystkich nowych możliwości OBRit2, aby
uczynić wiązania bardziej skutecznymi. Wiązania umożliwiają:
- użycie bibliotek typów ORBit2 do generowania szkieletów
- użycie wywołania ORBit_small_invoke_stub() do żądania operacji, co
  pozwala na krótkie wywołania na lokalnych obiektach.

%package devel
Summary:	Development files for the ORBit Python module
Summary(pl.UTF-8):	Pliki programistyczne dla modułu Pythona ORBit
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento para o módulo ORBit Python
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	ORBit2-devel >= 1:2.14.6
Requires:	python-devel >= 2.4.0

%description devel
This package contains development files needed to develop ORBit Python
based extensions.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne potrzebne do rozwijania
rozszerzeń bazujących na ORBit Python.

%description devel -l pt_BR.UTF-8
Este pacote contém arquivos de desenvolvimento necessários à criação
de extensões baseadas no ORBit Python.

%package examples
Summary:	Example programs using Python ORBit2 bindings
Summary(pl.UTF-8):	Przykładowe programy w Pythonie używające ORBit2
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Example programs using ORBit2 bindings.

%description examples -l pl.UTF-8
Przykładowe programy w Pythonie używające ORBit2.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/{*.la,*.py}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{py_sitedir}/ORBit.so
%{py_sitedir}/*.py[co]

%files devel
%defattr(644,root,root,755)
%{_includedir}/pyorbit-2
%{_pkgconfigdir}/pyorbit-2.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
