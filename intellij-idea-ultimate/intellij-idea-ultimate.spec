%define source_name idea-IU
%define install_path /opt/jetbrains/idea-iu
%define build_number 211.7142.45
%undefine __brp_mangle_shebangs

Name:          intellij-idea-ultimate
Version:       2021.1.1
Release:       1%{?dist}
Summary:       IntelliJ Java IDE - Ultimate Edition

Group:         Development
License:       Commercial
URL:           https://www.jetbrains.com/idea/
Source0:       https://download-cf.jetbrains.com/idea/ideaIU-%{version}.tar.gz

# Require /etc/pki/java/cacerts
Requires: ca-certificates

%description
The most intelligent JVM IDE

%prep
%autosetup -n %{source_name}-%{build_number}

%install
%__mkdir -p %{buildroot}%{install_path}
%__mkdir -p %{buildroot}%{_bindir}
%__cp -r %{_builddir}/%{source_name}-%{build_number}/* %{buildroot}%{install_path}
%__ln_s %{buildroot}%{install_path}/bin/idea.sh %{buildroot}%{_bindir}/idea

# Remove empty cacerts database
rm -f %{buildroot}%{install_path}/jbr/lib/security/cacerts
# Install cacerts symlink needed by some apps which hard-code the path
pushd %{buildroot}%{install_path}/jbr/lib/security
    ln -sf /etc/pki/java/cacerts .
popd

%files
%{_bindir}/idea
%{install_path}/*
