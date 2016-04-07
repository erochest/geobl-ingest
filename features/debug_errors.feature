Feature: Debug errors
  In order to better support users who are uploading data
  As a technical administrator
  I want to be able to view detailed error information.

  @priority4
  Scenario: View detailed error information
    Given I want to be able to track processing status
    And I want to be able to view detailed error information
    When I view a failed upload job on the web interface
    Then I should see traceback and other error information associated with that upload.

