%define module	Authen-Radius
%define name	perl-%{module}
%define version 0.13
%define release %mkrel 1
%define tarname RadiusPerl 

Summary:	Radius authentication interface to Perl 5	
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
URL:		http://search.cpan.org/dist/%{module}
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen/%{tarname}-%{version}.tar.bz2
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

%description
RadiusPerl is a Perl 5 module (Radius.pm) which allows you to 
communicate with a Radius server from Perl. You can just authenticate 
usernames/passwords via Radius, or comletely imitate AAA requests 
and process server response.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="$RPM_OPT_FLAGS" 
# (sb) can't really do this - need a Radius server
#make test

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall_std 

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Authen



