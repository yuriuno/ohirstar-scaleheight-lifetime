J/A+A/628/A90    OH maser emission in THOR survey            (Beuther+, 2019)
================================================================================
OH maser emission in the THOR survey of the northern Milky Way.
    Beuther H., Walsh A., Wang Y., Rugel M., Soler J., Linz H., Kloessen R.S.,
    Anderson L.D., Glover J.SUrquhardt.S.C.O., Billington S.J., Kainulainen J.,
    Menten K.M., Roy N., Longmore S.N., Bigiel F.
    <Astron. Astrophys. 628, A90 (2019)>
    =2019A&A...628A..90B        (SIMBAD/NED BibCode)
================================================================================
ADC_Keywords: Galactic plane ; Radio sources ; Masers
Keywords: stars: formation - ISM: clouds - ISM: kinematics and dynamics -
          stars evolution - catalogs - masers

Abstract:
    OH masers trace diverse physical processes, from the expanding
    envelopes around evolved stars to star-forming regions or supernovae
    remnants. Providing a survey of the ground-state OH maser transitions
    in the northern hemisphere inner Milky Way facilitates the study of a
    broad range of scientific topics.

    We want to identify the ground-state OH masers at 18 cm wavelength in
    the area covered by "The HI/OH/Recombination line survey of the
    Milky Way (THOR)". We will present a catalogue of all OH maser
    features and their possible associated environments.

    The THOR survey covers longitude and latitude ranges of
    14.3{deg}<l<66.8{deg} and b<+/-1.25{deg}. All OH ground state lines
    ^2^{PI}_3/2_(J=3/2) at 1612 (F=1-2), 1665 (F=1-1), 1667 (F=2-2) and
    1720MHz (F=2-1) have been observed, employing the Very Large Array
    (VLA) in its C configuration. The spatial resolution of the data
    varies between 12.5" and 19", the spectral resolution is 1.5km/s, and
    the rms sensitivity of the data is 10mJy/beam per channel.

    We identify 1585 individual maser spots (corresponding to single
    spectral features) distributed over 807 maser sites (regions of size
    ~10^3^-10^4^AU). Based on different criteria from spectral profiles to
    literature comparison, we try to associate the maser sites with
    astrophysical source types. Approximately 51% of the sites exhibit the
    double-horned 1612MHz spectra typically emitted from the expanding
    shells of evolved stars. The separations of the two main velocity
    features of the expanding shells typically vary between 22 and 38km/s.
    In addition to this, at least 20% of the maser sites are associated
    with star-forming regions. While the largest fraction of 1720MHz maser
    spots (21 out of 53) is associated with supernova remnants, a
    significant fraction of the 1720MHz maser spots (17) are also
    associated with star-forming regions. We present comparisons to the
    thermal ^13^CO(1-0) emission as well as to other surveys of class II
    CH_3_OH and H_2_O maser emission. The catalogue attempts to present
    associations to astrophysical sources where available, and the full
    catalogue is available in electronic form.

    This OH maser catalogue presents a unique resource of stellar and
    interstellar masers in the northern hemisphere. It provides the basis
    for a diverse range of follow-up studies from envelopes around evolved
    stars to star-forming regions and Supernova remnants.

Description:
    Based on the HI/OH/Recombination line survey of the Milky Way (THOR),
    we present an OH maser catalogue in the longitude/latitude ranges
    14.3<l<66.8 and b<+/-1.25 degrees. All ground state OH lines at
    1612, 1665, 1667 and 1720MHz are covered. In total, we identify 1585
    individual maser spots distributed over 807 maser sites. Where
    possible, associations with astrophysical source types are conveyed
    (evolved stars, starforming regions, supernovae remnants).

File Summary:
--------------------------------------------------------------------------------
 FileName      Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe            80        .   This file
table1.dat       112     1585   THOR maser spot catalogue
--------------------------------------------------------------------------------

See also:
   J/A+A/619/A124 : THOR survey in northern Galactic plane (Wang+, 2018)

