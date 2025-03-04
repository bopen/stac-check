## STAC-CHECK Change Log

All notable changes to this project will be documented in this file.

The format is (loosely) based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).


## [Unreleased]
### Added
- recursive mode lints assets https://github.com/stac-utils/stac-check/pull/84
### Changed
- recursive mode swaps pystac for stac-validator https://github.com/stac-utils/stac-check/pull/84
### Fixed
- fix catalog file name check https://github.com/stac-utils/stac-check/pull/83

## [v1.2.0] - 2022-04-26
### Added
- Option to include a configuration file to ignore selected checks
### Changed
- Change name from stac_check to stac-check in setup for cli

## [v1.1.3] - 2022-03-03
- Fix thumbnail size check

## [v1.1.2] - 2022-03-03
- Fix self-link test 

## [v1.1.1] - 2022-03-02
- Make it easier to export linting messages

## [v1.0.3] - 2022-03-02
- Set stac-validator version to 2.4.0

## [v1.0.2] - 2022-02-21
- Loosen stac-validator version 

## [v1.0.1] - 2022-02-20
- Update readme

## [v1.0.0] - 2022-02-20
### Changed
- Reorganized code for version 1.0.0 release

## [v0.2.0] - 2022-02-02 - 2022-02-19
### Added
- Import main validator as stac-validator was updated to 2.3.0
- Added best practices docuument to repo
- Recommend 'self' link in links
- Check catalogs and collections use 'catalog.json' or 'collection.json' as a file name
- Check that links in collections and catalogs have a title field
- Recommend that eo:bands or similar information is provided in collection summaries
- Check for small thumbnail image file type

## [v0.1.3] - 2022-01-23
### Added
- Check for bloated metadata, too many fields in properties
- Check for geometry field, recommend that STAC not be used for non-spatial data

### Changed  
- Changed bloated links check to a boolean to mirror bloated metadata

## [v0.1.2] - 2022-01-17 - 2022-01-22
### Added
- Check for null datetime
- Check for unlocated items, bbox should be set to null if geometry is

## [v0.1.1] - 2021-11-26 - 2021-12-12
### Added  
- Added github actions to test and push to pypi
- Added makefile, dockerfile  

### Changed  
- Removed pipenv  

## [v0.1.0] - 2021-11-26 - 2021-12-05
### Added
- Best practices - searchable identifiers - lowercase, numbers, '_' or '-'
  for id names
  https://github.com/radiantearth/stac-spec/blob/master/best-practices.md#searchable-identifiers
- Best practices ensure item ids don't contain ':' or '/' characters  
  https://github.com/radiantearth/stac-spec/blob/master/best-practices.md#item-ids
- Best practices check for item ids to see if they match file names
- Add url support, check for valid urls, validate urls
- Add pystac validate_all to new cli option -> recursive
- Update pystac from 0.5.6 to 1.1.0
- Move stac-validator 2.3.0 into repository
- Best practices check for too many links in object
- Best practices check for summaries in collections
- Validation from stac-validator 2.3.0  
- Links and assets validation checks  
