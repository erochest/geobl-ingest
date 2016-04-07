Feature: Valid user management
  In order to control who can upload data
  As a GIS specialist or technical administrator
  I want to be able to manage a list of users who have permission to upload layers

  @priority3
  Scenario: Add users
    Given I want to be able to allow users to upload layers
    When I visit the user management page,
    Then I can add users.

  @priority3
  Scenario: Bulk add users
    Given I want to be able to add multiple users to upload layers
    When I visit the user management page,
    Then I can upload a CSV file listing the users

  @priority3
  Scenario: List users
    Given I want to know who is allowed to upload data
    When I visit the user management page
    Then I can see a list of users.

  @priority3
  Scenario: Remove users
    Given I want to be able to prevent users from uploading layers
    When I visit the user management page
    Then I can remove users

  @priority5
  Scenario: Search valid UVa users
    Given I want to be able to accurately specify users to upload layers
    When I visit the user management page
    Then I should be able to search the UVa LDAP directory

  @priority3
  Scenario: Make users inactive
    Given I want to be able to temporarily prevent users from uploading layers
    When I visit the management page
    Then I should be able to mark a user as inactive

  @priority4
  Scenario: View users’ resources
    Given I want to be able to view the layers submitted by a user
    When I visit the user’s profile page
    Then I should see a list of layers submitted

