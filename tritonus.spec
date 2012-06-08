# Copyright (c) 2006-2008 oc2pus
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

# norootforbuild

%ifarch x86_64
%define _jvm_lib_ext_dir	%{_jvmdir}/jre/lib/amd64
%else
%define _jvm_lib_ext_dir	%{_jvmdir}/jre/lib/i386
%endif
%define _cvs_version	20110107

Name:			tritonus
Summary:		Tritonus - A implementation of the Java Sound API
URL:			http://www.tritonus.org/
Group:			Development/Java
Version:		0.3.7
Release:		%mkrel 0.0.%{_cvs_version}.1
License:		LGPL
# cvs -d:pserver:anonymous@tritonus.cvs.sourceforge.net:/cvsroot/tritonus login
# cvs -z3 -d:pserver:anonymous@tritonus.cvs.sourceforge.net:/cvsroot/tritonus co tritonus
# cp -far tritonus tritonus-0.3.7
# find tritonus-0.3.7 -name CVS -type d -exec rm -fr {} \; 2> /dev/null
# tar Jcf tritonus-0.3.7.tar.xz tritonus-0.3.7
Source0:		%{name}-%{version}.tar.xz
Source1:		%{name}-Mp3Encoder.java
Patch:			%{name}-configure.in.diff
Patch1:			%{name}-src-lib-fluidsynth.Makefile.in.diff
Patch2:			%{name}-src-lib-alsa-Makefile.in.diff
Patch3:			%{name}-src-lib-alsa-constants_check.h.diff
Patch4:			tritonus-removed-code.diff
Patch5:			%{name}-build-common.diff
Patch6:			%{name}-build.diff
BuildRequires:	ant
BuildRequires:	java-rpmbuild
BuildRequires:	libalsa-devel >= 0.9
BuildRequires:	libcdda-devel
BuildRequires:	ncurses-devel
#BuildRequires:	dos2unix
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	esound-devel
BuildRequires:	java-rpmbuild >= 1.5
BuildRequires:	jlayer
BuildRequires:	jorbis
BuildRequires:	jpackage-utils >= 1.5
#BuildRequires:	lame
BuildRequires:	lash-devel
BuildRequires:	libfluidsynth-devel
BuildRequires:	libjack-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	unzip
BuildRequires:	update-alternatives
BuildRequires:	xml-commons-apis
BuildRequires:  libtool
Requires:		jakarta-commons-logging
Requires:		java >= 1.5
Requires:		jpackage-utils >= 1.5
Requires:		jlayer
Requires:		jorbis
Requires:		alsa >= 0.9
# requires for virtual package:
Requires:		tritonus-alsa
Requires:		tritonus-aos
Requires:		tritonus-cdda
Requires:		tritonus-core
Requires:		tritonus-dsp
Requires:		tritonus-esd
Requires:		tritonus-fluidsynth
#Requires:		tritonus-javadoc
Requires:		tritonus-javasequencer
Requires:		tritonus-jorbis
Requires:		tritonus-gsm
Requires:		tritonus-mp3
%if 0
Requires:		tritonus-mp3enc
%endif
Requires:		tritonus-pvorbis
Requires:		tritonus-shared
Requires:		tritonus-src
Requires:		tritonus-vorbis
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Virtual package to install all tritonus-plugins.

Tritonus is an implementation of the Java Sound API.

Currently, GNU/Linux i386 and Linux/PowerPC is supported. Some
separately downloadable plugins also run on other JavaSound
platforms. Support for other platforms is planned for the future.

Tritonus is distributed under the terms of the GNU Library General
Public License.

%if 0
%package javadoc
Summary:	Javadoc for tritonus
Group:		Development/Java

%description javadoc
Javadoc for tritonus.
%endif

%package shared
Summary:	Shared classes required by all other Tritonus plug-ins
Group:		Development/Java

%description shared
Shared classes required by all other Tritonus plug-ins.

%package jorbis
Summary:	A plug-in for Java that enables decoding of Ogg Vorbis bitstreams
Group:		Development/Java
Requires:	jorbis
Requires:	%{name}-shared

