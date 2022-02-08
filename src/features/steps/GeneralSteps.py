import time
from behave import *
from elements import Icd10DataMainPage
from functions.GeneralFunctions import General_Functions

functions = General_Functions()


@step('site to navigate: "{url}"')
def step_impl(self, url):
    self.driver.get(url)


@step('enter the Coronavirus code "{code}" in the search field and click the search button.')
def step_impl(self, code):
    functions.implicit_wait_visible(Icd10DataMainPage.searchField)
    functions.send_key(Icd10DataMainPage.searchField, code)
    functions.click_element(Icd10DataMainPage.btnSearch)

