# Generated by rust2rpm 10
# * Tests require networking
%bcond_with check
%global debug_package %{nil}

%global crate restson

Name:           rust-%{crate}
Version:        0.5.4
Release:        3%{?dist}
Summary:        Easy-to-use REST client with automatic serialization and deserialization

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/restson
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Easy-to-use REST client with automatic serialization and deserialization.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 11:24:00 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Sun May 05 16:52:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-1
- Initial package
