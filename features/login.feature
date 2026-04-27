Feature: Login functionality

  Scenario: Successful login
    Given user is on login page
    When user enters valid username and password
    And clicks on login button
    Then user should see success message

  Scenario: Invalid login
    Given user is on login page
    When user enters invalid username and password
    And clicks on login button
    Then user should see error message
