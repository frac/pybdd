Feature: Pets in the house
    As a home owner 
    I want to know how many pets I have

Scenario: search for cats
    Given
        I am a home owner
        I have some cats in my home
        I have a dog in my home
    When
        I search for cats
    Then
        I should find 3 cats


Scenario: search for dogs
    Given
        I am a home owner
        I have some cats in my home
        I have a dog in my home
    When
        I search for dogs
    Then
        I should find 1 dog
            
