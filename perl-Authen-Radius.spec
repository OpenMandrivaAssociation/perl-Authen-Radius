%define upstream_name	 Authen-Radius
%define upstream_version 0.20
%define tarname RadiusPerl 

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Radius authentication interface to Perl 5	
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen/%{tarname}-%{upstream_version}.tar.gz

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
RadiusPerl is a Perl 5 module (Radius.pm) which allows you to 
communicate with a Radius server from Perl. You can just authenticate 
usernames/passwords via Radius, or comletely imitate AAA requests 
and process server response.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="$RPM_OPT_FLAGS" 
# (sb) can't really do this - need a Radius server
#make test

%install
rm -rf %{buildroot} 
%makeinstall_std 

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Authen
