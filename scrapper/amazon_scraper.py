import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Open undetected Chrome
driver = uc.Chrome()

# Amazon review page
url = "https://www.amazon.in/product-reviews/B0DSKL9MQ8/ref=cm_cr_dp_d_show_all_top?_encoding=UTF8&ie=UTF8&reviewerType=all_reviews"

driver.get(url)

# Wait for page load
time.sleep(10)

# IMPORTANT:
# Solve CAPTCHA manually if it appears
input("After page fully loads and CAPTCHA solved, press ENTER...")

# Find reviews
reviews = driver.find_elements(By.CSS_SELECTOR, '[data-hook="review"]')

print("Total Reviews Found:", len(reviews))

data = []

for review in reviews:

    try:
        customer = review.find_element(By.CSS_SELECTOR, '.a-profile-name').text
    except:
        customer = "N/A"

    try:
        review_text = review.find_element(By.CSS_SELECTOR, '[data-hook="review-body"]').text
    except:
        review_text = "N/A"

    try:
        rating = review.find_element(By.CSS_SELECTOR, '[data-hook="review-star-rating"]').text
    except:
        rating = "N/A"

    try:
        title = review.find_element(By.CSS_SELECTOR, '[data-hook="review-title"]').text
    except:
        title = "N/A"

    data.append({
        "Customer Name": customer,
        "Review Title": title,
        "Review": review_text,
        "Rating": rating
    })

# Create dataframe
df = pd.DataFrame(data)

print(df)

# Save CSV
df.to_csv("amazon_reviews.csv", index=False)

print("\nCSV File Saved Successfully!")

driver.quit()