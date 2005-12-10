%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	NITF
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - parse NITF documents
Summary(pl):	%{_pearname} - analiza dokumentów NITF
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	462fa8879bb021a0bafc6b9d44fbb50d
URL:		http://pear.php.net/package/XML_NITF/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a NITF XML parser. The parser was designed with
NITF version 3.1, but should be forward-compatible when new versions
of the NITF DTD are produced. Various methods for accessing the major
elements of the document, such as the hedline(s), byline, and lede are
provided. This class was originally tested against the Associated
Press's (AP) XML data feed.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet udostêpnia analizator dokumentów XML NITF. Analizator
zosta³ zaprojektowany dla NITF w wersji 3.1, ale powinien byæ
kompatybilny w przód, kiedy zostan± wydane nowe wersje NITF DTD.
Dostêpne s± ró¿ne metody do dostêpu do g³ównych elementów dokumentu,
takich jak hedline, byline i lede. Ta klasa by³a oryginalnie testowana
danymi XML z Associated Press (AP).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
