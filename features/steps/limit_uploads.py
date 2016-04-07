from behave import *


@given('I want to be able to limit access to uploading layers')
def step_impl(context):
    raise NotImplementedError


@when('someone tries to access the upload site')
def step_impl(context):
    raise NotImplementedError


@then('they should only be permitted to if they are a valid, active user')
def step_impl(context):
    raise NotImplementedError


@given('I want to be able to limit access to uploading directly into Virgo')
def step_impl(context):
    raise NotImplementedError


@when('someone tries to upload through the Virgo ArcGIS Tool')
def step_impl(context):
    raise NotImplementedError


@then('they should be required to authenticate with Shibboleth')
def step_impl(context):
    raise NotImplementedError


@given('I want to be able to review uploads after they are processed and before they are published')
def step_impl(context):
    raise NotImplementedError


@then('it should notify the data curator that data is available to be approved.')
def step_impl(context):
    raise NotImplementedError


@given('I want to be able to approve uploads before they are published')
def step_impl(context):
    raise NotImplementedError


@then('I should be able to approve the data through the webform.')
def step_impl(context):
    raise NotImplementedError


@given('I want to be able to deny approval for some data before they are published')
def step_impl(context):
    raise NotImplementedError


@when('the system has finished processing uploaded data')
def step_impl(context):
    raise NotImplementedError


@then('I should be able to deny approval through the webform.')
def step_impl(context):
    raise NotImplementedError


@given('I want upload users to have notification of the status of their data')
def step_impl(context):
    raise NotImplementedError


@when('data has been reviewed by the data curator')
def step_impl(context):
    raise NotImplementedError


@then('the users should be notified of its status.')
def step_impl(context):
    raise NotImplementedError


