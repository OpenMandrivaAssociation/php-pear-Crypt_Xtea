%define		_class		Crypt
%define		_subclass	Xtea
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(PHPUnit/PHPUnit.php)

Name:		php-pear-%{upstream_name}
Version:	1.1.0
Release:	%mkrel 6
Summary:	The Tiny Encryption Algorithm (TEA) (New Variant)
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Crypt_Xtea/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A class that implements the Tiny Encryption Algorithm (TEA) (New
Variant). This class does not depend on mcrypt. Encryption is
relatively fast, decryption relatively slow. Original code from
http://vader.brad.ac.uk/tea/source.shtml#new_ansi

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


