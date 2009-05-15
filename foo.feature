Feature: Pets in the house
    As a home owner 
    I want to know how many pets I have

Scenario: search for cats
    Given
        I am a home owner
    And 
        I have some cats in my home
        I have a dog in my home
    When
        I search for cats
    Then
        I should find 3 cats
