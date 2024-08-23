from django.shortcuts import render
from flask import Blueprint, render_template
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, StaleElementReferenceException
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from werkzeug.utils import secure_filename
import os

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'D:/OfficeWork/HiredSiteBot/core/static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Ensure the directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Ensure the directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)




# Create your views here.


def index(request):
    result = None
    
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        url = request.POST.get('url')
        resume = request.FILES.get('resume')
        profile_picture = request.FILES.get('profile_picture')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        city = request.POST.get('city')
        am_value = request.POST.get('am')
        degree = request.POST.get('degree')
        employment_status = request.POST.get('employment-status')
        
        university_name = request.POST.get('university_name')
        start_month = request.POST.get('start_month')
        start_year = request.POST.get('start_year')
        
        graduate_month = request.POST.get('graduate_month')
        graduate_year = request.POST.get('graduate_year')
        major = request.POST.get('major')
        cgpa = request.POST.get('cgpa')
        hometown = request.POST.get('hometown')
        f_gen = request.POST.get('f_gen')
        f_gen_community = request.POST.get('f_gen_community')
        sponsorship = request.POST.get('sponsorship')
        
                
    
        
        gender = request.POST.get('gender')
        ethnicity = request.POST.get('ethnicity')
        veteran_status = request.POST.get('veteran_status')
        
        

        
        
        if resume and allowed_file(resume.name):
            resume_filename = secure_filename(resume.name)
            resume_path = os.path.join(UPLOAD_FOLDER, resume_filename)
            with open(resume_path, 'wb+') as destination:
                for chunk in resume.chunks():
                    destination.write(chunk)

            
        if profile_picture:
            profile_picture_filename = secure_filename(profile_picture.name)
            profile_picture_path = os.path.join(UPLOAD_FOLDER, profile_picture_filename)
            with open(profile_picture_path, 'wb+') as destination:
                for chunk in profile_picture.chunks():
                    destination.write(chunk)
                    
            
            


            
        
                        
        

        driver = webdriver.Chrome()
        try:
            driver.get("https://www.wayup.com/member/register")

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]'))
            ).send_keys(email)

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))
            ).send_keys(password)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))
            ).click()

            time.sleep(5)
                        
                       
                                    
            
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"][accept="application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/pdf"]')
            file_input.send_keys(resume_path)
            
            
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='firstName']"))
            ).send_keys(first_name)           
            
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='lastName']"))
            ).send_keys(last_name)            
                        
                        
            
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
            ).click()
            
            
          # Scroll to the city container
            city_container = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.currentLocation"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", city_container)
            city_container.click()

            
            hidden_input = None
            try:
                hidden_input = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="react-select-343-input"]'))
                )
            except TimeoutException:
                try:
                    hidden_input = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id^="react-select-"][type="text"]'))
                    )
                except TimeoutException:
                    print("Hidden input element not found.")
            
            if hidden_input:
                # Enter the city name using JavaScript to set the value
                driver.execute_script(f"arguments[0].setAttribute('value', '{city}')", hidden_input)
                
                
                
                # Dispatch input and change events to ensure the value is recognized
                driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", hidden_input)
                driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", hidden_input)
                
                
                
                

                    
                try:
                # Wait for the suggestions menu to appear
                    print("Waiting for the suggestions menu to appear...")
                    suggestions_menu = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.css-njjcag-menu'))
                    )
                    print("Suggestions menu found")
                    
                    # Use JavaScript to make sure the suggestions are visible
                    print("Scrolling to suggestions menu...")
                    driver.execute_script("arguments[0].scrollIntoView(true);", suggestions_menu)
                    print("Scrolled to suggestions menu")

                    print("Finding suggestion elements...")
            
                    
                    child_divs_xpath = './/div[contains(@class, "css-yt9ioa-option") or contains(@class, "css-1n7v3ny-option")]'
                    
                    try:
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_all_elements_located((By.XPATH, child_divs_xpath))
                        )
                        child_divs = driver.find_elements(By.XPATH, child_divs_xpath)
                        
                        # Click on the first child div
                        # Click on the first child div
                        if child_divs:
                            first_child_div = child_divs[0]
                            attempt = 0
                            while attempt < 3:
                                try:
                                    first_child_div.click()
                                    print("Clicked on the first suggestion: ", first_child_div.text)
                                    break
                                except StaleElementReferenceException:
                                    attempt += 1
                                    child_divs = driver.find_elements(By.XPATH, child_divs_xpath)
                                    if child_divs:
                                        first_child_div = child_divs[0]
                                        
                            else:
                                print("Failed to click on the first suggestion after multiple attempts.")
                        else:
                            print("No suggestion elements found.")
                    except Exception as e:
                        print("Error:", e)
                        
                        
                    
                    

                    
                except TimeoutException as e:
                    print(f"TimeoutException: {e}")
                    driver.save_screenshot('timeout_screenshot.png')  
                except Exception as e:
                    print(f"An error occurred: {e}")
                    driver.save_screenshot('error_screenshot.png')
                    
                
            else:
                print("Failed to locate the hidden input element.")

            
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[19]/div/div/div/div/div[1]/div'))
            ).click()
            
    
            
            if am_value == "am":
                am_option = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "react-select-3-option-0"))
                )
                am_option.click()
            elif am_value == "am not":
                am_option = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "react-select-3-option-1"))
                )
                am_option.click()
            else:
                raise ValueError("Invalid AM option value")
            
            time.sleep(2)
            
            
            
            
            if profile_picture_path:
                profile_pic_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"][accept="image/png, image/jpeg"]')
                profile_pic_input.send_keys(profile_picture_path)
                
            
            
            
            time.sleep(2)
            
                    
            next_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[25]/div/button'))
            )
            
            next_button.click()   
            
             
                
            # degree_click = WebDriverWait(driver, 5).until(
            #     EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[6]/div[1]/div/div/div'))
            # )
            
            # degree_click.click()
            
            
            
            
            def select_degree(driver, degree_value):
                # Map degree values to their respective IDs
                degree_id_map = {
                    "Associate's": "react-select-4-option-0",
                    "Bachelor's": "react-select-4-option-1",
                    "Master's": "react-select-4-option-2",
                    "MBA": "react-select-4-option-3",
                    "M.D.": "react-select-4-option-4",
                    "J.D.": "react-select-4-option-5",
                    "Ph.D": "react-select-4-option-6",
                    "Other degree": "react-select-4-option-7",
                    "No Degree": "react-select-4-option-8"
                }

                option_id = degree_id_map.get(degree_value)
                
                if not option_id:
                    print(f"Degree value '{degree_value}' is not recognized.")
                    return

                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-4-input"]'))  # Adjust this XPath if needed
                    )
                    dropdown.click()

                    # Find the specific degree option using its ID and click it
                    degree_option = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.ID, option_id))
                    )
                    degree_option.click()

                    print(f"Selected degree: {degree_value}")

                except TimeoutException:
                    print(f"Option with value '{degree_value}' not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")

                    


                                                
            
            select_degree(driver, degree)
            
            time.sleep(2)
            
            
            

            
            def select_status(driver, status_value):
                
                
                status_click = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[6]/div[2]/div/div/div[1]/div[1]'))
                        )
                    
                status_click.click() 
                                


                

                
                                                
                # Map status values to their respective XPath or ID
                status_xpath_map = {
                    "full-time": 'react-select-14-option-0',
                    "part-time": 'react-select-14-option-1'
                }
                

                status_xpath = status_xpath_map.get(status_value)
                
                if not status_xpath:
                    print(f"Status value '{status_value}' is not recognized.")
                    return

                try:
                    # Wait for the status option to be clickable and click it
                    status_option = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.ID, status_xpath))
                    )
                    status_option.click()

                    print(f"Selected status: {status_value}")

                except TimeoutException:
                    print(f"Option with value '{status_value}' not found.")
                except Exception as e:
                    print(f"An error occurred: {e}" )   
                    
            
            select_status(driver,employment_status)   
            
            
            campus_click = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-5-input"]'))
            )
        
            campus_click.click() 
            
            time.sleep(2)     
            
            
            campus_click.send_keys(university_name)
            
            
            first_option = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-5-option-0"]'))
            )

            # Click on the first option
            first_option.click()    
            
            def select_month(driver: webdriver, month_name: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-6-input"]'))
                    )
                    dropdown.click()
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific month option using the provided month_name and click it
                    month_option = options_menu.find_element(By.XPATH, f'.//div[text()="{month_name}"]')
                    month_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")

                # Example usage
            select_month(driver, start_month) 
            
            time.sleep(1)


            
            def select_year(driver: webdriver, year: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-7-input"]'))
                    )
                    dropdown.click()
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific year option using the provided year and click it
                    year_option = options_menu.find_element(By.XPATH, f'.//div[text()="{year}"]')
                    year_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Example usage
            select_year(driver, start_year) 
            
            
            
                        
            time.sleep(2)
            
            
            def graduate_select_month(driver: webdriver, month_name: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-8-input"]'))
                    )
                    dropdown.click()
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific month option using the provided month_name and click it
                    month_option = options_menu.find_element(By.XPATH, f'.//div[text()="{month_name}"]')
                    month_option.click()


                    
                except Exception as e:
                    print(f"An error occurred: {e}")

                # Example usage
            graduate_select_month(driver, graduate_month)    
            
            
            time.sleep(2)
            
            
            def gradudate_select_year(driver: webdriver, year: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-9-input"]'))
                    )
                    dropdown.click()
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific year option using the provided year and click it
                    year_option = options_menu.find_element(By.XPATH, f'.//div[text()="{year}"]')
                    year_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Example usage
            gradudate_select_year(driver, graduate_year)   
            
            time.sleep(2)     

                        
            
            def major_option(driver: webdriver, input_text: str):
                try:
                    # Locate the input box where the user types the query
                    input_box = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-10-input"]'))
                    )
                    # Click the input box to focus and then type the input_text
                    input_box.click()
                    input_box.send_keys(input_text)
                    
                    # Optionally wait for the input text to be processed, if necessary
                    # e.g., time.sleep(1) # This can be adjusted based on the app's response time
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )
                    
                    time.sleep(2)
                    

                    
                    # Select the first suggestion in the dropdown
                    first_option = options_menu.find_element(By.XPATH, './/div[contains(@class, "css-1n7v3ny-option") or contains(@class, "css-yt9ioa-option")]')
                    first_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")

                    


            # Example usage
            major_option(driver, major) 
            
            
            time.sleep(2)
            
            def CGPA_Option(driver: webdriver, year: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-15-input"]'))
                    )
                    dropdown.click()
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific year option using the provided year and click it
                    year_option = options_menu.find_element(By.XPATH, f'.//div[text()="{year}"]')
                    year_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")

            
            CGPA_Option(driver, cgpa)
            
            
            
            time.sleep(2)
            
            
            def HomwTown_option(driver: webdriver, input_text: str):
                try:
                    # Locate the input box where the user types the query
                    input_box = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-16-input"]'))
                    )
                    # Click the input box to focus and then type the input_text
                    input_box.click()
                    input_box.send_keys(input_text)
                    
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 8).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )
                    
                    
                    time.sleep(2)
                                
                    
                    # Select the first suggestion in the dropdown
                    first_option = options_menu.find_element(By.XPATH, './/div[contains(@class, "css-1n7v3ny-option") or contains(@class, "css-yt9ioa-option")]')
                    first_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Example usage
            HomwTown_option(driver, hometown)
            
            
            # Additional Demographics
            
            
            def Generation_Option(driver: webdriver, year: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[19]/div[1]/div/div/div'))
                    )
                    dropdown.click()
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific year option using the provided year and click it
                    year_option = options_menu.find_element(By.XPATH, f'.//div[text()="{year}"]')
                    year_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")
                    

            
            Generation_Option(driver, f_gen)
            
            
            time.sleep(2)

            def community_Option(driver: webdriver, year: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[21]/div/div/div/div/div[1]'))
                    )
                    dropdown.click()
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific year option using the provided year and click it
                    year_option = options_menu.find_element(By.XPATH, f'.//div[text()="{year}"]')
                    year_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")
                    

            
            community_Option(driver, f_gen_community)
            
            
            
            def sponsorship_Option(driver: webdriver, year: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[23]/div/div/div/div/div[1]'))
                    )
                    dropdown.click()
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific year option using the provided year and click it
                    year_option = options_menu.find_element(By.XPATH, f'.//div[text()="{year}"]')
                    year_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")
         
     


      
            sponsorship_Option(driver, sponsorship)
            
            
            

            next_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[25]/div[2]/button'))
            )
            
            next_button.click()            
            
            
            
            time.sleep(3)
            
            def gender_Option(driver: webdriver, year: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[6]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]'))
                    )
                    dropdown.click()
                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific year option using the provided year and click it
                    year_option = options_menu.find_element(By.XPATH, f'.//div[text()="{year}"]')
                    year_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")
                

            
            gender_Option(driver, gender)
            
            
            time.sleep(2)
            
            
            def Ethnicity_Option(driver: webdriver, year: str):
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[6]/div[1]/div[2]/div[2]/div[2]/div/div'))
                    )
                    dropdown.click()
                    
                    

                    
                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific year option using the provided year and click it
                    year_option = options_menu.find_element(By.XPATH, f'.//div[text()="{year}"]')
                    year_option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")
                    
            Ethnicity_Option(driver, ethnicity)
            
            
            time.sleep(2)
                        

            
            def Veteran_Status(driver: webdriver, option_text: str):
       
                try:
                    # Click on the dropdown to reveal the options
                    dropdown = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[6]/div[1]/div[3]/div/div[3]/div/div/div[1]'))
                    )
                    dropdown.click()

                    # Wait for the dropdown options to be visible
                    options_menu = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "css-njjcag-menu")]'))
                    )

                    # Find the specific option using the provided text and click it
                    option = options_menu.find_element(By.XPATH, f'.//div[text()="{option_text}"]')
                    option.click()
                    
                except Exception as e:
                    print(f"An error occurred: {e}")

            Veteran_Status(driver, veteran_status)
            
            
            finish_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[6]/div[3]/div[2]/button'))
            )
            
            
                
        
    
            finish_button.click()
            
                            
                            
                        
    
            

                                                                    
                                    
            input("Press enter to contine..")      
            
            
            

            result = "Form submitted successfully!"
        except TimeoutException:
            result = "Timed out waiting for page elements."
        except ElementClickInterceptedException:
            result = "Element click intercepted. Try manually."
        except StaleElementReferenceException:
            result = "Stale element reference. Refresh the page and try again."
        finally:
            driver.quit()
    
    
    
    
    return render(request,'index.html',{'result':result})

