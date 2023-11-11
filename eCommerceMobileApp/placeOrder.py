import time

import self as self
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
# from appium_flutter_finder import FlutterElement, FlutterFinder
# from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.common.mobileby import MobileKeys

desired_cap = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "com.nopstation.nopcommerce.nopstationcart",
    "appWaitActivity": "com.bs.ecommerce.main.MainActivity",
    "app": "C:\\Users\\kazia\\AppData\\Local\\Android\\Sdk\\platform-tools\\nopstationCart_4.40.apk"
}
options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
time.sleep(5)

# Adding Products
try:
    # Accepting the terms
    accept = "com.nopstation.nopcommerce.nopstationcart:id/btnAccept"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=accept,
    )
    element.click()
    time.sleep(2)

    # Click on electronics
    menu = '//android.widget.ImageButton[@content-desc="NopStation Cart"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=menu,
    )
    element.click()
    time.sleep(2)

    electronics = '(//android.widget.ImageView[@content-desc="Placeholder"])[2]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=electronics,
    )
    element.click()
    time.sleep(2)

    # Scroll down
    burger = '(//android.widget.ImageView[@content-desc="Placeholder"])[16]'
    burgerElement = driver.find_element(
        by=AppiumBy.XPATH,
        value=burger,
    )
    action = TouchAction(driver)
    action.long_press(burgerElement).move_to(x=0, y=0).release().perform()
    # element.click()
    time.sleep(2)

    # Click to mattress bedroom
    mattressBedroom = '(//android.widget.ImageView[@content-desc="Placeholder"])[5]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=mattressBedroom,
    )
    element.click()
    time.sleep(5)

    # Scroll down
    img = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ImageView"
    imgElement = driver.find_element(
        by=AppiumBy.XPATH,
        value=img,
    )
    action = TouchAction(driver)
    action.long_press(imgElement).move_to(x=0, y=0).release().perform()
    time.sleep(3)

    # Clicking plus button
    plusBtn = "com.nopstation.nopcommerce.nopstationcart:id/btnPlus"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=plusBtn,
    )
    element.click()
    time.sleep(2)

    # Adding products to the cart
    addToCart = "com.nopstation.nopcommerce.nopstationcart:id/btnAddToCart"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=addToCart,
    )

    element.click()
    time.sleep(5)

    print('Adding Products: Successful ✔')
except Exception as e:
    print('Adding Products: Failed! 👎')
    print(f"Error when Adding Products: {e}")

