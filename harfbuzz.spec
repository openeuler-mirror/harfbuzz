Name:           harfbuzz
Version:        1.8.7
Release:        2
Summary:        A text shaping engine

License:        MIT
URL:            https://harfbuzz.github.io/what-is-harfbuzz.html
Source0:        https://github.com/harfbuzz/harfbuzz/releases/tag/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++ freetype-devel cairo-devel glib2-devel graphite2-devel
BuildRequires:  gtk-doc libicu-devel
Provides:       harfbuzz-icu
Obsoletes:      harfbuzz-icu

%description
HarfBuzz is a text-shaping engine. If you give HarfBuzz a font and a string
containing a sequence of Unicode codepoints, HarfBuzz selects and positions
the corresponding glyphs from the font, applying all of the necessary layout
rules and font features. HarfBuzz then returns the string to you in the form
that is correctly arranged for the language and writing system.

%package        devel
Summary:        The development environment for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files and libraries for building a extension library for %{name}.
%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure  --with-graphite2 --enable-static
%disable_rpath

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
%delete_la

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/libharfbuzz.so.*
%{_libdir}/libharfbuzz-subset.so.*
%{_libdir}/libharfbuzz-icu.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/harfbuzz/harfbuzz-config.cmake
%{_includedir}/harfbuzz/
%{_bindir}/*
%{_libdir}/*.a

%files help
%doc  README
%{_datadir}/gtk-doc/html/harfbuzz/*

%changelog
* Mon Aug 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.8.7-2
- Package Init
