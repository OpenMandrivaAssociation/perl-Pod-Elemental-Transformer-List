%define upstream_name    Pod-Elemental-Transformer-List
%define upstream_version 0.102000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Transform :list regions into =over/=back to save typing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-Elemental-Transformer-List-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Pod::Elemental)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
Transform :list regions into =over/=back to save typing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.101.620-2mdv2011.0
+ Revision: 658546
- rebuild for updated spec-helper

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.620-1mdv2011.0
+ Revision: 553136
- update to 0.101620

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.93.580-1mdv2010.1
+ Revision: 488856
- import perl-Pod-Elemental-Transformer-List


* Sun Jan 10 2010 cpan2dist 0.093580-1mdv
- initial mdv release, generated with cpan2dist