# Place Order
try:
    print("place order")
    # Got to Cart
    cart = "com.nopstation.nopcommerce.nopstationcart:id/counterIcon"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=cart,
    )
    element.click()
    time.sleep(2)

    # Clicking Checkout
    checkOut = "com.nopstation.nopcommerce.nopstationcart:id/btnCheckOut"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=checkOut,
    )
    element.click()
    time.sleep(2)

    # Checkout as a Guest
    guest = "com.nopstation.nopcommerce.nopstationcart:id/btnGuestCheckout"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=guest,
    )
    element.click()
    time.sleep(2)

    # Input all the details
    firstName = "com.nopstation.nopcommerce.nopstationcart:id/etFirstName"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=firstName,
    )
    element.click()
    element.send_keys('Mike')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    lastName = "com.nopstation.nopcommerce.nopstationcart:id/etLastName"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=lastName,
    )
    element.click()
    element.send_keys('Ahmed')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    email = "com.nopstation.nopcommerce.nopstationcart:id/etEmail"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=email,
    )
    element.click()
    element.send_keys('mike@gmail.com')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    country = "com.nopstation.nopcommerce.nopstationcart:id/countrySpinner"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=country,
    )
    element.click()
    time.sleep(5)

    # Scroll down
    img = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[14]'
    imgElement = driver.find_element(
        by=AppiumBy.XPATH,
        value=img,
    )
    action = TouchAction(driver)
    action.long_press(imgElement).move_to(x=0, y=0).release().perform()
    time.sleep(3)

    img = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[15]'
    imgElement = driver.find_element(
        by=AppiumBy.XPATH,
        value=img,
    )
    action = TouchAction(driver)
    action.long_press(imgElement).move_to(x=0, y=0).release().perform()
    time.sleep(3)

    selectCountry = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[13]"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=selectCountry,
    )
    element.click()
    time.sleep(5)

    img = 'com.nopstation.nopcommerce.nopstationcart:id/etEmail'
    imgElement = driver.find_element(
        by=AppiumBy.ID,
        value=img,
    )
    action = TouchAction(driver)
    action.long_press(imgElement).move_to(x=0, y=0).release().perform()
    time.sleep(3)

    state = "com.nopstation.nopcommerce.nopstationcart:id/stateSpinner"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=country,
    )
    element.click()
    time.sleep(5)

    selectState = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/" \
                      "android.widget.TextView[2]"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=selectState,
    )
    element.click()
    time.sleep(5)

    company = "com.nopstation.nopcommerce.nopstationcart:id/etCompanyName"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=company,
    )
    element.click()
    element.send_keys('Brain Station 23')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    city = "com.nopstation.nopcommerce.nopstationcart:id/etCity"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=city,
    )
    element.click()
    element.send_keys('Dhaka')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    address = "com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=address,
    )
    element.click()
    element.send_keys('Mirpur DOHS, Dhaka')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    # Scroll Down
    img = 'com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress'
    imgElement = driver.find_element(
        by=AppiumBy.ID,
        value=img,
    )
    action = TouchAction(driver)
    action.long_press(imgElement).move_to(x=0, y=0).release().perform()
    time.sleep(3)

    zipCode = "com.nopstation.nopcommerce.nopstationcart:id/etZipCode"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=zipCode,
    )
    element.click()
    element.send_keys('1216')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    phone = "com.nopstation.nopcommerce.nopstationcart:id/etPhone"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=phone,
    )
    element.click()
    element.send_keys('01731528978')
    # time.sleep(2)
    # driver.press_keycode(66)
    time.sleep(5)

    con = 'com.nopstation.nopcommerce.nopstationcart:id/btnContinue'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=con,
    )
    element.click()
    time.sleep(10)

    opt = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/com.bs.ecommerce.customViews.RadioGridGroupforReyMaterial/android.widget.RelativeLayout[4]"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=opt,
    )
    element.click()
    time.sleep(5)

    # Scroll down
    img = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/com.bs.ecommerce.customViews.RadioGridGroupforReyMaterial/android.widget.RelativeLayout[2]'
    imgElement = driver.find_element(
        by=AppiumBy.XPATH,
        value=img,
    )
    action = TouchAction(driver)
    action.long_press(imgElement).move_to(x=0, y=0).release().perform()
    time.sleep(3)

    con1 = "com.nopstation.nopcommerce.nopstationcart:id/btnContinue"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=con1,
    )
    element.click()
    time.sleep(5)

    # Scroll down
    img = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/com.bs.ecommerce.customViews.RadioGridGroupforReyMaterial/android.widget.RelativeLayout[6]'
    imgElement = driver.find_element(
        by=AppiumBy.XPATH,
        value=img,
    )
    action = TouchAction(driver)
    action.long_press(imgElement).move_to(x=0, y=0).release().perform()
    time.sleep(3)

    # Scroll down
    img = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/com.bs.ecommerce.customViews.RadioGridGroupforReyMaterial/android.widget.RelativeLayout[6]'
    imgElement = driver.find_element(
        by=AppiumBy.XPATH,
        value=img,
    )
    action = TouchAction(driver)
    action.long_press(imgElement).move_to(x=0, y=0).release().perform()
    time.sleep(3)

    money = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/com.bs.ecommerce.customViews.RadioGridGroupforReyMaterial/android.widget.RelativeLayout[4]"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=money,
    )
    element.click()
    time.sleep(5)

    con2 = "com.nopstation.nopcommerce.nopstationcart:id/btnContinue"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=con2,
    )
    element.click()
    time.sleep(5)

    nxt = "android.widget.Button"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=nxt,
    )
    element.click()
    time.sleep(5)

    confirm = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[10]"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=confirm,
    )
    element.click()
    time.sleep(5)

    con3 = "com.nopstation.nopcommerce.nopstationcart:id/md_button_positive"
    element = driver.find_element(
        by=AppiumBy.ID,
        value=con3,
    )
    element.click()
    time.sleep(5)

    print('Order Place: Successful ✔')
except Exception as e:
    print('Order Place: Failed! 👎')
    print(f"Error when Order Place: {e}")

    driver.close()
