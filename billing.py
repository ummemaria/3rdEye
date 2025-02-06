def add_billing(page):
    page.goto("https://3rd-eye-ed-mate-qa.mpower-social.com/batches?batchName=")

    page.wait_for_load_state("domcontentloaded")
    # page.locator("//p[contains(text(),'Batches')]").click()
    page.locator("//a[contains(text(),'CSE Day')]").click(timeout=6000)  # Wait up to 60s
    page.locator("//a[@id='simple-tab-5']").click(timeout=4000)
    
    page.locator("//button[contains(., 'Add New Fee')]").click(timeout=5000)
    
    page.locator("//label[contains(text(),'Fee Title')]/following-sibling::div//input").fill("Rime")
    
    page.locator("//label[contains(text(),'Amount')]/following-sibling::div//input").fill("20000")
    
    add_payment= page.locator("//label[contains(text(),'Payment Frequency')]/following-sibling::div//input")
    add_payment.click(timeout=4000)
    clear_payment= page.locator('button[aria-label="close"]:has(svg[data-testid="CloseIcon"])')
    clear_payment.click(timeout=5000)
    add_payment.click(timeout=6000)
    add_payment.fill("One Time")
    
    page.locator("//li[contains(text(), 'One Time')]").click()
    
    add_charge= page.locator("//label[contains(text(),'Charge Event')]/following-sibling::div//input")
    add_charge.click(timeout=4000)
    add_charge.fill("Monthly")
    page.locator("//li[contains(text(), 'Monthly')]").click()
    
    page.locator("//label[contains(text(),'Organization Percentage')]/following-sibling::div//input").fill("2")
    
    page.locator("//button[text()='Add']").click()
    
    page.locator("//button[text()='Charge Fees']").click(timeout=5000)
    
    add_charge= page.locator("//label[contains(text(),'Fees')]/following-sibling::div//input")
    add_charge.click(timeout=5000)
    page.fill("//label[contains(text(),'Fees')]/following-sibling::div//input", "Ace Exam")
    add_charge.click(timeout=4000)
    add_charge.fill("Ace Exam")
    page.locator("//li[contains(text(), 'Ace Exam')]").click(timeout=5000)
    
    add_student= page.locator("//label[contains(text(),'Students')]/following-sibling::div//input")
    add_student.click(timeout=4000)
    add_student.fill("ddd ddd")
    # Locate the checkbox using the class
    checkbox = page.locator('input[type="checkbox"]')
    checkbox.check()
    page.locator("button[title='Close']").click()
    page.locator("button[type='submit']").click()
    
    
    
    # Locate the button containing the SVG icon and click it
    
    
    user_icon = page.locator('button:has(svg.tabler-icon-user-check)')
    user_icon.click()
   
    tab = page.locator('a:has-text("Student")')
    tab.click()
 
 
   
    # Locate the input by placeholder
    search_field = page.locator('input[placeholder="Search Student"]')
 
    # Click to focus and type into the input
    search_field.click()
    search_field.fill('ddd')
   
    # Locate and click the link based on visible text
    link = page.locator('a:has-text("ddd ddd")')
    link.click()
   
    # Locate and click the tab based on visible text
    tab = page.locator('a:has-text("Billing")')
    tab.click()
 
    
   






    
    
    
    
    




    

    
      


    