%description jorbis
A plug-in for Java that enables decoding of Ogg Vorbis bitstreams.
It is based on the pure-java decoder implementation of JCraft. The
decoder runs in real-time even on old machines, as long as your
Java runtime has a JIT-Compiler (most contemporary have).

%package vorbis
Summary:	A plug-in for Java that enables encoding to Ogg Vorbis bitstreams
Group:		Development/Java
#Requires:	libvorbis
Requires:	%{name}-shared

%description vorbis
A plug-in for Java that enables encoding to Ogg Vorbis bitstreams.
It is based on the native vorbis libraries.

%package pvorbis
Summary:	A plug-in for Java that enables encoding to Ogg Vorbis bitstreams
Group:		Development/Java
Requires:	jorbis
Requires:	%{name}-shared

%description pvorbis
A plug-in for Java that enables encoding to Ogg Vorbis bitstreams.

%package cdda
Summary:	A plug-in for Java that enables you to digitally read audio CD's
Group:		Development/Java
Requires:	cdparanoia >= IIIalpha9.8
Requires:	%{name}-shared

%description cdda
A plug-in for Java that enables you to digitally read audio CD's.

The download package contains the library for Linux/i386, tritonus_cdda.jar,
source code, and detailed instructions.

A demo program was presented at the JavaOne 2002 conference:
Ripping and Encoding to MP3 with the Java Sound API.
See: http://www.jsresources.org/apps/ripper/

%package mp3
Summary:	MP3 Decoder
Group:		Development/Java
Requires:	%{name}-shared
Requires:	jlayer

%description mp3
MP3-Devoder.

%if 0
%package mp3enc
Summary:	A plug-in for Java that enables mp3 encoding with Java Sound
Group:		Development/Java
Requires:	lame
Requires:	%{name}-shared
Requires:	%{name}-mp3

%description mp3enc
A plug-in for Java that enables mp3 encoding with Java Sound.

The download package contains the native libraries for Linux/i386,
detailed instructions, and a test program.
%endif

%package gsm
Summary:	GSM codec
Group:		Development/Java
Requires:	%{name}-shared

%description gsm
For examples of using the GSM codec, refer to the Java Sound Resources examples
GSMEncoder, AudioDecoder  and DecodingAudioPlayer:
http://www.jsresources.org/
http://www.jsresources.org/examples/GSMEncoder.html
http://www.jsresources.org/examples/AudioDecoder.html
http://www.jsresources.org/examples/DecodingAudioPlayer.html

%package javasequencer
Summary:	A Java-Sequencer
Group:		Development/Java
Requires:	%{name}-shared

%description javasequencer
Note that for this sequencer to provide stable timing, three
conditions have to be met:

1. System.currentTimeMillis() has to do what its name says:
provide the system time in milliseconds. Some lecacy operating
systems (Windows & co.) provide a timer resolution of only 10,
30 or 60 ms. For information on what you can expect on your
operating system, see the measurements of YIP Chi Lap [Beta]

2. A synthesizer or MIDI port implementation that responds
immediately.
Testing with the synthesizer of the Sun implementation resulted
in horrible timing. Timing with the hardware synthesizer of a
SB Life!, accessed via ALSA, was very good. Working with
WireProvider should be ok, too (assuming you manage to meet
the first point)

3. Small scheduling latencies. On the GNU/Linux system I tested,
even heavy file system traffic didn't lead to noticeable effects
on the timing. However, usage of the X server almost always led
to delays. This is due to the fact that the X server normally
runs with very high scheduling priority, stealing other processes
CPU time. Moving a window killed the timing. Even a running 'top'
was noticeable.

For testing with this sequencer, I recommend to use a recent
version of MidiPlayer from the Java Sound Examples.

%package esd
Summary:	An implementation of javax.sound.sampled.Mixer based on libesd
Group:		Development/Java
Requires:	esound
Requires:	%{name}-shared

%description esd
An implementation of javax.sound.sampled.Mixer based on libesd.

It provides (most of) the capabilities Esound provides to Java
Sound. Especially, you can use this mixer to get full-duplex
support for Java Sound on Linux.

