%define		_status		stable
%define		_pearname	XML_NITF
Summary:	%{_pearname} - parse NITF documents
Summary(pl.UTF-8):	%{_pearname} - analiza dokumentów NITF
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1c849b5777e5ab7081c3959eaa831ee3
URL:		http://pear.php.net/package/XML_NITF/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.0
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

%description -l pl.UTF-8
Ten pakiet udostępnia analizator dokumentów XML NITF. Analizator
został zaprojektowany dla NITF w wersji 3.1, ale powinien być
kompatybilny w przód, kiedy zostaną wydane nowe wersje NITF DTD.
Dostępne są różne metody do dostępu do głównych elementów dokumentu,
takich jak hedline, byline i lede. Ta klasa była oryginalnie testowana
danymi XML z Associated Press (AP).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# developer project files
%{__rm} .%{php_pear_dir}/data/XML_NITF/.buildpath
%{__rm} .%{php_pear_dir}/data/XML_NITF/.project
%{__rm} .%{php_pear_dir}/data/XML_NITF/.settings/org.eclipse.php.core.prefs

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
%{php_pear_dir}/XML/NITF.php
