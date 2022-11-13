Name:		texlive-sourcecodepro
Version:	54512
Release:	1
Summary:	Use SourceCodePro with TeX(-alike) systems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/sourcecodepro
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sourcecodepro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sourcecodepro.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The font is an open-source Monospaced development from Adobe.
The package provides fonts (in both Adobe Type 1 and OpenType
formats) and macros supporting their use in LaTeX (Type 1) and
XeLaTeX/LuaLaTeX (OTF).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/sourcecodepro
%{_texmfdistdir}/fonts/map/dvips/sourcecodepro
%{_texmfdistdir}/fonts/opentype/adobe/sourcecodepro
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro
%{_texmfdistdir}/fonts/type1/adobe/sourcecodepro
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro
%{_texmfdistdir}/tex/latex/sourcecodepro
%doc %{_texmfdistdir}/doc/latex/sourcecodepro

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