%package alsa
Summary:	Implementations of javax.sound.sampled.Mixer and javax.sound.midi.MidiDevice based on ALSA
Group:		Development/Java
Requires:	alsa >= 0.9
Requires:	%{name}-shared

%description alsa
Implementations of javax.sound.sampled.Mixer and javax.sound.midi.MidiDevice
based on ALSA.

It provides (most of) the capabilities of ALSA pcm and seq to Java
Sound.
Especially, you can use this mixer to get full-duplex support and
MIDI in/out plus a very stable sequencer for Java Sound on Linux.

%package dsp
Summary:	A collection of classes for digital signal processing (DSP)
Group:		Development/Java
Requires:	%{name}-shared

%description dsp
A collection of classes for digital signal processing (DSP).

For an example of how to use it, see AmplitudeConverter in the examples
section of the Java Sound Resources.

%package aos
Summary:	An add-on to the Java Sound API
Group:		Development/Java
Requires:	%{name}-shared

%description aos
An add-on to the Java Sound API.

The AudioOutputStream architecture allow writing of audio data to
audio files. Supported types are .wav, .aiff and .au. It is an
alternative to using AudioSystem.write(). The advantage over
AudioSystem.write() is that with the AudioOutputStream architecture,
you can code your own main loop writing to the audio file.
The AudioOutputStream architecture implements a 'push' approach for
audio data, while AudioSystem.write() works with a "pull" approach.
In many situations, a 'push' approach is more flexible.

For an example of using the AudioOutputStream architecture, see the
examples on Java Sound Resources. There is an examples
OscillatorFileAOS using the AudioOutputStream architecture.

%package misc
Summary:	Plug-in with several service provider of Tritonus
Group:		Development/Java
Requires:	%{name}-shared

%description misc
Plug-in with several service provider of Tritonus.

It contains the PCM2PCM converter, A-law and U-law converters,
sample rate converter, ADPCM converters, audio file readers
and writers and MIDI file readers and writers.

For an example of how to use the sample rate converter, see
SampleRateConverter.
http://www.jsresources.org/examples/SampleRateConverter.html

%package fluidsynth
Summary:	Plug-in for fluidsynth
Group:		Development/Java
Requires:	%{name}-shared
Requires:	fluidsynth
Requires:	ncurses
Requires:	jack

%description fluidsynth
Plug-in for fluidsynth.

%package src
Summary:	Sample rate converter
Group:		Development/Java
Requires:	%{name}-shared

%description src
Sample rate converter.

%package core
Summary:	Contains public classes and SPI instantiation support
Group:		Development/Java

%description core
Contains public classes and SPI instantiation support.

%prep
%setup -q
%patch
%patch1
%patch2
%patch3
%patch4 -p1
%patch5
%patch6

autoreconf -fi

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export CPPFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure

%ant -f build-dtd.xml
export CLASSPATH=`build-classpath jl jorbis`
%ant

%__sed -i -e 's|-Wall -Werror||g' \
	src/lib/cdparanoia/Makefile
%__sed -i -e 's|-Wall -Werror||g' \
	src/lib/esd/Makefile
%__sed -i -e 's|-Wall -Werror||g' \
	src/lib/fluidsynth/Makefile
%__sed -i -e 's|-Wall -Werror||g' \
	src/lib/vorbis/Makefile
%__sed -i -e 's|libtool|libtool --tag=CXX |g' \
	src/lib/fluidsynth/Makefile

%__make \
	JAVADIR=%{_jvmdir}/java

