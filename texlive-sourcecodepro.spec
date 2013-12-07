# revision 32006
# category Package
# catalog-ctan /fonts/sourcecodepro
# catalog-date 2013-10-24 20:34:16 +0200
# catalog-license ofl
# catalog-version 2.2
Name:		texlive-sourcecodepro
Version:	2.2
Release:	4
Summary:	Use SourceCodePro with TeX(-alike) systems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/sourcecodepro
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sourcecodepro.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sourcecodepro.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/sourcecodepro/a_aoc6c2.enc
%{_texmfdistdir}/fonts/enc/dvips/sourcecodepro/a_djdyjq.enc
%{_texmfdistdir}/fonts/enc/dvips/sourcecodepro/a_jvslvy.enc
%{_texmfdistdir}/fonts/enc/dvips/sourcecodepro/a_ktd5xr.enc
%{_texmfdistdir}/fonts/enc/dvips/sourcecodepro/a_mqb3sg.enc
%{_texmfdistdir}/fonts/enc/dvips/sourcecodepro/a_retzg2.enc
%{_texmfdistdir}/fonts/enc/dvips/sourcecodepro/a_xftsmg.enc
%{_texmfdistdir}/fonts/map/dvips/sourcecodepro/SourceCodePro.map
%{_texmfdistdir}/fonts/opentype/adobe/sourcecodepro/SourceCodePro-Black.otf
%{_texmfdistdir}/fonts/opentype/adobe/sourcecodepro/SourceCodePro-Bold.otf
%{_texmfdistdir}/fonts/opentype/adobe/sourcecodepro/SourceCodePro-ExtraLight.otf
%{_texmfdistdir}/fonts/opentype/adobe/sourcecodepro/SourceCodePro-Light.otf
%{_texmfdistdir}/fonts/opentype/adobe/sourcecodepro/SourceCodePro-Medium.otf
%{_texmfdistdir}/fonts/opentype/adobe/sourcecodepro/SourceCodePro-Regular.otf
%{_texmfdistdir}/fonts/opentype/adobe/sourcecodepro/SourceCodePro-Semibold.otf
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Black-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Light-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Medium-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Regular-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/type1/adobe/sourcecodepro/SourceCodePro-Black.pfb
%{_texmfdistdir}/fonts/type1/adobe/sourcecodepro/SourceCodePro-Bold.pfb
%{_texmfdistdir}/fonts/type1/adobe/sourcecodepro/SourceCodePro-ExtraLight.pfb
%{_texmfdistdir}/fonts/type1/adobe/sourcecodepro/SourceCodePro-Light.pfb
%{_texmfdistdir}/fonts/type1/adobe/sourcecodepro/SourceCodePro-Medium.pfb
%{_texmfdistdir}/fonts/type1/adobe/sourcecodepro/SourceCodePro-Regular.pfb
%{_texmfdistdir}/fonts/type1/adobe/sourcecodepro/SourceCodePro-Semibold.pfb
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Black-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Black-osf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Black-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Black-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Black-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Black-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Black-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Black-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Black-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-ExtraLight-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-ExtraLight-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-ExtraLight-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Light-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Light-osf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Light-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Light-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Light-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Light-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Medium-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Medium-osf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Medium-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Medium-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Medium-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Medium-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Regular-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Regular-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Semibold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Semibold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Semibold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Semibold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/adobe/sourcecodepro/SourceCodePro-Semibold-tosf-ts1.vf
%{_texmfdistdir}/tex/latex/sourcecodepro/LY1SourceCodePro-OsF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/LY1SourceCodePro-TLF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/LY1SourceCodePro-TOsF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/OT1SourceCodePro-OsF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/OT1SourceCodePro-TLF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/OT1SourceCodePro-TOsF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/T1SourceCodePro-OsF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/T1SourceCodePro-TLF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/T1SourceCodePro-TOsF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/TS1SourceCodePro-OsF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/TS1SourceCodePro-TLF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/TS1SourceCodePro-TOsF.fd
%{_texmfdistdir}/tex/latex/sourcecodepro/sourcecodepro-type1-autoinst.sty
%{_texmfdistdir}/tex/latex/sourcecodepro/sourcecodepro.sty
%doc %{_texmfdistdir}/doc/latex/sourcecodepro/LICENSE.txt
%doc %{_texmfdistdir}/doc/latex/sourcecodepro/README
%doc %{_texmfdistdir}/doc/latex/sourcecodepro/sourcecodepro-otf-specimen.pdf
%doc %{_texmfdistdir}/doc/latex/sourcecodepro/sourcecodepro-otf-specimen.tex
%doc %{_texmfdistdir}/doc/latex/sourcecodepro/sourcecodepro-type1-specimen.pdf
%doc %{_texmfdistdir}/doc/latex/sourcecodepro/sourcecodepro-type1-specimen.tex
%doc %{_texmfdistdir}/doc/latex/sourcecodepro/sourcecodepro.pdf
%doc %{_texmfdistdir}/doc/latex/sourcecodepro/sourcecodepro.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
