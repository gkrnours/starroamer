Universe
========

Here is documented part of the file _universeDataDx.db_. For the basic,
it's an sqlite3 database with 12 tables.

Summary
-------

 * mapCelestialStatistics
 * mapConstellationJumps
 * mapConstellations
 * mapDenormalize
 * mapJumps
 * mapLandarks
 * mapLocationScenes
 * mapLocationWorholeClasses
 * mapRegionJumps
 * mapRegions
 * mapSolarSystemJumps
 * mapSolarSystems

mapSolarSystems
---------------

### Structure

 * regionID | int | indexed
 * constellationID | int | indexed
 * solarSystemID | int |
 * solarSystemName | str(100) |
 * x | real |
 * y | real |
 * z | real |
 * xMin | real |
 * xMax | real |
 * yMin | real |
 * yMax | real |
 * zMin | real |
 * zMax | real |
 * luminosity | real |
 * border | bit |
 * fringe | bit |
 * corridor | bit |
 * hub | bit |
 * international | bit |
 * regional | bit |
 * constellation | bit |
 * security | real | indexed
 * factionID | int |
 * radius | real |
 * sunTypeId | int |
 * securityClass | str(2) |

### Interpretation

First, only three field are indexed. Finding every system from a region
or a constellation is ok. Same for finding everything above a specific
security level. Getting the three darkest corner of the universe ? Maybe
not a bright idea.

A good halve of the field are pretty self-explanatory. System ID and
name under solarSystemID and solarSystemName. RegionID and
constellationID give you where the system is in the universe hierarchy
while x, y, z give you an absolute position. Nice for planning jump.  
Then you get a bounding box, in case you want to plan really tight jump
and the system luminosity in case you suffer of photodermatitis. At the
end is the security level for more common form of allergy like laser
beam or good 'ol projectile. FactionID tell you who delve in the system,
radius is an easier way than messing with xMax and cie, sunTypeID is
purely cosmetic just like securityClass which is a 2 letter code for the
security level.

The other halve, from border to constellation, give some other kind of
information on the system.  
The border bit seems to indicate system in border of a constellation.
There are 1997 such systems.
Fringe system seems to be system attached to their own region by only
one stargate, such as _Sooma_. They might be have stagate pointing to
other region such as _Akkio_. System such as _G-QTSD_, _LXQ2-T_,
_Hogimo_, _Kaaputenen_ or _venilen_ are harder to
categorize as they are fringe but have multiple connexion to their own
region.

8035 systems.
1997 are in border
782 are in fringe
1920 corridor

30001641|50-TJY > corridor in jove empire; many more
30044971|Mesokel > corridor with only one connexion
30003383|Todrir > corridor while should be fringe ?



