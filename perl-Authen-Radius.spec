%define upstream_name	 Authen-Radius
%define upstream_version 0.37
%define tarname RadiusPerl 

Summary:	Radius authentication interface to Perl 5	
Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/Authen-Radius
Source0:	https://cpan.metacpan.org/authors/id/P/PO/PORTAONE/Authen-Radius-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

%description
RadiusPerl is a Perl 5 module (Radius.pm) which allows you to 
communicate with a Radius server from Perl. You can just authenticate 
usernames/passwords via Radius, or comletely imitate AAA requests 
and process server response.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="%{optflags}" 
# (sb) can't really do this - need a Radius server
#make test

%install
%makeinstall_std 

%files
%doc README
%{perl_vendorlib}/Authen
%{_mandir}/man3/*

