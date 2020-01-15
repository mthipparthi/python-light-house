from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from requests_html import HTMLSession


def main():
    driver = webdriver.Chrome()
    driver.get("http://apply.dataprocessors.com.au")
    # assert "Python" in driver.title
    res = driver.find_elements_by_xpath("/html/body/form/p[2]")
    images = res[0].find_elements_by_tag_name("img")

    imageCount = filledcircle_count(images)
    jobRef = driver.find_element_by_name("jobref")
    jobRef.clear()
    jobRef.send_keys("PO178")
    jobRef = driver.find_element_by_name("valuee")
    jobRef.send_keys(imageCount)
    jobRef.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


def filledcircle_count(images):
    count = 0
    for i in images:
        if i.get_attribute("src").endswith("/filledO.gif"):
            count += 1
    return count


if __name__ == "__main__":
    # print(filledcircle_count())
    main()
