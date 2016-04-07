Feature: Feed bulk data into gis.lib.virginia.edu
  In order to make my data available to students, other researchers, or the public
  As a GIS specialist
  I want to be able to bulk upload a lot of data

  @priority1
  Scenario: Upload through webform
    Given I have multiple layers of GIS data, each bundled into one file,
    And I want to upload them into Virgo
    When I navigate to the upload site
    Then it provides a form I can use to upload all the layers.

  @priority5
  Scenario: Upload through ArcGIS
    Given there are a number of layers in ArcGIS
    And I want to upload it all into Virgo
    When I use the Virgo Bulk Upload Tool in ArcGIS
    Then it automatically uploads all layers into Virgo

  @priority4
  Scenario: View status of uploads
    Given I want to be able to track my uploads
    And see if there are problems uploading my data
    When I have uploaded my data
    Then I should be able to see its progress being imported into Virgo

