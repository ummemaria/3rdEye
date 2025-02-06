from playwright.sync_api import sync_playwright
#from add_batch import add_batch
#from batchadd_kf import create_batch
from billing import add_billing
# from checkbill import add_billingcheck
from studentadd_kf import add_student
import json
import tkinter as tk

# File to load the authentication state
auth_file = "auth_state.json"
# root = tk.Tk()
# screenwidth = root.winfo_screenwidth()  
# screenheight = root.winfo_screenheight() 

def login_with_saved_state(playwright):
    """Create a browser context with saved login state."""
    # Load the saved authentication state
    with open(auth_file, "r") as f:
        auth_data = json.load(f)
       
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(storage_state=auth_data["storage"])
    # page = context.new_page()
    
    # Set the viewport size to the screen's dimensions
    # page.set_viewport_size({'width': screenwidth, 'height': screenheight})
    
    
    browser = playwright.chromium.launch(headless=False, args = ["--start-maximized"])
    context = browser. new_context(storage_state=auth_data["storage"], no_viewport = True)
    page = context.new_page()
    
    # browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    # context = browser.new_context(storage_state=auth_data["storage"])  # Removed 'no_viewport=True'
    # page = context.new_page()


    # Navigate to a known domain URL to initialize session storage
    base_url = "https://3rd-eye-ed-mate-qa.mpower-social.com/"
    page.goto(base_url)

    # Set the session token in session storage
    token = auth_data.get("session_token")
    if token:
        page.evaluate(
            f"""
            () => {{
                window.sessionStorage.setItem('token', '{token}');
            }}
            """
        )
        print("Session token restored.")
    return page

def main():
    with sync_playwright() as playwright:
        # Login and create a page instance
        page = login_with_saved_state(playwright)

        # Perform test cases sequentially
        #create_batch(page)
        # add_student(page)
        add_billing(page)
        # add_billingcheck(page)

        # Keep the browser open for debugging
        input("Press Enter once you're ready to exit...")
        page.context.browser.close()

if __name__ == "__main__":
    main()


