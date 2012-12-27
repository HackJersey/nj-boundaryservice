from datetime import date

from boundaryservice import utils

SHAPEFILES = {
    # This key should be the plural name of the boundaries in this set
    'New Jersey Municipalities': {
        # Path to a shapefile, relative to /data/shapefiles
        'file': 'nj_boundaries/nj_munis.shp',
        # Generic singular name for an boundary of from this set
        'singular': 'Municipality',
        # Should the singular name come first when creating canonical identifiers for this set?
        'kind_first': True,
        # Function which each feature will be passed to in order to extract its "external_id" property
        # The utils module contains several generic functions for doing this
        'ider': utils.simple_namer(['KEY']),
        # Function which each feature will be passed to in order to extract its "name" property
        'namer': utils.simple_namer(['NAME']),
        # Authority that is responsible for the accuracy of this data
        'authority': 'NJ Geographic Information Network',
        # Geographic extents which the boundary set encompasses
        'domain': 'New Jersey',
        # Last time the source was checked for new data
        'last_updated': date(2012, 12, 27),
        # A url to the source of the data
        'href': 'https://njgin.state.nj.us/NJ_NJGINExplorer/jviewer.jsp?pg=DataDownloads',
        # Notes identifying any pecularities about the data, such as columns that were deleted or files which were merged
        'notes': '',
        # Encoding of the text fields in the shapefile, i.e. 'utf-8'. If this is left empty 'ascii' is assumed
        'encoding': '',
        # SRID of the geometry data in the shapefile if it can not be inferred from an accompanying .prj file
        # This is normally not necessary and can be left undefined or set to an empty string to maintain the default behavior
        'srid': ''
    },
    'New Jersey Counties': {
        'file': 'nj_boundaries/nj_counties.shp',
        'singular': 'County',
        'kind_first': True,
        'ider': utils.simple_namer(['FIPSSTCO']),
        'namer': utils.simple_namer(['COUNTY']),
        'authority': 'NJ Geographic Information Network',
        'domain': 'New Jersey',
        'last_updated': date(2012, 12, 27),
        'href': 'https://njgin.state.nj.us/NJ_NJGINExplorer/jviewer.jsp?pg=DataDownloads',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Congressional Districts': {
        'file': 'tl_2012_us_cd112/tl_2012_us_cd112.shp',
        'singular': 'Congressional District',
        'kind_first': True,
        'ider': utils.simple_namer(['CD112FP']),
        'namer': utils.simple_namer(['NAMELSAD']),
        'authority': 'U.S. Census Bureau',
        'domain': 'United States',
        'last_updated': date(2012, 12, 27),
        'href': 'http://www.census.gov/geo/maps-data/data/tiger-line.html',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Elementary School Districts': {
        'file': 'tl_2012_34_elsd/tl_2012_34_elsd.shp',
        'singular': 'Elementary school district',
        'kind_first': True,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census Bureau',
        'domain': 'New Jersey',
        'last_updated': date(2012, 12, 27),
        'href': 'http://www.census.gov/geo/maps-data/data/tiger-line.html',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Secondary School Districts': {
        'file': 'tl_2012_34_scsd/tl_2012_34_scsd.shp',
        'singular': 'Secondary school district',
        'kind_first': True,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census Bureau',
        'domain': 'New Jersey',
        'last_updated': date(2012, 12, 27),
        'href': 'http://www.census.gov/geo/maps-data/data/tiger-line.html',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Unified School Districts': {
        'file': 'tl_2012_34_unsd/tl_2012_34_unsd.shp',
        'singular': 'Unified school district',
        'kind_first': True,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census Bureau',
        'domain': 'New Jersey',
        'last_updated': date(2012, 12, 27),
        'href': 'http://www.census.gov/geo/maps-data/data/tiger-line.html',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Urban Enterprise Zones': {
        'file': 'UEZ_shp/UEZ_Statewide.shp',
        'singular': 'Urban Enterprise Zone',
        'kind_first': True,
        'ider': utils.simple_namer(['CONTACT_ID']),
        'namer': utils.simple_namer(['MUNICIPAL']),
        'authority': 'NJ Geographic Information Network',
        'domain': 'New Jersey',
        'last_updated': date(2012, 12, 27),
        'href': 'https://njgin.state.nj.us/NJ_NJGINExplorer/jviewer.jsp?pg=DataDownloads',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'State Legislative Districts': {
        'file': 'LegDist/DistrictBoundaries_Adopted04032011.shp',
        'singular': 'State legislative district',
        'kind_first': True,
        'ider': utils.simple_namer(['ID']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'NJ Geographic Information Network',
        'domain': 'New Jersey',
        'last_updated': date(2012, 12, 27),
        'href': 'https://njgin.state.nj.us/NJ_NJGINExplorer/jviewer.jsp?pg=DataDownloads',
        'notes': '',
        'encoding': '',
        'srid': ''
    }
}