Byte-by-byte Description of file: table1.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1- 19  A19   ---     Name      Name, GLL.LLL+B.bbb-NNNA, including the maser
                                   frequency and spot label A.B
  21- 22  I2    h       RAh       Right ascension (J2000.0)
  24- 25  I2    min     RAm       Right ascension (J2000.0)
  27- 32  F6.3  s       RAs       Right ascension (J2000.0)
      34  A1    ---     DE-       Declination sign (J2000)
  35- 36  I2    deg     DEd       Declination (J2000)
  38- 39  I2    arcmin  DEm       Declination (J2000)
  41- 45  F5.2  arcsec  DEs       Declination (J2000)
  47- 53  F7.3  Jy      Speak     Peak flux density
  55- 57  I3    mJy     rms       rms
  59- 65  F7.3  Jy.km/s Sint      Integrated flux density
  67- 71  F5.1  km/s    vpeak     Peak velocity
  73- 78  F6.2  km/s    vmin      Minimum velocity of maser spot
  80- 85  F6.2  km/s    vmax      Maximum velocity of maser spot
  87- 89  F3.1  arcsec  Deltax    Positional uncertainty along X
  91- 93  F3.1  arcsec  Deltay    Positional uncertainty along Y
  95-112  A18   ----    Assoc     Associations (1)
--------------------------------------------------------------------------------
Note (1): Associations codes:
    ES   = evolved star
    D    = double peaked
    D?   = potentially double peaked with 2nd component either two weak to be
            firmly identified or outside the imaged velocity range
    BS, RS or wkS = in the GLIMPSE images a bright, red or weak star is seen
                     co-spatial with the maser site
    SF   = star formation
    SNR  = supernova remnant
    PN   = planetary nebula
    Star = star
    nPL  = near a pulsar
    Sim  = according to Simbad database
    rc   = cm continuum emission from Wang et al. (2018. Cat. J/A+A/619/A124)
   Previous literature entries are referenced as:
    Bel13 = Beltran et al. (2013, Cat. J/A+A/552/A123)
    Blo94 = Bloemmaert et al. (1994A&A...287..479B)
    Cas95 = Caswell et al. (1995MNRAS.272...96C)
    Cod10 = Codella et al. (2010A&A...510A..86C)
    Dea07 = Deacon et al. (2007, Cat. J/ApJ/658/1096)
    Deg04 = Deguchi et al. (2004, Cat. J/PASJ/56/765)
    DiF08 = Di Francesco et al. (2008, Cat. J/ApJS/175/277)
    Fel02 = Felli et al. (2002A&A...392..971F)
    He05  = He et al. (2005, Cat. J/A+A/434/201)
    Hil05 = Hill et al. (2005, Cat. J/MNRAS/363/405)
    Ima13 = Imai et al. (2013ApJ...773..182I)
    Kwo97 = Kwok et al. (1997, Cat. J/ApJS/112/557)
    Kur94 = Kurtz et al. (1994, Cat. J/ApJS/91/659)
    Lou93 = Loup et al. (1993, Cat. J/A+AS/99/291)
    Mot03 = Motte et al. (2003ApJ...582..277M)
    MMB   = Methanol Multibeam Survey Caswell et al. (2010MNRAS.404.1029C,
             Cat. VIII/96), Green et al. (2010MNRAS.409..913G, Cat. VIII/96),
             Breen et al. (2015MNRAS.450.4109B)
    Per09 = Peretto & Fuller (2009, Cat. J/A+A/505/405)
    Pes05 = Petsalozzi et al. 2005, Cat. J/A+A/432/737)
    Ros10 = Rosolowsky et al. (2010, Cat. J/ApJS/188/123)
    Sev01 = Sevenster et al. (2001, Cat. J/A+A/366/481)
    Tho06 = Thompson et al. (2006, Cat. J/A+A/453/1003)
    Urq09 = Urquhart et al. (2009, Cat. J/A+A/501/539)
    Wal98 = Walsh et al. (1998, Cat. J/MNRAS/301/640)
    Win75 = Winnberg et al. (1975A&A....38..145W)
--------------------------------------------------------------------------------

Acknowledgements:
    Henrik Beuther, beuther(at)mpia.de

================================================================================
(End)                                        Patricia Vannier [CDS]  26-Jul-2019
