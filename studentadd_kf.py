from datetime import datetime

def select_dropdown_option(page, dropdown_label, option_text):
    """Select an option from a dropdown by clicking it and choosing a value."""
 
    # Click the dropdown field based on its visible text
    page.locator(f"//div[normalize-space()='{dropdown_label}']").click()
 
    # Wait for the dropdown options to load
    page.wait_for_selector("//li[@role='option']", timeout=5000)
 
    # Click the option with the specified text
    page.locator(f"//li[normalize-space()='{option_text}']").click()
    
def add_student(page):
    page.goto("https://3rd-eye-ed-mate-qa.mpower-social.com/batches?batchName=")

    page.wait_for_load_state("domcontentloaded")
    

    ## Navigate to students tab
    page.locator("(//button[@aria-label='theme-icon'])[5]").click()

    # Wait for the "Sorry, no matching records found" text to disappear
    #page.wait_for_selector("text=Sorry, no matching records found", state="hidden", timeout=30000)
    #page.wait_for_selector("//tr[@data-testid='MUIDataTableBodyRow-0']", state="visible", timeout=30000)


    

    ## WAit until add new student is visible
    #page.wait_for_selector("//button[normalize-space()='Add New Student']", state="visible", timeout=10000)

    page.click("//a[@role='tab' and contains(., 'Student')]")

    ## Click Add new student
    page.locator("//button[normalize-space()='Add New Student']").click()

    ## Send values at firstname field
    page.locator("//input[@name='firstName']").fill("Montyy")
 
    ## Send values at lastname field
    page.locator("//input[@name='lastName']").fill("Babuu")

    ## Send values for contact number
    page.locator("//input[@name='contactNo']").fill("01122330003")

    ## Send value email field
    page.locator("//input[@name='email']").fill("montybabuu@gmail.com")

    # ## Select date 
    # page.locator("//button[@aria-label='Choose date']").click()
    # today = datetime.now().strftime("%d")  # Get day as a two-digit number (e.g., '21')

    # # Remove leading zero if your calendar uses single-digit days for the first 9 days
    # if today.startswith("0"):
    #     today = today[1:]

    # page.locator(f"//button[normalize-space()='{today}']").click()

    # Clear the input field first
    date_input = page.locator("label:has-text('Date of Birth') ~ div input[placeholder='DD/MM/YYYY']")
    date_input.fill("")  # Clears the field

    # Type the full date
    date_input.type("09/9/2000")    

    ## Select blood group dropdown
    page.locator("//div[.='Blood Group']").click()

    ## wait fpr list
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select blood group 
    page.locator("//li[normalize-space()= 'O (+ve)']").click()

    ##Select Division
    page.locator("//div[.='Division']").click()

    ## wait for list
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select division
    page.locator("//li[normalize-space()= 'DHAKA']").click()

    ## Select district
    page.locator("//div[.='District']").click()

    ## Select district
    page.locator("//li[normalize-space()= 'DHAKA']").click()

    ## Give address
    page.locator("//textarea[@name='address']").fill("346/6, Lake Circus")

    ## Open school dropdown
    page.locator("//div[.='School']").click()
 
    ## wait for list
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Give school
    page.locator("//li[normalize-space()= 'Aga Khan Academy']").click()

    ## Click gender
    page.locator("//input[@value='female']").click()
    
    ##Scroll down
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    ## Give username
    page.locator("//input[@name='userName']").fill("mmmontybabuu")

    ## Give password
    page.fill("//input[@name='password']", "12345678")

    ## Click Next button
    page.wait_for_timeout(5000)
    page.locator("//button[normalize-space()='Next']").click()
    

    # ##--------------Step 2 --------------------------
    
    page.locator("//div[.='Search Guardin']").click()
    page.wait_for_selector("//li[@role='option']", timeout=5000)
    page.locator("//li[normalize-space()= 'Tanvir Islam']").click()
    
    

    ## Select guardian first Name
    # page.locator("//input[@name='guardian[0].relationId.firstName']").fill("Edtechy")

    ## Select guardian last name
    # page.locator("//input[@name='guardian[0].relationId.lastName']").fill("Father")

    ## Select guardian contact no
    # page.locator("//input[@name='guardian[0].relationId.contactNo']").fill("01122330002")

    ##Select guardian email
    # page.locator("//input[@name='guardian[0].relationId.email']").fill("edtechyf102@edmate.com")

    ## Select relation with student
    # page.locator("//div[.='Relation with student']").click()

    ## wait for list
    # page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select father
    # page.locator("//li[normalize-space()= 'Father']").click()

    ## Select primary guardian
    # page.locator("//input[@name='saveCard']").click()

    ## Select username
    # page.locator("//input[@name='guardian[0].relationId.userName']").fill("edtechyf102")

    ## Select password
    # page.locator("//input[@name='password']").fill("12345678")

    ## Scroll to last
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    ## Click next
    page.wait_for_timeout(5000)
    page.locator("//button[normalize-space()='Next']").click()
    

    # ##-------------Step 3---------------

## Click next from batch enrollment
    
    
    
    # If there's a checkbox inside the button, adjust the locator
    # page.locator("//label[contains(text(), 'Batches')]/following-sibling::div//input[@type='checkbox']").check()

 
    # # Wait for the options to appear and select an option by text
    # option_locator = "//ul[@role='listbox']//li[contains(text(), 'holllla')]"
    # page.locator(option_locator).check()
    
    # page.locator(get_batches_checkbox("holllla")).check(force=True)
    # page.wait_for_timeout(3000)
    # assert page.locator(get_batches_checkbox("holllla")).is_checked()
    
    
    # page.get_by_label("Batches").click()
    # Check the checkbox associated with the "Test 1" label
    # page.locator("//label[contains(text(), 'Test 1')]/preceding-sibling::input").check()
    page.locator("//label[contains(text(),'Batches')]/following-sibling::div//input").click()

    page.locator(".PrivateSwitchBase-input").first.check()
    # page.locator("div:nth-child(2) > .MuiButtonBase-root > .PrivateSwitchBase-input").check()
    # page.locator("div:nth-child(4) > .MuiButtonBase-root > .PrivateSwitchBase-input").check()
    
    page.wait_for_timeout(2000)
    page.locator("button[title='Close'] svg").click()
    page.wait_for_timeout(2000)
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.locator("//button[normalize-space()='Next']").click()
    
    # select_dropdown_option(page, "Batches", "Test 1")
    # page.wait_for_timeout(5000)
    
    # page.locator("//button[normalize-space()='Next']").click()

    # ##--------------------Step 4 ---------------------

    ## Review and submit
    page.wait_for_timeout(5000)
    page.locator("//button[normalize-space()='Submit']").click()
    page.wait_for_timeout(10000)

    ##Get the message
    message_text = page.text_content("//p[@id='alert-dialog-description']")

    # Validate the message
    assert "User with details created successfully" in message_text, "Confirmation message validation failed"

    print("Confirmation message validated successfully!")

    ##  Close the success message
    page.wait_for_timeout(5000)
    page.locator("//button[@aria-label='Close']").click()

    





