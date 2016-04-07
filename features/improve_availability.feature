Feature: Improve the data's availability through Virgo
  In order to improve others' ability to find data through Virgo
  As a GIS specialist, librarian, or researcher
  I want to be able to associate appropriate metadata with the uploaded resources

  @priority1
  Scenario: Automatically detect metadata
    Given I want data to be searchable through Virgo
    When I upload it
    Then it should automatically gather metadata intrinsic to the data formats

  @priority2
  Scenario: View current metadata
    Given I want to know what I've uploaded to Virgo
    When the data has been uploaded
    And they visit the upload site
    Then I can see the metadata associated with the resources

  @priority2
  Scenario: Enter new metadata or correct existing metadata
    Given I want full and correct metadata to be used by Virgo
    When the data is submitted to upload or afterward
    And after I have a chance to review it
    Then I can revise or add to the metadata