%install
# jars
%__install -dm 755 %{buildroot}%{_javadir}
%__install -pm 644 dist/*.jar %{buildroot}%{_javadir}
pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

# native libs
%__install -dm 755 %{buildroot}%{_jvmdir}/jre/lib/ext
pushd dist
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

%__make install \
	JAVAEXTPATH=%{buildroot}%{_jvmdir}/jre/lib/ext \
	JAVADIR=%{_jvmdir}/java \
	JAVAEXTLIBPATH=%{buildroot}%{_jvm_lib_ext_dir} \
	DESTDIR=%{buildroot}

# link the tritonus-jar files from %{javadir}/%{name} to %{_jvmdir}/jre/lib/ext
for i in core gsm mp3 remaining share; do
	%add_jvm_extension %{buildroot}%{_javadir}/%{name}_$i.jar
done

# directory for native-libraries
#install -dm 755 %{buildroot}%{_libdir}
#install -m 744 libtritonuscommon.so* %{buildroot}%{_libdir}

# javadoc
%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
#cp -pr doc/apidoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
#ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if 0
# install Mp3Encoder.java
%__install -dm 755 %{buildroot}%{_defaultdocdir}/%{name}-mp3enc
%__install -m 644 %{SOURCE1} \
	%{buildroot}%{_defaultdocdir}/%{name}-mp3enc
%__install -m 644 LGPL \
	%{buildroot}%{_defaultdocdir}/%{name}-mp3enc
%endif

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && %__rm -rf %{buildroot}

%files
%defattr(-,root,root)

%files alsa
%defattr(-,root,root)
%doc LGPL
%doc doc/ALSA*  doc/Alsa*
%doc doc/bindists/alsa/readme.txt
%{_javadir}/%{name}_alsa*.jar
%{_jvm_lib_ext_dir}/lib%{name}alsa.so*

%files aos
%defattr(-,root,root)
%doc LGPL
%doc doc/AudioOutput*
%{_javadir}/%{name}_aos*.jar

%files cdda
%defattr(-,root,root)
%doc LGPL
%doc doc/cdda.txt
%doc doc/bindists/cdda/readme.txt
%{_javadir}/%{name}_cdda*.jar
%{_jvm_lib_ext_dir}/lib%{name}cdparanoia.so*

%files core
%defattr(-,root,root)
%doc LGPL NEWS README
%doc doc/%{name}faq.sgml
%{_javadir}/%{name}_core*.jar
%{_jvmdir}/jre/lib/ext/%{name}_core.jar
#%{_libdir}/lib%{name}common.so*

%files dsp
%defattr(-,root,root)
%doc LGPL
%{_javadir}/%{name}_dsp*.jar

%files esd
%defattr(-,root,root)
%doc LGPL
%doc doc/bindists/esd/readme.txt
%{_javadir}/%{name}_esd*.jar
%{_jvm_lib_ext_dir}/lib%{name}esd.so*

%files fluidsynth
%defattr(-,root,root)
%doc LGPL
%doc doc/fluidsynth*
%{_javadir}/%{name}_fluidsynth*.jar
%{_jvm_lib_ext_dir}/lib%{name}fluid.so*

%files gsm
%defattr(-,root,root)
%doc LGPL
%{_javadir}/%{name}_gsm*.jar
%{_jvmdir}/jre/lib/ext/%{name}_gsm*.jar

%if 0
%files javadoc
%defattr(-,root,root)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}
%endif

%files javasequencer
%defattr(-,root,root)
%doc LGPL
%{_javadir}/%{name}_javasequencer*.jar

%files jorbis
%defattr(-,root,root)
%doc LGPL
%{_javadir}/%{name}_jorbis*.jar

%files misc
%defattr(-,root,root)
%doc LGPL
%{_javadir}/%{name}_remaining*.jar
%{_jvmdir}/jre/lib/ext/tritonus_remaining.jar

%files mp3
%defattr(-,root,root)
%doc LGPL
%doc README_mp3
%{_javadir}/%{name}_mp3*.jar
%{_jvmdir}/jre/lib/ext/%{name}_mp3.jar

%if 0
%files mp3enc
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}-mp3enc/*
%{_jvm_lib_ext_dir}/liblame%{name}.so*
%endif

%files pvorbis
%defattr(-,root,root)
%doc LGPL
%{_javadir}/%{name}_pvorbis*.jar

%files shared
%defattr(-,root,root)
%doc LGPL
%{_javadir}/%{name}_share*.jar
%{_jvmdir}/jre/lib/ext/%{name}_share.jar

%files src
%defattr(-,root,root)
%doc LGPL
%{_javadir}/%{name}_src*.jar

%files vorbis
%defattr(-,root,root)
%doc LGPL
%doc doc/bindists/vorbis/readme.txt
%{_javadir}/%{name}_vorbis*.jar
%{_jvm_lib_ext_dir}/lib%{name}vorbis.so*
