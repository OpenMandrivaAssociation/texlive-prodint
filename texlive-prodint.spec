Name:		texlive-prodint
Version:	21893
Release:	2
Summary:	A font that provides the product integral symbol
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/prodint
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prodint.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prodint.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Product integrals are to products, as integrals are to sums.
They have been around for more than a hundred years, they have
not become part of the standard toolbox, possibly because no-
one invented the right mathematical symbol for them. The
authors remedied that situation by proposing the symbol and
providing this font.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/prodint/prodint.afm
%{_texmfdistdir}/fonts/map/dvips/prodint/prodint.map
%{_texmfdistdir}/fonts/tfm/public/prodint/prodint.tfm
%{_texmfdistdir}/fonts/type1/public/prodint/prodint.pfb
%{_texmfdistdir}/tex/latex/prodint/prodint.sty
%doc %{_texmfdistdir}/doc/fonts/prodint/README
%doc %{_texmfdistdir}/doc/fonts/prodint/config.prodint
%doc %{_texmfdistdir}/doc/fonts/prodint/prodint.bma
%doc %{_texmfdistdir}/doc/fonts/prodint/prodint.mt1
%doc %{_texmfdistdir}/doc/fonts/prodint/prodint.pdf
%doc %{_texmfdistdir}/doc/fonts/prodint/prodint.pfa
%doc %{_texmfdistdir}/doc/fonts/prodint/prodint.sit.hqx
%doc %{_texmfdistdir}/doc/fonts/prodint/prodint.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
