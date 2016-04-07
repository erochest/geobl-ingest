Feature: Feed individual data into gis.lib.virginia.edu
  In order to make my data available to students, other researchers, or the public
  As a GIS specialist, librarian, or researcher
  I want to be able to upload my data.

  @priority1
  Scenario: Upload through a web interface
    Given I have a layer of GIS data bundled in one file
    And I want to upload it into Virgo
    When I navigate to the upload site
    Then it provides a form I can use to upload data.

  @priority5
  Scenario: Upload through ArcGIS
    Given I have a layer in ArcGIS
    And I want to upload it into Virgo
    When I use the Virgo Upload Tool in ArcGIS
    Then it automatically uploads the selected layers into Virgo.

  @priority4
  Scenario: View status of uploads
    Given I want to be able to track my uploads
    And see if there are problems uploading my data
    When I have uploaded my data
    Then I should be able to see its progress and error status being imported into Virgo

