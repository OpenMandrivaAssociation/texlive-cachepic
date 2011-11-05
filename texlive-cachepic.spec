# revision 18835
# category Package
# catalog-ctan /macros/latex/contrib/cachepic
# catalog-date 2009-11-09 14:16:05 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-cachepic
Version:	1.0
Release:	1
Summary:	Convert document fragments into graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cachepic
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cachepic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cachepic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-cachepic.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle simplifies and automates conversion of document
fragments into external EPS or PDF files. The bundle consists
of two parts: a LaTeX package that implements a document level
interface, and a command line tool (written in lua) that
generates the external graphics.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/cachepic
%{_texmfdistdir}/scripts/cachepic/cachepic.cmd
%{_texmfdistdir}/scripts/cachepic/cachepic.tlu
%{_texmfdistdir}/tex/latex/cachepic/cachepic.sty
%{_texmfdistdir}/tex/latex/cachepic/prcachepic.def
%doc %{_texmfdistdir}/doc/latex/cachepic/README
%doc %{_texmfdistdir}/doc/latex/cachepic/cachepic.pdf
%doc %{_texmfdistdir}/doc/latex/cachepic/cachepic.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/cachepic/cachepic.tlu cachepic
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
