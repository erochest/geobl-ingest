from behave import *


@given('I have a layer of GIS data bundled in one file')
def step_impl(context):
    raise NotImplementedError


@then('it provides a form I can use to upload data.')
def step_impl(context):
    raise NotImplementedError


@given('I have a layer in ArcGIS')
def step_impl(context):
    raise NotImplementedError


@given('I want to upload it into Virgo')
def step_impl(context):
    raise NotImplementedError


@when('I use the Virgo Upload Tool in ArcGIS')
def step_impl(context):
    raise NotImplementedError


@then('it automatically uploads the selected layers into Virgo.')
def step_impl(context):
    raise NotImplementedError


@then('I should be able to see its progress and error status being '
      'imported into Virgo')
def step_impl(context):
    raise NotImplementedError
