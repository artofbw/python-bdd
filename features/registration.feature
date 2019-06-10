Feature: Registration new user

  Scenario: Going to the registration page
    Given Page https://qa-has-power.herokuapp.com/ is loaded
    When I am sure that "Zadzwoń do nas" text is visible on the page
    And I am sure that page is ready to use
    Then I click "Zarejestruj się" link

  Scenario: Filling up registration form
    Given Page https://qa-has-power.herokuapp.com/register is loaded
    When I am sure that "Zadzwoń do nas" text is visible on the page
    And I am sure that page is ready to use
    Then I fill Register form with values
      | field_type | field_label     | field_value            |
      | input      | Imię i nazwisko | Test user              |
      | input      | Email           | test123@mailinator.com |
      | input      | Hasło           | test123                |
      | input      | Powtórz hasło   | test123                |
    Then ipdb
