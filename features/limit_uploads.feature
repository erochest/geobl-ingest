Feature: Limit upload access
  In order to control use of disk space and University IT resources
  As a data curator 
  I want to be able to limit upload rights to those affiliated with the University

  @priority2
  Scenario: authentication via webform
    Given I want to be able to limit access to uploading directly into Virgo
    When someone tries to access the upload site
    Then they should be required to authenticate with shibboleth

  @priority3
  Scenario: Only valid users can access the webform
    Given I want to be able to limit access to uploading layers
    When someone tries to access the upload site
    Then they should only be permitted to if they are a valid, active user

  @priority5
  Scenario: authentication via ArcGIS
    Given I want to be able to limit access to uploading directly into Virgo
    When someone tries to upload through the Virgo ArcGIS Tool
    Then they should be required to authenticate with Shibboleth

  @priority4
  Scenario: Admins are notified via email
    Given I want to be able to review uploads after they are processed and before they are published
    When the system has finished processing uploaded data
    Then it should notify the data curator that data is available to be approved.

  @priority4
  Scenario: Approval via webform
    Given I want to be able to approve uploads before they are published
    When the system has finished processing uploaded data
    Then I should be able to approve the data through the webform.

  @priority4
  Scenario: Deny approval via webform
    Given I want to be able to deny approval for some data before they are published
    When the system has finished processing uploaded data
    Then I should be able to deny approval through the webform.

  @priority4
  Scenario: Notify users of data’s approval status
    Given I want upload users to have notification of the status of their data
    When data has been reviewed by the data curator
    Then the users should be notified of its status.

