import time
from behave import *
from elements import Icd10DataMainPage
from functions.GeneralFunctions import General_Functions
from assertpy import assert_that

functions = General_Functions()


@step('check the presence of the website logo and its name "{name}" on the logo on the page.')
def step_impl(self, name):
    functions.implicit_wait_present(Icd10DataMainPage.logo)


@step('check that there is a "{btn}" button in the menu bar of the page.')
def step_impl(self, btn):
    functions.implicit_wait_visible(Icd10DataMainPage.menuBar)
    elements = self.driver.find_elements(*Icd10DataMainPage.menuBar)
    x = len(elements)
    j = 1
    for i in elements:
        if btn in i.text:
            print("Button visible in Menu Bar")
            break
        elif x == j:
            raise ValueError("Button is not visible in Menu Bar")
        j += 1

@step('check that when you click on the "{btn}" button, a drop-down menu opens.')
def step_impl(self, btn):
    functions.implicit_wait_visible(Icd10DataMainPage.menuBar)
    element = self.driver.find_element(*Icd10DataMainPage.menuCodes)
    assert_that(element.text).contains(btn)
    functions.click_element(Icd10DataMainPage.menuCodes)
    functions.implicit_wait_visible(Icd10DataMainPage.menuCodesOpen)


@step("check that the disease search field by code is located at the top of the page")
def step_impl(self):
    functions.implicit_wait_visible(Icd10DataMainPage.searchField)
    locationElement = self.driver.find_element(*Icd10DataMainPage.searchField).location
    assert_that(locationElement["y"]).is_less_than(50)


@step('check that the search result "{result}" we need is on the page that opens.')
def step_impl(self, result):
    functions.implicit_wait_visible(Icd10DataMainPage.searchResults)
    elements = self.driver.find_elements(*Icd10DataMainPage.searchResults)
    x = len(elements)
    j = 1
    for i in elements:
        if result in i.text:
            print("Result found")
            print("Result " + str(j) + ":" + i.text)
            break
        elif x == j:
            raise ValueError("Result not found")
        j += 1

