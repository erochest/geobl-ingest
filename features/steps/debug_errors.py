from behave import *


@given("I want to be able to track processing status")
def step_impl(context):
    raise NotImplementedError


@given("I want to be able to view detailed error information")
def step_impl(context):
    raise NotImplementedError


@when("I view a failed upload job on the web interface")
def step_impl(context):
    raise NotImplementedError


@then("I should see traceback and other error information associated with "
      "that upload.")
def step_impl(context):
    raise NotImplementedError
