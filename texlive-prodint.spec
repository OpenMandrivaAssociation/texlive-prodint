# revision 21893
# category Package
# catalog-ctan /fonts/prodint
# catalog-date 2011-03-30 12:07:52 +0200
# catalog-license ofl
# catalog-version undef
Name:		texlive-prodint
Version:	20180303
Release:	1
Summary:	A font that provides the product integral symbol
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/prodint
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prodint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prodint.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110330-2
+ Revision: 755070
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110330-1
+ Revision: 719304
- texlive-prodint
- texlive-prodint
- texlive-prodint
- texlive-prodint

