%global tl_name prodint
%global tl_revision 21893

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A font that provides the product integral symbol
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/prodint
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prodint.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prodint.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Product integrals are to products, as integrals are to sums. They have
been around for more than a hundred years, they have not become part of
the standard mathematician's toolbox, possibly because no-one invented
the right mathematical symbol for them. The authors have remedied that
situation by proposing the symbol and providing this font.

