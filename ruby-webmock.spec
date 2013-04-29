#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	webmock
Summary:	Library for stubbing HTTP requests in Ruby
Name:		ruby-%{pkgname}
Version:	1.11.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	d8a5e5893994b5b3ed94c4088d5cafb2
URL:		http://github.com/bblimke/webmock
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-curb >= 0.8.0
BuildRequires:	ruby-em-http-request >= 1.0.2
BuildRequires:	ruby-excon >= 0.11.0
BuildRequires:	ruby-httpclient >= 2.2.4
BuildRequires:	ruby-minitest >= 2.2.2
BuildRequires:	ruby-patron >= 0.4.18
BuildRequires:	ruby-rspec >= 2.10
BuildRequires:	ruby-typhoeus >= 0.5.0
%endif
Requires:	ruby-addressable >= 2.2.7
Requires:	ruby-crack >= 0.3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebMock allows stubbing HTTP requests and setting expectations on HTTP
requests.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
