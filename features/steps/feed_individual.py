from behave import *
import sure


@given('I have a layer of GIS data bundled in one file, {filename}')
def step_impl(context, filename):
    context.data_file = filename


@then('it provides a form I can use to upload data.')
def step_impl(context):
    data = context.response.data.decode('utf8')
    data.should.contain('Upload Form')
    data.should.contain('<input')


@given('I have a layer in ArcGIS')
def step_impl(context):
    raise NotImplementedError


@given('I want to upload it into Virgo')
def step_impl(context):
    pass


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
