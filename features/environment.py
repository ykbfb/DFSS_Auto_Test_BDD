from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

# def after_tag(context, tag):
#     context.tag = tag
#     if context.tag == '@Then':
#         context.driver.close()
#     else:
#         print('tag error')

def after_all(context):
    context.driver.quit()
