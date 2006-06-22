%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_Renderer_XUL
%define		_status		beta
%define		_pearname	Structures_DataGrid_Renderer_XUL

Summary:	%{_pearname} - Renderer driver that generates the XML string for a XUL listbox
Summary(pl):	%{_pearname} - sterownik renderera generuj±cy ci±g znaków XML dla listbox XUL-a
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	76cd4559e6e7627f2d3205691879906a
URL:		http://pear.php.net/package/Structures_DataGrid_Renderer_XUL/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.-0.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
Requires:	php-pear-XML_Util >= 1.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Renderer driver for Structures_DataGrid that generates the
XML string for a XUL listbox.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza sterownik renderera dla Structures_DataGrid
generuj±cy ci±g znaków XML dla listbox XUL-a.

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
%{php_pear_dir}/Structures/DataGrid/Renderer/XUL.php
