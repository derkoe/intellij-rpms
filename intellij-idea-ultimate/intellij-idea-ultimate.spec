%define source_name idea-IU
%define install_path /opt/jetbrains/idea-iu
%define build_number 211.7142.45

Name:          intellij-idea-ultimate
Version:       2021.1.1
Release:       1%{?dist}
Summary:       IntelliJ Java IDE - Ultimate Edition

Group:         Development
License:       Commercial
URL:           https://www.jetbrains.com/idea/
Source0:       https://download-cf.jetbrains.com/idea/ideaIU-%{version}.tar.gz

%description
The most intelligent JVM IDE

%prep
%autosetup -n %{source_name}-%{build_number}

%install
%__mkdir -p %{buildroot}%{install_path}
%__mkdir -p %{buildroot}%{_bindir}
%__cp -r %{_builddir}/%{source_name}-%{build_number}/* %{buildroot}%{install_path}
%__ln_s %{buildroot}%{install_path}/bin/idea.sh %{buildroot}%{_bindir}/idea

%files
%{install_path}/*
