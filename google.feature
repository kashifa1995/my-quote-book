Feature: Login
    """
        Login feature will test for successful and failed login attempts
    """

    Scenario: Success test for login
        Given I navigate to login page
        When I enter valid username and password
        And I click on Submit button
        Then login is successful

    Scenario: Amazon login Test
        Given I navigate to amazon.in
        When I click on sign up
        And I enter username and password for amazon
        And I click on signIn button
        Then Kashi is seen on login
