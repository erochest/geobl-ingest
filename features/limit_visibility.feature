Feature: Limit visibility to prevent the data from being URL-only, searchable, or visible off-grounds
  In order to be able to make resources with IP restrictions available to the University community
  As a GIS specialist, librarian, or researcher
  I want to be able to limit resources' to being URL-only, searchable, and visible to on-grounds only

  @priority2
  Scenario: during upload via webform
    Given I am uploading features from the webform
    When I upload
    Then I am presented with options for limiting visibility

  @priority5
  Scenario: during upload via ArcGIS
    Given I am uploading features from ArcGIS
    When I upload
    Then I am presented with options for limiting visibility

  @priority4
  Scenario: after upload
    Given I have uploaded features
    And I wish to change its visibility
    When I visit the status/metadata-editing page
    Then I am presented with options for changing visibility

