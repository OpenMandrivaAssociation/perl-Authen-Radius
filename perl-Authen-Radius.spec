%define upstream_name	 Authen-Radius
%define upstream_version 0.20
%define tarname RadiusPerl 

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:	Radius authentication interface to Perl 5	
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen/%{tarname}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch


%description
RadiusPerl is a Perl 5 module (Radius.pm) which allows you to 
communicate with a Radius server from Perl. You can just authenticate 
usernames/passwords via Radius, or comletely imitate AAA requests 
and process server response.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="%{optflags}" 
# (sb) can't really do this - need a Radius server
#make test

%install
%makeinstall_std 

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Authen


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.200.0-4mdv2012.0
+ Revision: 765068
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.200.0-3
+ Revision: 763484
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.200.0-2
+ Revision: 667032
- mass rebuild

* Sat Nov 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 597209
- update to 0.20

* Fri Jan 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.1
+ Revision: 491729
- update to 0.17

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.1
+ Revision: 460719
- update to 0.15

* Thu Aug 20 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 418413
- update to 0.14

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.13-3mdv2009.1
+ Revision: 351673
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.13-2mdv2009.0
+ Revision: 223566
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 0.13-1mdv2008.1
+ Revision: 166033
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Apr 29 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.13-1mdv2008.0
+ Revision: 19249
-New version


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.12-3mdv2007.0
+ Revision: 73308
- import perl-Authen-Radius-0.12-3mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-3mdk
- Fix SPEC Using perl Policies
	- Source URL
- use mkrel

* Mon Feb 06 2006 Stew Benedict <sbenedict@mandriva.com> 0.12-2mdk
- annual rebuild

* Fri Jan 07 2005 Stew Benedict <sbenedict@mandrakesoft.com> 0.12-1mdk
- 0.12

* Mon Dec 01 2003 Stew Benedict <sbenedict@mandrakesoft.com> 0.09-1mdk
- first Mandrake release, optional feature for nocatauth

