from behave import given, when, then
import time


@given(u'I navigate to login page')
def step_impl(context):
    context.browser.get('https://www.google.com/')


@when(u'I enter valid username and password')
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@title='Search']").send_keys("ice cream")


@when(u'I click on Submit button')
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@title='Search']").submit()


@then(u'login is successful')
def step_impl(context):
    pass

@given(u'I navigate to amazon.in')
def step_impl(context):
    context.browser.get('https://www.amazon.in/')

@when(u'I click on sign up')
def step_impl(context):
    context.browser.find_element_by_xpath("//span[.='Hello, sign in']").click()

@when(u'I enter username and password for amazon')
def step_impl(context):
    context.browser.find_element_by_id("ap_email").send_keys("kashifamansoor1995@gmail.com")
    context.browser.find_element_by_id("continue").click()
    context.browser.find_element_by_id("ap_password").send_keys("chulbul2020")
@when(u'I click on signIn button')
def step_impl(context):
    context.browser.find_element_by_id("signInSubmit").click()

@then(u'Kashi is seen on login')
def step_impl(context):
    pass