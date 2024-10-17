%define		_class		Crypt
%define		_subclass	Xtea
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.0
Release:	11
Summary:	The Tiny Encryption Algorithm (TEA) (New Variant)
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Crypt_Xtea/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
A class that implements the Tiny Encryption Algorithm (TEA) (New
Variant). This class does not depend on mcrypt. Encryption is
relatively fast, decryption relatively slow. Original code from
http://vader.brad.ac.uk/tea/source.shtml#new_ansi

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-7mdv2012.0
+ Revision: 741837
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-6
+ Revision: 679277
- mass rebuild
- the mass rebuild of 2010.1 packages

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-4mdv2010.1
+ Revision: 478357
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-3mdv2010.0
+ Revision: 440969
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2009.1
+ Revision: 321946
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1mdv2009.0
+ Revision: 278911
- update to new version 1.1.0

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-8mdv2009.0
+ Revision: 236818
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2007.0
+ Revision: 81477
- Import php-pear-Crypt_Xtea

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdk
- initial Mandriva package (PLD import)

