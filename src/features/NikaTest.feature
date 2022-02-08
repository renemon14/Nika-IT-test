@Test
Feature: Tests on te website icd10data.com

  Scenario: Assertions on the page
    Given site to navigate: "https://www.icd10data.com/"
    Then check the presence of the website logo and its name "icd10data" on the logo on the page.
    And check that there is a "Codes" button in the menu bar of the page.
    And check that when you click on the "Codes" button, a drop-down menu opens.
    And check that the disease search field by code is located at the top of the page
    When enter the Coronavirus code "Covid-19" in the search field and click the search button.
    Then check that the search result "COVID-19" we need is on the page that opens.
