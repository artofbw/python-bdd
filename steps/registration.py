from behave import given, when, then, step, use_step_matcher
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


use_step_matcher('re')

TIME_IN_SECONDS = 10


@given('Page (?P<url>.*) is loaded')
def step_impl(context, url):
    context.browser.get(url)


@step('I am sure that "(?P<text>.*)" text is visible on the page')
def step_impl(context, text):
    wait = WebDriverWait(context.browser, TIME_IN_SECONDS)
    wait.until(
        EC.presence_of_element_located((
            By.XPATH, f'//*[contains(text(), "{text}")]',
        ))
    )


@step('I am sure that page is ready to use')
def step_impl(context):
    wait = WebDriverWait(context.browser, TIME_IN_SECONDS)
    wait.until(EC.presence_of_element_located((
        By.XPATH, '//div[@class="se-pre-con" and @style="display: none;"]'
    )))


@step('I click (?P<name>.*) (?P<click_type>button|link)')
def step_impl(context, name, click_type):
    tag = {
        'button': 'button',
        'link': 'a',
    }
    import ipdb; ipdb.set_trace()
    element = context.browser.find_element_by_xpath(
        f'//{tag.get(click_type)}[contains(text(), {name})]'
    )
    element.click()


@step('I fill (?P<label>.*) form with values')
def step_impl(context, label):
    for row in context.table:
        field_label = row.get('field_label')
        field_value = row.get('field_value')
        field_type = row.get('field_type')

        element = context.browser.find_element_by_xpath(
            f'//h1[contains(text(), "{label}")]//'
            'following-sibling::form//'
            f'label[contains(text(), "{field_label}")]/'
            f'ancestor::div[1]/following-sibling::div/{field_type}'
        )
        element.send_keys(field_value)


@step('ipdb')
def step_impl(context):
    import ipdb; ipdb.set_trace()
