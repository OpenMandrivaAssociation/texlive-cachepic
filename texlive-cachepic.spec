%global tl_name cachepic
%global tl_revision 78415
%global tl_bin_links cachepic:%{_texmfdistdir}/scripts/cachepic/cachepic.tlu

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Convert document fragments into graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cachepic
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cachepic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cachepic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cachepic.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The bundle simplifies and automates conversion of document fragments
into external EPS or PDF files. The bundle consists of two parts: a
LaTeX package that implements a document level interface, and a command
line tool (written in Lua) that generates the external graphics.

